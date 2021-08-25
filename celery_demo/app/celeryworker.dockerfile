FROM python:3.7

WORKDIR /app/

ENV C_FORCE_ROOT=1

COPY ./app /app
WORKDIR /app

RUN pip install -r requirments.txt

ENV PYTHONPATH=/app

COPY ./worker-start.sh /worker-start.sh
RUN chmod +x /worker-start.sh

WORKDIR /

CMD ["bash", "./worker-start.sh"]
