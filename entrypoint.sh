#!/bin/bash
cd /app
pip install -r /app/requirements.txt
/app/manage.py runserver 0.0.0.0:8000
