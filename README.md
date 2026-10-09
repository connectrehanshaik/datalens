Enterprise DevOps baseline on Ubuntu/WSL2 demonstrating Linux storage monitoring, PID 1 supervision, zero-downtime log rotation, and CGroup v2 resource hardening.
* **Worker**: Python 3.12+ daemon using timezone-aware UTC timestamps and unbuffered I/O.
* **Supervision**: `systemd` (`datalens.service`) providing lifecycle management (`Restart=always`, `RestartSec=3`).
* **Resource Isolation**: Linux CGroup v2 limits enforced at the unit level:
  * `MemoryMax=64M`
  * `CPUQuota=20%`
* **Log Rotation**: `logrotate` via the `copytruncate` pattern, maintaining a 7-day retention window with `gzip` compression (>90% space reduction).
* **Journal Boundaries**: `systemd-journald` capped at `SystemMaxUse=100M`.
## Repository Structure

* `scripts/heartbeat_worker.py`: Primary supervised worker daemon.
* `scripts/storage_monitor.sh`: Block storage and inode capacity audit tool.
* `scripts/memory_allocator_test.py`: CGroup OOM limit validation harness.
* `systemd/datalens.service`: Hardened Systemd unit file.
* `config/logrotate.datalens`: Declarative logrotate policy.
