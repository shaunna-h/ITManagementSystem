import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itmanagementsystem.settings')

# Create the WSGI application object that the server will use.
application = get_wsgi_application()