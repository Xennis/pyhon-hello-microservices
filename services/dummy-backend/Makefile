SERVICE := dummy-backend
PKG := dummy_backend
PORT:= 2501

setup:
	pip install --editable .[run,test]

build:
	docker build --tag phra/$(SERVICE) .

test-unit:
	python -m unittest discover

run:
	cd $(PKG)/ && uvicorn main:app --reload --port $(PORT)

run-docker:
	docker run --rm --publish $(PORT):80 --name phra-$(SERVICE) phra/$(SERVICE)

format:
	black .
	isort .

check-format:
	black --check .
	isort --check .
