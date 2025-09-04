#!/usr/bin/env bash
set -euo pipefail

# Ensure a writable HOME for javaldx and extensions
export HOME="${HOME:-/tmp}"
mkdir -p "$HOME"

# Start LibreOffice headless with UNO socket (no spaces in accept)
soffice --headless --invisible --norestore \
  --accept="socket,host=127.0.0.1,port=2002;urp;StarOffice.ServiceManager" &
lo_pid=$!

# Ensure soffice is reaped on exit
trap 'kill -TERM "$lo_pid" 2>/dev/null || true; wait "$lo_pid" 2>/dev/null || true' EXIT INT TERM

# Wait up to 20s for the UNO port to open
for i in {1..20}; do
  sleep 1
  if ss -ltn | grep -q ':2002'; then
    break
  fi
done

# Run the Flask app (becomes PID 1)
exec python3 app/server.py
