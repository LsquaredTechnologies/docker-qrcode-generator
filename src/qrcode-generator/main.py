#!/usr/bin/env python
import os
from app import create_app

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 8000

    application = create_app()
    application.run(HOST, PORT, debug=True)
