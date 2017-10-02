#!/bin/bash

# ############# CONFIGURE THIS APP FOR PYTHONANYWHERE ##############################################
#
#  On https://www.pythonanywhere.com/user/yourname/webapps/
#  create a new web app and choose `flask` and then choose Python3.6
#
#  specify /home/YOURUSER/repo/cms/wsgi.py as the application file
#
#  Go to your console and access your home `cd ~`
#
#  delete the existing `repo` with `rm -rf repo` 
#  
#  Clone the new repo
#  git clone -b cms_9_deploy https://github.com/cursodepythonoficial/flask_tutorial_pybr13.git repo
#
#  cd repo
#
#  ./deploy.sh
#
#  wait....
#
#  Go back to web dashbord https://www.pythonanywhere.com/user/yourname/webapps/
# 
#  Configure sourcecode to /home/YOURUSER/repo/cms
#  Configure workdir to /home/YOURUSER/repo
#  DO NOT TOUCH THE WSGI config file field
# 
#  Configure virtualenv to /home/YOURUSER/repo/venv
#
#  Reload the web app
#
#  Access the YOURNAME.pythonanywhere.com and see your cms running
#  try the /admin with `admin` `admin` credentials
#  Or change in last step of this file
# ##################################################################################################

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
