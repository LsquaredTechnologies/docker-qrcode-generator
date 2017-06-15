from flask import Blueprint, jsonify

health = Blueprint('health', __name__)

@health.route('/health', methods = ['GET'])
def get_health():
    status_code = 200
    success = True
    response = {'success': success}
    return jsonify(response), status_code
