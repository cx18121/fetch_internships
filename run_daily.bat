@echo off
:: Daily internship fetcher — runs via Windows Task Scheduler
:: Email recipient and credentials are read from .env next to fetch.py.

wsl python3 /mnt/c/Users/charl/School/cs_misc/fetch_internships/fetch.py -d 1
