@echo off
:: Daily internship fetcher — runs via Windows Task Scheduler
:: Credentials are read from .env next to fetch.py — do not put them here.

set TO_EMAIL=charlie.l.xue@gmail.com

wsl python3 /mnt/c/Users/charl/School/cs_misc/fetch_internships/fetch.py -d 1 --email %TO_EMAIL%
