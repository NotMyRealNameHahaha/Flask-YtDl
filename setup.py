#!/usr/bin/env python3
import os
import json
import subprocess


def setup():
    with open("config.JSON", "r+") as YTR_config:
        my_config = json.load(YTR_config)
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
        my_config['first_run'] = "false"
    YTR_config.close()
setup()
