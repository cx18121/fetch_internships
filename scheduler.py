"""
scheduler.py — Run fetch.py every day at a specified time.

Usage:
    python scheduler.py              # runs at 09:00 by default
    python scheduler.py --time 08:30
    python scheduler.py --time 17:00 --days 1 --email you@gmail.com
"""

import argparse
import datetime
import subprocess
import sys
import time
from pathlib import Path

FETCH = Path(__file__).parent / "fetch.py"


def seconds_until(target_time: datetime.time) -> float:
    now = datetime.datetime.now()
    run_at = datetime.datetime.combine(now.date(), target_time)
    if run_at <= now:
        # Already passed today — schedule for tomorrow
        run_at += datetime.timedelta(days=1)
    return (run_at - now).total_seconds()


def run_fetch(days: int, email: str | None):
    cmd = [sys.executable, str(FETCH), "--days", str(days)]
    if email:
        cmd += ["--email", email]
    print(f"\n[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] Running: {' '.join(cmd)}")
    subprocess.run(cmd)


def main():
    parser = argparse.ArgumentParser(description="Daily scheduler for fetch.py")
    parser.add_argument(
        "--time", "-t",
        default="09:00",
        metavar="HH:MM",
        help="Time to run each day in 24h format (default: 09:00)",
    )
    parser.add_argument("--days", "-d", type=int, default=0, metavar="N",
                        help="--days value passed to fetch.py (default: 0)")
    parser.add_argument("--email", "-e", metavar="ADDRESS",
                        help="--email value passed to fetch.py")
    args = parser.parse_args()

    try:
        target = datetime.time.fromisoformat(args.time)
    except ValueError:
        print(f"Invalid time '{args.time}'. Use HH:MM format (e.g. 09:00).")
        sys.exit(1)

    print(f"Scheduler started — will run fetch.py daily at {target.strftime('%H:%M')}")
    print("Press Ctrl+C to stop.\n")

    while True:
        secs = seconds_until(target)
        wake = datetime.datetime.now() + datetime.timedelta(seconds=secs)
        print(f"Next run at {wake:%Y-%m-%d %H:%M:%S} (sleeping {secs/3600:.1f}h)")
        time.sleep(secs)
        run_fetch(args.days, args.email)


if __name__ == "__main__":
    main()
