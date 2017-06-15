from flask import Blueprint

ping = Blueprint('ping', __name__)

@ping.route('/ping', methods = ['GET'])
def get_ping():
    status_code = 200
    return 'pong', status_code
