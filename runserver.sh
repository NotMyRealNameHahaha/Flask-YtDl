#!/usr/bin/env bash
python setup.py
export FLASK_APP=runserver.py
flask run
