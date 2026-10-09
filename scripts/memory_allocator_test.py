#!/usr/bin/env python3
"""
DataLens Stress Testing & Chaos Harness
Simulates deliberate memory expansion to validate CGroup MemoryMax=64M isolation.
"""
import os
import sys
import time

def allocate_chunk(megabytes: int):
    pid = os.getpid()
    print(f"[*] PID {pid}: Allocating {megabytes} MB into physical memory...", flush=True)
    chunk = bytearray(megabytes * 1024 * 1024)
    print(f"[*] Allocation complete. Resident size increased by {megabytes} MB.", flush=True)
    return chunk

def main():
    print("=== DataLens Memory Stress Test ===", flush=True)
    print("[*] Baseline process holding 10 MB...", flush=True)
    baseline = allocate_chunk(10)
    time.sleep(2)

    target_leak = 100
    print(f"[!] TRIGGERING OVER-LIMIT SPIKE: Allocating {target_leak} MB...", flush=True)
    spike = allocate_chunk(target_leak)

    print("[*] Holding allocation. Expecting kernel CGroup intervention...", flush=True)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
