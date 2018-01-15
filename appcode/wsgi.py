import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append("/var/www/appcode/djangoapp/appcode")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appcode.settings")

application = get_wsgi_application()
