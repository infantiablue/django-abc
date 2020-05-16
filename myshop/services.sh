#!/bin/zsh
# My first script
sudo service rabbitmq-server start
celery -A myshop worker -l info

