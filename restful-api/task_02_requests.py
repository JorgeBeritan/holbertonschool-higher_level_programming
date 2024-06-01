#!/usr/bin/python3
"""Made by Jorge Beritan
"""


import requests
import csv

def fetch_and_print_posts():
    """In this function we get a url and print title
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(i["title"])

def fetch_and_save_posts():
    """In this function we put the all information for the api on archive.csv"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        with open("posts.csv", "w", encoding="utf-8") as archive:
            writer = csv.DictWriter(archive, fieldnames = ["id", "title", "body"])
            writer.writeheader
            for i in data:
                writer.writerow({"id": i["id"], "title": i["title"], "body": i["body"]})
