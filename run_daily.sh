#!/bin/bash
# Daily internship fetcher — alternative to run_daily.bat for running directly in WSL/Linux.
# Credentials are read from .env next to fetch.py — do not put them here.

TO_EMAIL="charlie.l.xue@gmail.com"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_DIR/fetch.py" --email "$TO_EMAIL"
