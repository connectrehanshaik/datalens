#!/usr/bin/env bash
set -euo pipefail

echo "============================================================"
echo "          DATALENS STORAGE & INODE AUDIT REPORT            "
echo "============================================================"

echo -e "\n[1] Block Device Storage Utilization:"
df -h / /var/log

echo -e "\n[2] Inode Allocation Table:"
df -i / /var/log

echo -e "\n[3] DataLens Log Directory Footprint:"
if [ -d "/var/log/datalens" ]; then
    ls -lh /var/log/datalens/
else
    echo "Directory /var/log/datalens does not exist yet."
fi

echo -e "\n[4] Open File Handles Holding Deleted Inodes (lsof check):"
DELETED_FILES=$(sudo lsof +L1 2>/dev/null | grep "/var/log/datalens" || true)
if [ -z "$DELETED_FILES" ]; then
    echo "Clean: No unlinked open file descriptors detected in /var/log/datalens."
else
    echo "WARNING: Deleted files still held by open PIDs:"
    echo "$DELETED_FILES"
fi

echo "============================================================"
