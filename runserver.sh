#!/usr/bin/env bash
#export VIRTUALENV_PYTHON=mypy/python3.5
sudo pip install virtualenv
virtualenv mypy/venv/venv --python=python3.5


source mypy/venv/venv/bin/activate
mypy/venv/venv/bin/pip install -r requirements.txt
mypy/venv/venv/bin/python3.5 runserver.py