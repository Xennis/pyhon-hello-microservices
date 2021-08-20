import multiprocessing
import os

cores = multiprocessing.cpu_count()

# Gunicorn settings variables
# https://docs.gunicorn.org/en/stable/settings.html
bind = "0.0.0.0:80"
graceful_timeout = 120
keepalive = 5
loglevel = os.getenv("LOG_LEVEL", "info")
timeout = 120
worker_tmp_dir = "/dev/shm"
workers = max(cores, 2)
