# Python imports
import os
import subprocess
import json
import sys

# open config.JSON as r+
config = open("config.JSON", "r+")
my_config = json.load(config)


def setup():
    if my_config['first_run'] == 'true':
        # Declare path to bash script
        run_me = os.path.join(".", "install.sh")
        if my_config['OS'] == 'Linux':
            # Run install.sh
            subprocess.run(["bash", run_me], shell=True)
        else:
            subprocess.run(["source", run_me], shell=True)
    else:
        pass


# Run this from bash script
def open_browser():
    if my_config['OS'] == 'Linux':
        subprocess.run("sensible-browser 127.0.0.1:5000", shell=True)
    elif my_config['OS'] == 'OSX':
        subprocess.run("open 127.0.0.0:5000", shell=True)
    else:
        subprocess.run("xdg-open 127.0.0.1:5000", shell=True)


def mytest():
    py_location = subprocess.Popen("which python3.5", shell=True)
    print(py_location.stdout.read())








