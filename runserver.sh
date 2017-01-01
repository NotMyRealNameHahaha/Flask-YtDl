#!/usr/bin/env bash
python3.5 setup.py

activate() {
    source venv/bin/activate
#    pip install -r requirements.txt
    export FLASK_APP=runserver.py
    flask run
}
activate
