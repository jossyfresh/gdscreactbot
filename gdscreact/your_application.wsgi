# your_application.wsgi

import os
from your_application import create_app  # Import the application object from your actual application

# Set the 'application' variable to the WSGI application
application = create_app()

# Optionally, you can configure Gunicorn settings here
# For example, setting the number of workers:
# workers = 4

# If you're using a virtual environment, you might need to activate it here
# activate_this = '/path/to/your/virtualenv/bin/activate_this.py'
# exec(open(activate_this).read(), dict(__file__=activate_this))

if __name__ == "__main__":
    # This block is executed if the script is run directly (not imported)
    # It's useful for local development
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)
