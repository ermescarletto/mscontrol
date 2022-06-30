"""
WSGI config for ms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/opt/bitnami/projects/mscontrol/ms/')
os.environ.setdefault('PYTHON_EGG_CACHE', '/opt/bitnami/projects/mscontrol/ms/egg_cache')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ms.settings')
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
