from .constants import VALID_SATELLITES_NAMES

def validate_topsecret_json(json):
    topsecret_json = json.get("satellites")

    if topsecret_json is None:
        return False

    if len(topsecret_json) is not 3:
        return False

    len_messages = 0

    for satellite in topsecret_json:
        if satellite.get("name") is None:
            return False

        if satellite.get("name") not in VALID_SATELLITES_NAMES:
            return False

        if satellite.get("distance") is None:
            return False

        if satellite.get("message") is None:
            return False

    return True


def validate_topsecret_split_json(json):
    if json.get("distance") is None:
        return False

    if json.get("message") is None:
        return False

    return True