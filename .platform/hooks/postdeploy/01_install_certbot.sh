#!/bin/bash

sudo python3.11 -m venv /opt/certbot/
sudo /opt/certbot/bin/pip install --upgrade pip

sudo /opt/certbot/bin/pip install certbot certbot-nginx

sudo ln -sf /opt/certbot/bin/certbot /usr/bin/certbot