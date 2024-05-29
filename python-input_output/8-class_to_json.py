#!/usr/bin/python3
"""By me
"""

import json


def class_to_json(obj):
    """In this function we learn how return description dictionary for JSON serialization
    """
    instancia = json.dumps(obj.__dict__)
    return json.loads(instancia)
