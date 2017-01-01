from YTR import app
# Python imports
import os
import subprocess
import json
import sys


# Run this from bash script
def open_browser():
    # open config.JSON as r+
    config = open("config.JSON", "r+")
    my_config = json.load(config)
    if my_config['OS'] == 'Linux':
        subprocess.run("sensible-browser 127.0.0.1:1234", shell=True)
    elif my_config['OS'] == 'OSX':
        subprocess.run("open 127.0.0.0:1234", shell=True)
    # else:
    #     subprocess.run("xdg-open 127.0.0.1:5000", shell=True)


if __name__ == '__main__':
    open_browser()
    app.run(debug=True, port=1234)
