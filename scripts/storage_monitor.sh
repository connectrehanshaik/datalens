#!/usr/bin/env bash
set -euo pipefail

echo "============================================================"
echo "          DATALENS STORAGE & RUNTIME TELEMETRY             "
echo "============================================================"
echo -e "\n[1] Block Storage Utilization:"
df -h / /var/log

echo -e "\n[2] Inode Allocation:"
df -i / /var/log

echo -e "\n[3] Log Footprint:"
ls -lh /var/log/datalens/

echo -e "\n[4] Open Descriptor Leak Check:"
sudo lsof +L1 2>/dev/null | grep "/var/log/datalens" || echo "Clean: No unlinked open descriptors."

echo -e "\n[5] Metrics Endpoint Health Check:"
curl -s http://127.0.0.1:9100/healthz || echo "Health check endpoint waiting for service start..."
echo -e "\n============================================================"
