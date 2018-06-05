test:
	python analysis.py -v
	pytest --cov-report html \
		   --cov-report term \
		   --cov-branch \
		   --cov .

style:
	pycodestyle *.py

check: test style
