IMAGE := phra/uvicorn-gunicorn-fastapi

build:
	docker build --tag $(IMAGE):python3.9-alpine3.14 .

format:
	black .
	isort .

check-format:
	black --check .
	isort --check .
