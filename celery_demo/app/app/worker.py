import os
import time

from celery import Celery
from datetime import timedelta, datetime

app = Celery("worker", broker="amqp://guest@queue//")
app.conf.task_routes = {"app.worker.add": "main-queue"}
app.conf.beat_schedule = {
    "failure_alert_task": {
        "task": "app.worker.add",
        "schedule": timedelta(seconds=30),
        'args': (16, 16)
    }
}

@app.task
def add(x, y):
    print(f"[{datetime.now().isoformat()}]Receive add task {x} {y}.")
    return x + y

if __name__ == '__main__':
    add(1, 1)
