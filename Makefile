doctest:
	python analysis.py -t -v

test:
	pytest --cov-report html \
		   --cov-report term \
		   --cov-branch \
		   --cov .

style:
	pycodestyle *.py

check: doctest test style

host-coverage:
	cd htmlcov && python -m http.server

lint:
	-pylint analysis.py

radon:
	radon raw analysis.py
	radon cc analysis.py
	radon mi analysis.py

static-analysis: lint radon

build:
	docker build -t barren-land-analysis:latest .

run: build
	docker run -it --rm barren-land-analysis:latest '{"0 292 399 307"}'
