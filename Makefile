doctest:
	python analysis.py -t -v

test:
	pytest --cov-report html \
		   --cov-report term \
		   --cov-branch \
		   --cov .

style:
	pycodestyle *.py

check: doctest test style loc

loc:
	@echo "LOC analysis.py: `cat analysis.py | wc -l`"
	@echo "LOC test_analysis.py: `cat test_analysis.py | wc -l`"

lint:
	pylint analysis.py

uber-check: check loc lint

host-coverage:
	cd htmlcov && python -m http.server

build:
	docker build -t barren-land-analysis:latest .

run: build
	docker run -it --rm barren-land-analysis:latest '{"0 292 399 307"}'
