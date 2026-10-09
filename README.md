# DataLens — Production DevOps Architecture

Comprehensive Linux infrastructure reference implementation on Ubuntu/WSL2 featuring systemd supervision, CGroup v2 constraints, zero-downtime log rotation, Prometheus instrumentation, containerized deployment, and CI/CD automation.

## System Architecture
* **Worker Daemon**: Python 3.12 unbuffered heartbeat worker with timezone-aware UTC timestamps.
* **Telemetry**: Native Prometheus metrics server exposed on `:9100/metrics` and health probe on `:9100/healthz`.
* **Supervision**: `systemd` (`datalens.service`) managing lifecycle policies with automated restart logic (`Restart=always`).
* **Resource Hardening**: CGroup v2 boundaries enforcing `MemoryMax=64M` and `CPUQuota=20%`.
* **Log Rotation**: Automated `copytruncate` policy retaining 7 compressed daily archives via `logrotate`.
* **Containerization**: Multi-stage lightweight OCI container with enforced Docker Compose resource limits.
* **CI/CD**: GitHub Actions pipeline checking syntax, validating configurations, and verifying Docker builds on every commit.

## Repository Layout
```text
├── .github/workflows/ci.yml    # GitHub Actions Continuous Integration pipeline
├── config/logrotate.datalens   # Zero-downtime log rotation & gzip policy
├── docker/
│   └── Dockerfile              # Production Python 3.12 container specification
├── docker-compose.yml          # Container orchestration with CPU/Memory limits
├── scripts/
│   ├── heartbeat_worker.py     # Worker daemon + Prometheus metrics exporter
│   ├── memory_allocator_test.py# CGroup OOM chaos test harness
│   └── storage_monitor.sh      # Block storage & inode health auditor
└── systemd/datalens.service    # Hardened systemd service definition
# Check service status & resource consumption
systemctl status datalens
curl -s [http://127.0.0.1:9100/metrics](http://127.0.0.1:9100/metrics)

# Run forensic storage & inode check
./scripts/storage_monitor.sh

# Force log rotation drill
sudo logrotate -f -v /etc/logrotate.d/datalens
