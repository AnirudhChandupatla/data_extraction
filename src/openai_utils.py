from __future__ import annotations

import os
import time
import logging
import random 
from typing import Any, Dict, List, Tuple, Optional

from dotenv import load_dotenv
from openai import AzureOpenAI, APIError, RateLimitError, APIConnectionError, APITimeoutError

import tiktoken


class AzureResponsesClient:
    """
    Azure OpenAI Responses API helper:
    - Loads credentials from environment (dotenv supported)
    - Constructs an AzureOpenAI client
    - Provides response parsing and usage/cost accounting
    - Invokes multimodal prompts (text + image) via Responses API
    - Uses an internally resolved logger compatible with ExtractionLogManager
    """

    def __init__(
        self,
        *,
        model: str,
        system_prompt: str = "",
        user_prompt: str = "",
        api_version: str = "2025-03-01-preview",
        endpoint_env: str = "AZURE_OPENAI_API_ENDPOINT",
        key_env: str = "AZURE_OPENAI_API_KEY",
        # Logger resolution compatible with ExtractionLogManager:
        parent_logger_name: str = "extract",
        extraction_id: Optional[str] = None,
        page_num: Optional[int] = None,
        # Optional direct overrides for endpoint/key (fallback to env if None):
        azure_endpoint: Optional[str] = None,
        azure_api_key: Optional[str] = None,
        # Token pricing knobs (can be customized):
        price_fallback_gpt_in: float = 1.25,
        price_fallback_gpt_cached_in: float = 0.125,
        price_fallback_gpt_out: float = 10.00,
        price_gpt5mini_in: float = 0.25,
        price_gpt5mini_cached_in: float = 0.025,
        price_gpt5mini_out: float = 2.00,
    ) -> None:
        # Load environment variables from .env if present
        load_dotenv()

        self.model = model
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.api_version = api_version

        # Resolve endpoint and key from args or env
        self.azure_endpoint = azure_endpoint or os.getenv(endpoint_env)
        self.azure_api_key = azure_api_key or os.getenv(key_env)

        if not self.azure_endpoint or not self.azure_api_key:
            raise ValueError("Azure endpoint or API key not provided or missing from environment.")

        # Build the Azure OpenAI client
        self.client = AzureOpenAI(
            azure_endpoint=self.azure_endpoint,
            api_key=self.azure_api_key,
            api_version=self.api_version,
        )

        # Pricing configuration
        self._price_fallback_gpt_in = price_fallback_gpt_in
        self._price_fallback_gpt_cached_in = price_fallback_gpt_cached_in
        self._price_fallback_gpt_out = price_fallback_gpt_out
        self._price_gpt5mini_in = price_gpt5mini_in
        self._price_gpt5mini_cached_in = price_gpt5mini_cached_in
        self._price_gpt5mini_out = price_gpt5mini_out

        # Resolve a logger that matches ExtractionLogManager hierarchy
        if extraction_id is not None and page_num is not None:
            logger_name = f"{parent_logger_name}.{extraction_id}.page.{page_num:04d}"
        else:
            logger_name = parent_logger_name
        self.logger = logging.getLogger(logger_name)

    # ---------------- Response parsing ----------------

    @staticmethod
    def extract_response_text(response) -> Optional[str]:
        """
        Extract text content from the Responses API result, handling object/dict shapes.
        """
        try:
            if response and hasattr(response, "output") and response.output:
                for output_item in response.output:
                    if hasattr(output_item, "type") and output_item.type == "message":
                        if hasattr(output_item, "content") and output_item.content:
                            for content_item in output_item.content:
                                # Dataclass-like shape
                                if hasattr(content_item, "text"):
                                    return content_item.text
                                # Dict-like shape fallback
                                if isinstance(content_item, dict) and "text" in content_item:
                                    return content_item["text"]
            # Dict-like fallback for full response
            if isinstance(response, dict):
                out = response.get("output") or []
                for item in out:
                    if item.get("type") == "message":
                        for ci in item.get("content", []):
                            if "text" in ci:
                                return ci["text"]
            return None
        except Exception as e:
            # Keep non-fatal, log and return None
            logging.getLogger("extract").exception(f"Error extracting response text: {e}")
            return None

    # ---------------- Usage and cost helpers ----------------

    @staticmethod
    def _pick(obj, *names, default=None):
        """Return first non-None attribute or dict key among names for mixed object/dict shapes."""
        if obj is None:
            return default
        for n in names:
            v = getattr(obj, n, None)
            if v is None and isinstance(obj, dict):
                v = obj.get(n)
            if v is not None:
                return v
        return default

    @staticmethod
    def _cached_tokens_from_details(details) -> int:
        """Extract cached_tokens across object and dict variants."""
        if details is None:
            return 0
        if isinstance(details, dict):
            return details.get("cached_tokens", 0) or 0
        return getattr(details, "cached_tokens", 0) or 0

    def extract_usage_counts(self, response) -> Tuple[int, int, int]:
        """
        Extract (input_tokens, output_tokens, cached_tokens) across SDK/dict variations.
        """
        usage = getattr(response, "usage", None) or {}
        input_tokens = self._pick(usage, "input_tokens", "prompt_tokens", default=0)
        output_tokens = self._pick(usage, "output_tokens", "completion_tokens", default=0)
        itd = self._pick(usage, "input_tokens_details", "prompt_tokens_details", default=None)
        cached_tokens = self._cached_tokens_from_details(itd)
        return int(input_tokens or 0), int(output_tokens or 0), int(cached_tokens or 0)

    @staticmethod
    def _get_encoding(model: str):
        """Prefer model encoding, then o200k_harmony, then o200k_base."""
        try:
            return tiktoken.encoding_for_model(model)
        except Exception:
            try:
                return tiktoken.get_encoding("o200k_harmony")
            except Exception:
                return tiktoken.get_encoding("o200k_base")

    def estimate_text_tokens_from_input(self, input_messages: List[Dict[str, Any]], model: str) -> int:
        """
        Estimate text-only tokens from the outgoing payload; ignores images/audio content.
        """
        enc = self._get_encoding(model)
        total = 0
        for msg in input_messages:
            if "role" in msg and msg["role"] is not None:
                total += len(enc.encode(str(msg["role"])))
            content = msg.get("content") or []
            seq = content if isinstance(content, list) else [content]
            for part in seq:
                if isinstance(part, dict) and part.get("type") in ("text", "input_text"):
                    total += len(enc.encode(str(part.get("text", ""))))
                elif isinstance(part, dict) and part.get("type") in ("input_image", "image_url", "image", "input_audio"):
                    continue  # non-text tokens are counted server-side
                elif isinstance(part, str):
                    total += len(enc.encode(part))
        return total

    def model_prices_usd_per_million(self, model: str) -> Dict[str, float]:
        """
        Return USD per-million token rates for input, cached input, and output.
        Replace with current pricing pages in production.
        """
        m = model.lower()
        if "gpt-5-mini" in m:
            return {
                "in": self._price_gpt5mini_in,
                "cached_in": self._price_gpt5mini_cached_in,
                "out": self._price_gpt5mini_out,
            }
        # Default GPT-5-like fallback
        return {
            "in": self._price_fallback_gpt_in,
            "cached_in": self._price_fallback_gpt_cached_in,
            "out": self._price_fallback_gpt_out,
        }

    def compute_cost_usd(self, model: str, input_tokens: int, output_tokens: int, cached_tokens: int = 0) -> Tuple[float, float]:
        """Compute approximate input/output costs using cached/non-cached split."""
        prices = self.model_prices_usd_per_million(model)
        non_cached_in = max(0, int(input_tokens) - max(0, int(cached_tokens)))
        cin = (non_cached_in * prices["in"] + int(cached_tokens) * prices["cached_in"]) / 1_000_000.0
        cout = (int(output_tokens) * prices["out"]) / 1_000_000.0
        return round(cin, 6), round(cout, 6)

    def print_usage_breakdown(self, response, model: str, input_messages: List[Dict[str, Any]]) -> None:
        """
        Log total tokens and estimated text/image split plus cost, to the internally-managed logger.
        """
        input_tokens, output_tokens, cached_tokens = self.extract_usage_counts(response)
        est_text_tokens = self.estimate_text_tokens_from_input(input_messages, model)
        est_image_tokens = max(0, int(input_tokens) - int(est_text_tokens))
        cost_in, cost_out = self.compute_cost_usd(model, input_tokens, output_tokens, cached_tokens=cached_tokens)

        self.logger.info(f"total input tokens: {input_tokens}")
        self.logger.info(f"input text tokens: {est_text_tokens} # estimated")
        self.logger.info(f"input image tokens: {est_image_tokens} # estimated (input - text)")
        self.logger.info(f"cost for input: ${cost_in} USD")
        self.logger.info(f"total output tokens: {output_tokens}")
        self.logger.info(f"cost of output: ${cost_out} USD")

    # ---------------- Invoke ----------------

    def build_input_messages(
        self,
        *,
        system_prompt: Optional[str],
        user_prompt: Optional[str],
        data: str,
        base64_image: str,
        data_type: str = None,
    ) -> List[Dict[str, Any]]:
        """
        Build the multi-part input for the Responses API (system + user with image and text).
        data_type: FULL_RAW_TEXT or MARKDOWN or OCR_COORDINATES
        """
        sys_prompt = system_prompt if system_prompt is not None else self.system_prompt
        usr_prompt = user_prompt if user_prompt is not None else self.user_prompt

        content = []
        if base64_image:
            content.append({
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{base64_image}",
            })
        
        if data_type:
            content.append({
                "type": "input_text",
                "text": f"## {data_type} START:\n{data}\n ## {data_type} END\n",
            })

        if usr_prompt:
            content.append({
                "type": "input_text",
                "text": usr_prompt or "",
            })

        inp: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": [
                    {"type": "input_text", "text": sys_prompt or ""},
                ],
            },
            {
                "role": "user",
                "content": content,
            },
        ]
        return inp

    def _parse_seconds(self, val) -> float:
        """
        Normalize common header formats to seconds (supports '1s', '600ms', '55', etc.).
        """
        if val is None:
            return 0.0
        s = str(val).strip().lower()
        try:
            if s.endswith("ms"):
                return max(0.0, float(s[:-2]) / 1000.0)
            if s.endswith("s"):
                return max(0.0, float(s[:-1]))
            return max(0.0, float(s))
        except Exception:
            return 0.0

    def _retry_after_hint_secs(self, exc) -> float:
        """
        Extract server-provided retry hints from headers: Retry-After or Azure x-ratelimit-reset-*.
        Returns seconds to wait, or 0 if unavailable.
        """
        headers = {}
        try:
            resp = getattr(exc, "response", None)
            headers = getattr(resp, "headers", {}) or {}
            # Coerce to dict in case of a case-insensitive mapping
            try:
                headers = dict(headers)
            except Exception:
                pass
        except Exception:
            headers = {}

        # Case-insensitive header lookup
        def hget(name: str):
            lname = name.lower()
            for k, v in headers.items():
                if str(k).lower() == lname:
                    return v
            return None

        # Standard hint
        ra = hget("retry-after")
        if ra:
            return self._parse_seconds(ra)

        # Azure-specific hints frequently seen on 429
        for key in (
            "x-ratelimit-reset-requests",
            "x-rate-limit-reset-requests",
            "x-ratelimit-reset-tokens",
            "x-rate-limit-reset-tokens",
        ):
            val = hget(key)
            if val:
                return self._parse_seconds(val)

        return 0.0

    def invoke(
        self,
        data: str,
        base64_image: str,
        # Optional overrides per call:
        system_prompt: Optional[str] = None,
        user_prompt: Optional[str] = None,
        reasoning_effort: Optional[str] = None,  # e.g., "low" | "medium" | "high"
        model: Optional[str] = None,             # override model if needed
        data_type: str = None,
        verbosity: str = "low",
        # NEW retry knobs:
        max_retries: int = 6,
        initial_delay: float = 1.0,
        max_delay: float = 60.0,
    ):
        """
        Call the Azure Responses API with retry logic:
        - Prefer server-provided wait hints (Retry-After, x-ratelimit-reset-*)
        - Fallback to randomized exponential backoff with jitter
        - Retry on 429/408/5xx up to max_retries
        """
        try:
            inp = self.build_input_messages(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                data=data,
                base64_image=base64_image,
                data_type=data_type,
            )

            mdl = model if model else self.model
            kwargs: Dict[str, Any] = {
                "model": mdl,
                "input": inp,
                "text": {"verbosity": verbosity},
            }
            if reasoning_effort:
                kwargs["reasoning"] = {"effort": reasoning_effort}

            attempt = 0
            delay = initial_delay

            while True:
                try:
                    start = time.time()
                    resp = self.client.responses.create(**kwargs)
                    self.logger.info(f"llm {mdl} api call took {time.time() - start:.3f} seconds")
                    # Log usage and cost after the call
                    self.print_usage_breakdown(resp, self.model, inp)
                    return resp

                except (RateLimitError, APITimeoutError, APIConnectionError, APIError) as e:
                    # Determine HTTP status if present
                    status = getattr(e, "status_code", None)
                    if status is None:
                        resp = getattr(e, "response", None)
                        status = getattr(resp, "status_code", None)

                    # Retry on 429/408/5xx
                    retriable = status in (429, 408, 500, 502, 503, 504) or isinstance(e, (RateLimitError, APITimeoutError, APIConnectionError))
                    attempt += 1

                    if not retriable or attempt > max_retries:
                        self.logger.exception("Azure Responses API call failed (no more retries or non-retriable).")
                        return None

                    # Prefer server-provided retry hints
                    hint_secs = self._retry_after_hint_secs(e)
                    if hint_secs > 0:
                        wait_secs = min(hint_secs, max_delay)
                    else:
                        # randomized exponential backoff with jitter
                        jitter = random.uniform(0, 0.5 * initial_delay)
                        wait_secs = min(delay + jitter, max_delay)
                        delay = min(delay * 2, max_delay)

                    self.logger.warning(f"Transient error (status={status}) attempt {attempt}/{max_retries}; sleeping {wait_secs:.2f}s before retry.")
                    time.sleep(wait_secs)

                except Exception:
                    self.logger.exception("Azure Responses API call failed (unexpected).")
                    return None
        except Exception:
            self.logger.exception("Azure Responses API outer failure")
            return None

'''
from pathlib import Path
from logging import INFO
# Assuming ExtractionLogManager from your logging refactor is available:
# mgr = ExtractionLogManager(base_dir=Path("./runs"), parent_logger_name="extract", level=INFO, enable_console=True)
# extraction_id, root = mgr.create_extraction_root()
# with mgr.page_logger(root, extraction_id, page_num=1) as (logger, page_dir):
#     # Instantiate the client bound to the same page logger by name (no logger argument needed)
#     client = AzureResponsesClient(
#         model="gpt-5-mini",  # example; use your deployed model name
#         system_prompt="You are a helpful assistant.",
#         user_prompt="Answer concisely.",
#         extraction_id=extraction_id,
#         page_num=1,
#     )
#     resp = client.invoke(full_raw_text="Some text...", base64_image="<base64>", reasoning_effort="low")
#     text = client.extract_response_text(resp)
#     logger.info(f"LLM text: {text}")
'''