.PHONY: clean

PROJECT = salt
PORT = 8080

ENV ?= env
VENV = $(shell echo $(VIRTUAL_ENV))

ifneq ($(VENV),)
	NOSETESTS = nosetests
	PEP8 = pep8
	PIP = pip
	PYLINT = pylint
	PYTHON = python
else
	NOSETESTS = $(ENV)/bin/nosetests
	PEP8 = $(ENV)/bin/pep8
	PIP = $(ENV)/bin/pip
	PYLINT = $(ENV)/bin/pylint
	PYTHON = $(ENV)/bin/python
endif


clean:
	find . -name '*.pyc' -delete

run:
	$(PYTHON) manage.py runserver 0.0.0.0:$(PORT)