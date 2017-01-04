from YTR import app
# Python imports
import subprocess
import json


def open_browser():
    # open config.JSON as r+
    config = open("config.JSON", "r+")
    my_config = json.load(config)
    if my_config['OS'] == 'Linux':
        subprocess.run("sensible-browser 127.0.0.1:5100", shell=True)
    elif my_config['OS'] == 'OSX':
        subprocess.run("open 127.0.0.1:5100", shell=True)

# open_browser()
if __name__ == '__main__':
    app.run(debug=True, port=5100)
