# fetch_internships

Fetches CS internship postings from the SimplifyJobs github repo, scores them against a resume profile, and outputs a styled Excel spreadsheet.

## Scripts

| File            | Description                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `fetch.py`      | Main script — clones/updates the SimplifyJobs repo, parses and filters postings, scores them, and writes an `.xlsx` to `./Internships/` |
| `scheduler.py`  | Daemon that runs `fetch.py` once daily at a set time (requires WSL to stay open)                                                        |
| `run_daily.bat` | Script for Windows Task Scheduler                                                                                                       |
| `run_daily.sh`  | Same script as above but runs directly from terminal                                                                                    |

## Usage

```bash
# Today's postings only (posted 0 days ago)
python fetch.py

# Include postings up to n days old
python fetch.py --days n
python fetch.py -d n

# Send spreadsheet by email (uses TO_EMAIL from .env if --email not provided)
python fetch.py
python fetch.py --email you@gmail.com
python fetch.py -d 1 --email you@gmail.com

# Run scheduler daemon
python scheduler.py --time 09:00
nohup python scheduler.py --time 09:00 &
```

## Email Setup

Create a `.env` file with the following format:

```
GMAIL_USER=you@gmail.com
GMAIL_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
TO_EMAIL=you@gmail.com
```

Generate an app password at: Google Account → Security → 2-Step Verification → App passwords.
