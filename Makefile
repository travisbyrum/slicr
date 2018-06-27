MAKEFLAGS += --silent
DOCKER := $(shell which docker)
PIPENV := $(shell which pipenv)
PIP := $(shell which pip)
COVR := $(PIPENV) run coverage
LINT := $(PIPENV) run pylint
PYTHON := $(PIPENV) run python

PKG := slicr
API_PORT ?= 5000

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

.PHONY: install-dev

install:
	$(PIPENV) install --deploy --system
	$(PIP) install .

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
	$(PIPENV) uninstall --all

.PHONY: uninstall