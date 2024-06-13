import os
import sys
import traceback
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eatog.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    # Log the exception traceback
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'type': exc_type.__name__,
        'message': str(exc_value),
        'traceback': traceback.format_tb(exc_traceback)
    }
    print("Exception in WSGI application:", traceback_details)
    raise e
