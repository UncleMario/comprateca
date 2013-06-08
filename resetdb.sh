#!/bin/sh

sudo -u postgres dropdb comprateca
sudo -u postgres createdb comprateca
python manage.py syncdb --settings comprateca.localsettings
python manage.py runserver --settings comprateca.localsettings
