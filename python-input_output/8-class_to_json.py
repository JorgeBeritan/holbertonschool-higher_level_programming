#!/usr/bin/python3
"""By me
"""


def class_to_json(obj):
    """In this function we learn how return description dictionary for JSON serialization
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        json_dict[key] = value
    return json_dict
