# Barren Land Analysis

## Assumptions
You have [Docker](https://store.docker.com/search?type=edition&offering=community) installed.

## Usage
### Default
```
make run
```

### Custom
```
make build
docker run -it --rm barren-land-analysis:latest '{"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}'
```

## Running Tests
Tests will be run automatically during a `make build`, but if you want to run the tests independently, or if you want more detailed coverage reports, you can do so by running `make check`. However, running `make check` requires that you are able to run the tests on your localhost directly, which implies that you have installed the `requirements.pip` dependencies in some local python environment (I'd recommend using a [virtualenv](https://virtualenv.pypa.io/en/stable/)).

### Viewing Coverage Reports
```
make check
make host-coverage
```
Now, navigate to [localhost:8000](localhost:8000) and you'll see some shiny code coverage reports!

### Static Analysis
If you're really into static analysis, and you want to see more info about this codebase, run `make static-analysis` to see the results of some [pylint](https://www.pylint.org) and [radon](https://radon.readthedocs.io/en/latest/) analysis.

## Why Python?
While I have a strong preference for static types in projects of team_size > 1, I found that Python was a pleasant choice for this particular problem if only for the shallow reason that list literals make creating/viewing matrices slightly easier in Python than in Java.
