# Python imports
import os
import subprocess
import json


# open config.JSON as r+
config = open("config.JSON", "r+")
my_config = json.load(config)


def setup():
    if my_config['first_run'] == 'true':
        print(my_config['first_run'])
        subprocess.run("sudo pip install virtualenv")





