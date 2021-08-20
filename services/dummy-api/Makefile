SERVICE := dummy-api
PKG := dummy_api

setup:
	pip install --editable .[run,test]

build:
	docker build --tag phra/$(SERVICE) .

test-unit:
	python -m unittest discover

run:
	cd $(PKG)/ && uvicorn main:app --reload

run-docker:
	docker run --rm --publish 2500:80 --name phra-$(SERVICE) phra/$(SERVICE)

format:
	black .
	isort .

check-format:
	black --check .
	isort --check .
