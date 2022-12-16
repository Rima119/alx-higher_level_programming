#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        obj = req.json()
        if not obj:
            print('No result')
        else:
            print("[{}] {}".format(obj['id'], obj['name']))
    except ValueError:
        print("Not a valid JSON")
