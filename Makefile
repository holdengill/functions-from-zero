install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		pip install --upgrade fire

test:
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C hello.py


all: install lint test