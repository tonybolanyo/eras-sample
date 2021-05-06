#!/bin/sh

cwd=$(pwd)

cd /app/src

coverage run --source='.' --rcfile=.coveragerc manage.py test --failfast --settings=roomusu.settings.test
coverage html -d htmlcov
coverage report -m

cd $cwd