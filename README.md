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
Now, navigate to [localhost:8000](http://localhost:8000) and you'll see some shiny code coverage reports!

### Static Analysis
If you're really in to static analysis, and you want to see more info about this codebase, run `make static-analysis` to see the results of some [pylint](https://www.pylint.org) and [radon](https://radon.readthedocs.io/en/latest/) analysis.

## Why Python?
While I have a strong preference for static types in projects of team_size > 1, I found that Python was a pleasant choice for this particular problem if only for the shallow reason that list literals make creating/viewing matrices slightly easier in Python than in Java.

## Noteworthy Decisions
Initially, I had settled on a recursive solution, but that caused some nasty stack overflows when dealing with larger matrices. As such, I had to translate that recursive solution into an iterative one where I held my own little stack of coordinates to explore in memory instead of relying on the call stack to store that for me. I still think the recursive solution is far more "natural", but this is a good reminder of the great wisdom of [SICP](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html#_toc_start) that iteration is just a special case of recursion :)

## Areas for Improvement
In a word: performance. I'm unsatisfied with the performance of this solution on the larger examples, and that warrants more benchmarking and investigation to really discover the root cause. It might also be fun and beneficial to explore the use of [numpy](http://www.numpy.org) for a "free" performance boost.
