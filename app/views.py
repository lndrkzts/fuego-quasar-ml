from flask import Blueprint
from flask import request

from .constants import VALID_SATELLITES_NAMES
from .responses import success, bad_request, not_found
from .services import get_message, get_location
from .utils import get_messages_and_satellites, update_satellites_split_json, load_satellites_split_json
from .validators import validate_topsecret_json, validate_topsecret_split_json


api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@api_v1.route('/topsecret', methods=['POST'])
def topsecret():
    req_json = request.get_json(force=True)

    if not validate_topsecret_json(req_json):
        return bad_request('Invalid JSON')

    messages, satellites = get_messages_and_satellites(req_json)
    message = get_message(messages)
    location = get_location(satellites)

    if message is None or location is None:
        return not_found('Message or position cannot be determined')
    
    return success(
        {
            'position': location,
            'message': message
        }
    )


@api_v1.route('/topsecret_split/<name>', methods=['POST'])
def topsecret_split_post(name):
    req_json = request.get_json(force=True)

    if name not in VALID_SATELLITES_NAMES:
        return bad_request('Invalid name')

    if not validate_topsecret_split_json(req_json):
        return bad_request('Invalid JSON')

    update_satellites_split_json(name, req_json)

    return success(
        { 
            'distance': req_json['distance'],
            'message': req_json['message']
        }
    )


@api_v1.route('/topsecret_split', methods=['GET'])
def topsecret_split_get():
    json_satellites = load_satellites_split_json()

    if not validate_topsecret_json(json_satellites):
        return bad_request('Information is missing')

    messages, satellites = get_messages_and_satellites(json_satellites)
    message = get_message(messages)
    location = get_location(satellites)

    if message is None or location is None:
        return not_found('Message or position cannot be determined')

    return success(
        { 
            'distance': location,
            'message': message
        }
    )