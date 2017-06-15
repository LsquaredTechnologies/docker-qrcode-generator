from flask import Flask

def _initialize_blueprints(application):
    '''
    Register Flask blueprints
    '''
    from app.health import health
    application.register_blueprint(health, url_prefix='/conf')
    from app.ping import ping
    application.register_blueprint(ping, url_prefix='/conf')
    from app.qrcode import qrcode
    application.register_blueprint(qrcode, url_prefix='/api/v1')

def create_app():
    '''
    Create an app by initializing components.
    '''
    application = Flask(__name__)
    _initialize_blueprints(application)
    return application
