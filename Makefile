.PHONY: clean pep8 test install

clean: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

pep8: ## check style with flake8
	flake8 cms tests

test: pep8 ## run tests quickly with the default Python
	py.test -v

install: clean test ## install the package to the active Python's site-packages
	python setup.py develop
