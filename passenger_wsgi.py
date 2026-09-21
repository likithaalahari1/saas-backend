import sys, os

# Virtual environment Python executable for cPanel Phusion Passenger
INTERP = "/home/xpsvyema/virtualenv/andhrayatri.in/3.10/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socially_backend.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
