#!/usr/bin/env python3
import os
import sys
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from datetime import datetime, timezone

LOG_DIR = "/var/log/datalens"
LOG_FILE = os.path.join(LOG_DIR, "app.log")
METRICS_PORT = 9100

heartbeat_seq = 0
start_time = time.time()

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.end_headers()
            uptime = time.time() - start_time
            metrics = (
                f"# HELP datalens_heartbeats_total Total heartbeat iterations generated.\n"
                f"# TYPE datalens_heartbeats_total counter\n"
                f"datalens_heartbeats_total {heartbeat_seq}\n"
                f"# HELP datalens_uptime_seconds Process uptime in seconds.\n"
                f"# TYPE datalens_uptime_seconds gauge\n"
                f"datalens_uptime_seconds {uptime:.2f}\n"
            )
            self.wfile.write(metrics.encode("utf-8"))
        elif self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"healthy","service":"datalens"}')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return  # Suppress internal HTTP request noise

def run_metrics_server():
    server = HTTPServer(("0.0.0.0", METRICS_PORT), MetricsHandler)
    server.serve_forever()

def main():
    global heartbeat_seq
    pid = os.getpid()
    print(f"[*] Starting DataLens Worker (PID {pid}) | Exposing /metrics on port {METRICS_PORT}", flush=True)

    metrics_thread = threading.Thread(target=run_metrics_server, daemon=True)
    metrics_thread.start()

    while True:
        heartbeat_seq += 1
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{now} UTC] [HEARTBEAT] #{heartbeat_seq} - Status: HEALTHY (PID: {pid})\n"
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_line)
            f.flush()
        time.sleep(2)

if __name__ == "__main__":
    main()
