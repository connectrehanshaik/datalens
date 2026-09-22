#!/usr/bin/env python3
import time
import os

print(f"[*] Process ID (PID): {os.getpid()}")
print("[*] Allocating memory in chunks of ~100MB... Press Ctrl+C to stop.")

chunks = []
try:
    for i in range(1, 11):  # Allocate up to ~1GB in 10 steps
        chunks.append(b"x" * (100 * 1024 * 1024))
        print(f" -> Allocated {i * 100} MB (Current RSS footprint expanding)")
        time.sleep(1)
    print("[+] Test completed. Holding memory for 5 seconds...")
    time.sleep(5)
except KeyboardInterrupt:
    print("\n[!] Stopped by user.")
