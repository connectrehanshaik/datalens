#!/usr/bin/env python3
"""
DataLens Production Heartbeat Service
Logs periodic worker health status with UTC timestamps and unbuffered I/O.
"""
import os
import sys
import time
from datetime import datetime, timezone

LOG_DIR = "/var/log/datalens"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

def init_environment():
    if not os.path.exists(LOG_DIR):
        try:
            os.makedirs(LOG_DIR, exist_ok=True)
        except PermissionError:
            print(f"[!] Critical: Cannot create {LOG_DIR}. Check permissions.", file=sys.stderr)
            sys.exit(1)

def main():
    init_environment()
    pid = os.getpid()
    print(f"[*] DataLens Service running under CGroup limits (PID {pid}). Directing output to {LOG_FILE}", flush=True)

    heartbeat_seq = 1
    while True:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp} UTC] [HEARTBEAT] #{heartbeat_seq} - Status: HEALTHY (PID: {pid})\n"
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)
                f.flush()
        except Exception as e:
            print(f"[!] Error writing to log: {e}", file=sys.stderr, flush=True)

        heartbeat_seq += 1
        time.sleep(2)

if __name__ == "__main__":
    main()
