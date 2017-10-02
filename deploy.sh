#!/bin/bash

# CONFIGURE THIS APP FOR PYTHONANYWHERE


# Create virtualenv
virtualenv -p python3.6 venv;


# activate it
. venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# ensure it is ok
python3.6 setup.py develop 

# add admin user
cms adduser --username admin --password admin 
