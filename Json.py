import json
from datetime import date, time


def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, time):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, bytes):
        return str(obj)[2:-1]

    return obj.__dict__


def pprint(obj):
    print(json.dumps(obj, default=serialize, indent=4))
