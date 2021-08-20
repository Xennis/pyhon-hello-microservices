FROM python:3.9-alpine3.14

RUN apk add --no-cache --virtual .build-deps gcc make libc-dev \
    && pip install --no-cache-dir fastapi gunicorn "uvicorn[standard]" \
    && apk del .build-deps gcc libc-dev make

COPY ./gunicorn_conf.py /gunicorn_conf.py

WORKDIR /app/
ENV PYTHONPATH=/app

EXPOSE 80
CMD ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "--config", "/gunicorn_conf.py", "main:app"]
