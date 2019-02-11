#!/bin/bash
echo "this app needs to be run in virtual python environment with flask module..."
echo "run on all IP address need to --host=\"0.0.0.0\""
export FLASK_APP="get24"
flask run 

