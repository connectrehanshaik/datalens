FROM python:3.12-slim
WORKDIR /app
RUN mkdir -p /var/log/datalens
COPY scripts/heartbeat_worker.py /app/worker.py
EXPOSE 9100
CMD ["python3", "-u", "/app/worker.py"]
