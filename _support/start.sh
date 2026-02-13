#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

source /home/pi/.virtualenv/python_notebooks/bin/activate
jupyter lab --config ${SCRIPTPATH}/jupyter_notebook_config.py
