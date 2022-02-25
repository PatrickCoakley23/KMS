#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/staging
from django.contrib.auth.models import User; User.objects.create_superuser( "patrick","patrickcoakley23@outlook.com", "020408")