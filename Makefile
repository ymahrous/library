run:
	python3 -m app.main

test:
	pytest --tb=short

coverage:
	coverage run -m pytest --tb=short && coverage report -m && coverage html

format:
	black app/*.py

lint:
	pylint --disable=R,C,W1203,E1101,redefined-outer-name app/*.py

install:
	pip3 install --upgrade pip && pip3 install -r requirements.txt

clean:
	rm -rf __pycache__ */__pycache__ htmlcov .pytest_cache .coverage instance/*.db .DS_Store

all: install format lint coverage test clean

docker-build:
	docker-compose build

docker-run:
	docker-compose up

docker-test:
	docker-compose run --rm web pytest --disable-warnings --tb=short