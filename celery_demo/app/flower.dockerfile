FROM mher/flower

WORKDIR /app/

ENV C_FORCE_ROOT=1

COPY ./app /app
WORKDIR /app

RUN pip install -r requirments.txt

ENV PYTHONPATH=/app

COPY ./flower-start.sh /flower-start.sh
#RUN chmod +x /flower-start.sh

WORKDIR /

EXPOSE 5555

CMD ["sh", "./flower-start.sh"]
