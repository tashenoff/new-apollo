#!/bin/bash
source /home/apollo-admin/apollo-site/apollo-venv/bin/activate
exec gunicorn  -c "home/apollo-admin/apollo-site/new-apollo/config/gunicorn_config.py" acrm.wsgi

