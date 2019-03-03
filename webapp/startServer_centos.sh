#!/bin/bash
cd WebProject
sudo scl enable rh-python36 bash
sudo rm -rf djangoEnv
virtualenv -p python djangoEnv
source djangoEnv/bin/activate
cat requirements.txt | xargs -n 1 pip install
python manage.py runserver 0.0.0.0:80