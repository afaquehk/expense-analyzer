"""
WSGI configuration for PythonAnywhere deployment.

INSTRUCTIONS:
1. Copy the content of this file
2. Paste it into your WSGI configuration file on PythonAnywhere
3. Replace USERNAME with your actual PythonAnywhere username
4. Replace YOUR_MYSQL_PASSWORD with your MySQL password
5. Generate a new SECRET_KEY (see below)

TO GENERATE SECRET KEY:
Run this in Python console:
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())

Copy the output and paste as SECRET_KEY below.
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# REPLACE USERNAME WITH YOUR PYTHONANYWHERE USERNAME
# ═══════════════════════════════════════════════════════════

# Add your project directory to the sys.path
path = '/home/USERNAME/expense-analyzer'
if path not in sys.path:
    sys.path.insert(0, path)

# ═══════════════════════════════════════════════════════════
# SET ENVIRONMENT VARIABLES - UPDATE THESE!
# ═══════════════════════════════════════════════════════════

os.environ['DJANGO_SETTINGS_MODULE'] = 'splitledger.production_settings'

# Replace with your actual MySQL password
os.environ['DB_PASSWORD'] = 'YOUR_MYSQL_PASSWORD'

# Replace with a newly generated secret key
# Generate one: https://djecrety.ir/ or use Django's get_random_secret_key()
os.environ['SECRET_KEY'] = 'your-super-secret-key-replace-this-with-real-one'

# ═══════════════════════════════════════════════════════════
# DJANGO WSGI APPLICATION - DON'T CHANGE BELOW
# ═══════════════════════════════════════════════════════════

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
