#!/usr/bin/env bash

set -euo pipefail

echo "===================================================="
echo "      DATALENS SERVER HEALTH DIAGNOSTIC REPORT     "
echo "===================================================="
echo "Timestamp: $(date)"
echo ""

# 1. Check Disk Space Usage on Root Partition
echo "[*] Checking Root Disk Partition Usage..."
DISK_USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//g')

if [ "$DISK_USAGE" -gt 80 ]; then
    echo "WARNING: Disk usage is critically high at ${DISK_USAGE}%!"
else
    echo "OK: Root disk usage is at ${DISK_USAGE}%."
fi
echo ""

# 2. Check Memory Consumption
echo "[*] Checking Memory (RAM) Usage..."
free -h
echo ""

# 3. Check Top 3 Memory-Consuming Processes
echo "[*] Top 3 Processes Consuming Memory:"
ps aux --sort=-%mem | head -n 4
echo ""

# 4. Check Network Listening Ports
echo "[*] Active Listening Ports (TCP/UDP):"
ss -tulnp | head -n 10
echo ""

echo "===================================================="
echo "Diagnostic complete."
