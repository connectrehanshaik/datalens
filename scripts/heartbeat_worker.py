#!/usr/bin/env python3
import time
import os
from datetime import datetime, timezone

LOG_FILE = "/var/log/datalens/app.log"
print(f"[*] DataLens Service running under CGroup limits. Output directed to {LOG_FILE}", flush=True)

count = 1
while True:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now} UTC] [HEARTBEAT] #{count} - Worker healthy (PID {os.getpid()})\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
        f.flush()
    count += 1
    time.sleep(2)
