#!/usr/bin/python3
import sys

with open("prueba.txt", "w", encoding="utf-8") as archive:
    for i in sys.argv[1:]:
        archive.write(str(sys.argv))