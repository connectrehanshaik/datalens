#!/usr/bin/env python3
import os, time
pid = os.getpid()
print(f"[*] PID {pid}: Running CGroup Boundary Test...", flush=True)
chunk = bytearray(80 * 1024 * 1024)  # 80MB intentionally triggers MemoryMax=64M
print("[*] Allocated test memory. Monitoring kernel behavior...", flush=True)
while True:
    time.sleep(1)
