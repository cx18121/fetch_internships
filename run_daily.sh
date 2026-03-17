#!/bin/bash
# Daily internship fetcher — alternative to run_daily.bat for running directly in WSL/Linux.
# Email recipient and credentials are read from .env next to fetch.py.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_DIR/fetch.py" -d 1
