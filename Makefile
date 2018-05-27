MAKEFLAGS += --silent
COVR := $(shell which coverage)
LINT := $(shell which pylint)
PIPENV := $(shell which pipenv)
PYTHON := $(PIPENV) run python
API_PORT ?= 5000

PKG := slicr

all: clean clean-pyc install

.PHONY: all

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: clean-pyc

clean:
	rm -rf build dist *.egg-info

.PHONY: clean

coverage:
	$(COVR) run setup.py test
	$(COVR) report

.PHONY: coverage

install-dev:
	$(PIPENV) install --dev
	$(PIPENV) install --dev -e .

.PHONY: install-dev

install:
	$(PIPENV) install
	$(PIPENV) install .

.PHONY: install

lint:
	$(LINT) $(PKG) -rn

.PHONY: lint

run:
	$(PYTHON) bin/main.py -p $(API_PORT)

.PHONY: run

test:
	$(PYTHON) setup.py test

.PHONY: test

uninstall:
	$(PIPENV) uninstall