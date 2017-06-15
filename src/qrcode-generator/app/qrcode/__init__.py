from flask import Flask, Blueprint, request, send_file
from flask_qrcode import QRcode

qrcode = Blueprint('qrcode', __name__)

generate_qrcode = QRcode()

@qrcode.route('/qrcode/<data>', methods=['GET'])
def get_qrcode(data):
    return send_file(generate_qrcode(data, error_correction='H', mode='raw'), mimetype='image/png')
