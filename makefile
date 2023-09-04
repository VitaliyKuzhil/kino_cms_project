# Makefile for kino_cms

# variables
PROJECT_NAME = kino_cms
PYTHON = python
PIP = pip
MANAGE = $(PYTHON) manage.py
DB_NAME = kino_cms_db

# my targets

# runserver for kino_cms project
runserver:
	$(MANAGE) runserver

# make_migrations for kino_cms project
migrations:
	$(MANAGE) makemigrations

# execute migration for kino_cms project
migrate:
	$(MANAGE) migrate

# create superuser
superuser:
	$(MANAGE) createsuperuser

# reset database
#resetdb:
#	- dropdb $(PROJECT_NAME)
#	- createdb $(PROJECT_NAME)
#	$(MANAGE) migrate

# copy database
backup:
	$(MANAGE) dumpdata > backup.json

# restore database with backup
restore:
	$(MANAGE) loaddata backup.json

# install requirements
install:
	$(PIP) install -r requirements.txt

# run tests
test:
	$(MANAGE) test

# create virtual environment
venv:
	python -m venv venv

# activate virtual environment
activate:
	source venv/bin/activate

# deactivation virtual environment
deactivate:
	deactivate

# run clean code
lint:
	pylint $(app_name)
	flake8 $(app_name)

# deploy project
deploy:
	# command to deploy

# clean cache files
clean:
	rm -rf __pycache__ *.pyc .coverage htmlcov

