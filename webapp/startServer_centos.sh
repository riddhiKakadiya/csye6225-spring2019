#!/bin/bash
sudo chown centos /home/centos/webapp/* && scl enable rh-python36 bash && rm -rf /home/centos/webapp/WebProject/djangoEnv/ && virtualenv -p python3 /home/centos/webapp/WebProject/djangoEnv && source /home/centos/webapp/WebProject/djangoEnv/bin/activate && pip install -r /home/centos/webapp/WebProject/requirements.txt &&python /home/centos/webapp/WebProject/manage.py runserver 0.0.0.0:8000 --settings=WebProject.settings_test