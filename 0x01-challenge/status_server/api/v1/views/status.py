#!/usr/bin/python3
from flask import Blueprint, jsonify

status_bp = Blueprint('status_bp', name, url_prefix='/api/v1')

@status_bp.route('/status', methods=['GET'])
def get_status():
        return jsonify({'status': 'OK'})i
