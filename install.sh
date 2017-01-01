#!/usr/bin/env bash
sudo pip install virtualenv
# Create virtualenv with python3.5 as version
virtualenv -p $(which python3.5) venv
# activate venv
source venv/bin/activate
sudo pip install -r requirements.txt
