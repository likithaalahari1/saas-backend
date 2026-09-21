import sys, os

# Add application directory to path
sys.path.append(os.getcwd())

from socially_backend.wsgi import application
