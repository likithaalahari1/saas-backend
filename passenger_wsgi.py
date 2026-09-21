    import sys, os

    # Add application directory to Python path for cPanel Phusion Passenger
    sys.path.insert(0, os.path.dirname(__file__))

    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socially_backend.settings')

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
