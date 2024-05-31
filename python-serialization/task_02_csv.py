#!/usr/bin/python3
"""Made by Jorge Beritan
"""


import csv
import json


def convert_csv_to_json(filename):
    """Convert csv to json
    """
    try:
        with open(filename, "r") as archive:
            csv_reader = csv.DictReader(archive)
            data = [row for row in csv_reader]
    
        with open(filename, "w") as archive_json:
            json.dumps(data, archive_json)
        return True
    except FileNotFoundError:
        return False
