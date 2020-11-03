from flask import jsonify


def success(data):
    return jsonify(data), 200  

def bad_request(info):
    return jsonify(
        {
            'message': 'Bad request',
            'info': info,
        }
    ), 400

def not_found(info):
    return jsonify(
        {
            'message': 'Resource not found',
            'info': info,
        }
    ), 404
