#!/usr/bin/python3
"""By me
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    argument = load_from_json_file('add_item.json')
except Exception:
    argument = []

for i in range(1, len(sys.argv)):
    argument.append(sys.argv[i])

save_to_json_file(argument, 'add_item.json')
