FROM python:3.6.5-alpine3.6

# separate requirements COPY from sources COPY for caching purposes
COPY requirements.pip .
RUN pip install -r requirements.pip

COPY test_analysis.py analysis.py ./
# we run the tests during the build so that builds that don't pass the tests fail
RUN python analysis.py -t -v && pytest test_analysis.py

ENTRYPOINT ["python", "analysis.py"]
