test:
	pytest

style:
	pycodestyle *.py

check: test style
