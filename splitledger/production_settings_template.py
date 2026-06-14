"""
Production settings for PythonAnywhere deployment.

INSTRUCTIONS:
1. Copy this file to production_settings.py
2. Replace all USERNAME placeholders with your PythonAnywhere username
3. Update SECRET_KEY in WSGI file (not here for security)
4. Update DB_PASSWORD in WSGI file (not here for security)
"""

from .settings import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
# Set this in your WSGI file as environment variable!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-wsgi-file')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update with your PythonAnywhere username
ALLOWED_HOSTS = ['USERNAME.pythonanywhere.com']

# Database
# Update USERNAME with your PythonAnywhere username
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'USERNAME$splitledger',
        'USER': 'USERNAME',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'USERNAME.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'CONN_MAX_AGE': 600,
    }
}

# Static files (CSS, JavaScript, Images)
# Update USERNAME with your PythonAnywhere username
STATIC_URL = '/static/'
STATIC_ROOT = '/home/USERNAME/expense-analyzer/staticfiles'

# Media files (CSV uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/USERNAME/expense-analyzer/media'

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings (uncomment when you have SSL)
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/USERNAME/expense-analyzer/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
