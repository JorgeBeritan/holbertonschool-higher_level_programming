#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    if not template:
       return "Template is empty, no output files generated"
    if not attendees:
        return "No data provided, no output files generated"

    if isinstance(template, str):
        return "Template is empty, no output files generated"
    elif all(isinstance(item, dict) for item in attendees):
        return "No data provide, no output files generated"
    

    for index, replacements in enumerate(attendees):
        file_open = template
        for key, value in replacements.items():
            file_open = file_open.replace(f"{{{key}}}", str(value) or "N/A")

        output = f"output_{index + 1}.txt"
        with open("output_" + str(index + 1) + ".txt", "w") as file:
            file.write(file_open)
