# Template for a python repository

## Installation

Use a virtual environment, with `python3`:

``` bash
virtualenv venv -p python3;
source venv/bin/activate;

pip install -r requirements.txt  # install existing librairaries
pip install requests;  # install new librairies
pip freeze > requirements.txt  # export the new librairies
```

## Code

Add your code in [./package](./package) (and rename the package).

## Unit tests

Use [pytest](https://docs.pytest.org/en/latest/) for unit testing.

Run your tests with `pytest tests`.

## Docs

Use [sphinx](http://www.sphinx-doc.org/en/master/) for generating the docs
from your code.

Use [Napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/)
style when writing your docstrings.

``` bash
sphinx-apidoc ./package -o ./docs/source -M;
cd docs;
make clean;
make html;
open docs/build/html/index.html;
```
