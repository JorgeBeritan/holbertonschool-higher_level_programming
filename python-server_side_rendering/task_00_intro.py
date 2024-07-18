#!/usr/bin/python3


def generate_invitations(template, attendees):
    if isinstance(template, str):
        raise TypeError("template must be a string")
    elif all(isinstance(item, dict) for item in attendees):
        raise TypeError("attendes must be a list of dictionaries")
    elif not template and attendees:
        raise ValueError("Template or attendes is required")

    for index, replacements in enumerate(attendees):
        file_open = template
        for key, value in replacements.items():
            file_open = file_open.replace(f"{{{key}}}", str(value))

        output = f"output_{index + 1}.txt"
        with open(output, "w") as file:
            file.write(file_open)
