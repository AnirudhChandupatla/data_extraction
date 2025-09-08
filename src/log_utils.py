from __future__ import annotations

import logging
from pathlib import Path
import uuid
import sys
from typing import Tuple, Optional, Iterator
from contextlib import contextmanager


class ExtractionLogManager:
    """
    Manage extraction logging:
    - Configure a parent 'extract' logger with an idempotent console (stdout) handler.
    - Create a unique extraction root directory.
    - Provide per-page loggers that write to page_{NNNN}/log.md with context-managed or manual APIs.
    """

    def __init__(
        self,
        base_dir: Path,
        *,
        parent_logger_name: str = "extract",
        level: int = logging.INFO,
        enable_console: bool = True,
        console_format: str = "%(asctime)s | %(levelname)s | %(message)s",
    ) -> None:
        self.base_dir = Path(base_dir)
        self.parent_logger_name = parent_logger_name
        self.level = level
        self.console_format = console_format

        # Configure parent logger
        self.parent = logging.getLogger(self.parent_logger_name)
        self.parent.setLevel(self.level)
        self.parent.propagate = False  # do not bubble to root to avoid duplicates

        if enable_console:
            self._ensure_console_handler()

    def _ensure_console_handler(self) -> None:
        """Attach a single stdout StreamHandler to the parent logger (idempotent)."""
        has_stream = any(isinstance(h, logging.StreamHandler) for h in self.parent.handlers)
        if not has_stream:
            ch = logging.StreamHandler(stream=sys.stdout)  # default would be stderr
            ch.setLevel(self.level)
            ch.setFormatter(logging.Formatter(self.console_format))
            self.parent.addHandler(ch)

    def set_level(self, level: int) -> None:
        """Update the logging level on the parent logger and its console handler."""
        self.level = level
        self.parent.setLevel(level)
        for h in self.parent.handlers:
            h.setLevel(level)

    def create_extraction_root(self) -> Tuple[str, Path]:
        """
        Create a unique extraction root named by a UUID.
        Returns (extraction_id, root_path).
        """
        extraction_id = str(uuid.uuid4())
        root = self.base_dir / extraction_id
        root.mkdir(parents=True, exist_ok=False)
        return extraction_id, root

    def _page_logger_name(self, extraction_id: str, page_num: int) -> str:
        return f"{self.parent_logger_name}.{extraction_id}.page.{page_num:04d}"

    def _ensure_page_dir(self, root: Path, page_num: int) -> Path:
        page_dir = Path(root) / f"page_{page_num:04d}"
        page_dir.mkdir(parents=True, exist_ok=True)
        return page_dir

    def start_page_logger(
        self,
        root: Path,
        extraction_id: str,
        page_num: int,
        level: Optional[int] = None,
        file_format: str = "%(asctime)s | %(levelname)s | %(message)s",
    ):
        """
        Start per-page logging by attaching a FileHandler to page_{NNNN}/log.md.
        Returns (logger, page_dir, file_handler).
        """
        lvl = self.level if level is None else level
        page_dir = self._ensure_page_dir(root, page_num)

        logger_name = self._page_logger_name(extraction_id, page_num)
        logger = logging.getLogger(logger_name)
        logger.setLevel(lvl)
        logger.propagate = True  # let messages flow to parent (console)

        log_file = page_dir / "log.md"
        fh = logging.FileHandler(log_file, encoding="utf-8", delay=True)
        fh.setLevel(lvl)
        fh.setFormatter(logging.Formatter(file_format))
        logger.addHandler(fh)

        return logger, page_dir, fh

    def stop_page_logger(self, logger: logging.Logger, fh: logging.FileHandler) -> None:
        """
        Detach and close the per-page FileHandler, leaving other handlers intact.
        """
        try:
            logger.removeHandler(fh)
        finally:
            fh.close()

    @contextmanager
    def page_logger(
        self,
        root: Path,
        extraction_id: str,
        page_num: int,
        level: Optional[int] = None,
        file_format: str = "%(asctime)s | %(levelname)s | %(message)s",
    ):
        """
        Context-managed per-page logger:
        - creates page dir and file handler
        - yields (logger, page_dir)
        - ensures cleanup of the file handler on exit
        """
        logger, page_dir, fh = self.start_page_logger(
            root=root,
            extraction_id=extraction_id,
            page_num=page_num,
            level=level,
            file_format=file_format,
        )
        try:
            yield logger, page_dir
        finally:
            self.stop_page_logger(logger, fh)


'''
# One-time setup
mgr = ExtractionLogManager(base_dir=Path("./runs"), parent_logger_name="extract", level=logging.INFO, enable_console=True)

# Create a unique extraction root
extraction_id, root = mgr.create_extraction_root()

# Context-managed per-page logging
with mgr.page_logger(root, extraction_id, page_num=1) as (logger, page_dir):
    logger.info("Starting page 1")
    # ... work ...
    logger.info("Finished page 1")

# Or manual start/stop
logger, page_dir, fh = mgr.start_page_logger(root, extraction_id, page_num=2)
try:
    logger.info("Processing page 2")
finally:
    mgr.stop_page_logger(logger, fh)

'''