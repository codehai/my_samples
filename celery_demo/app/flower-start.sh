#! /usr/bin/env bash
set -e

celery -A app.worker --broker=amqp://guest:guest@queue:5672// flower