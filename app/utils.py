import json

from . import constants


def get_satellites_dict():
    return {
        'kenobi': constants.KENOBI.copy(),
        'skywalker': constants.SKYWALKER.copy(),
        'sato': constants.SATO.copy(),
    }


def get_messages_and_satellites(json):
    messages = []
    satellites = get_satellites_dict()

    for s in json.get('satellites'):
        messages.append(s['message'])
        satellites[s['name']]['r'] = s['distance']

    return messages, satellites


def save_satellites_split_json(data):
    with open('satellites_split.json', 'w+') as file:
        json.dump(data, file, indent=4)


def load_satellites_split_json():
    with open('satellites_split.json') as file: 
        data = json.load(file) 
    return data


def update_satellites_split_json(name, data):
    json_file = load_satellites_split_json()

    for s in json_file['satellites']:
        if s['name'] == name:
            s['distance'] = data['distance']
            s['message'] = data['message']
            break

    save_satellites_split_json(json_file)