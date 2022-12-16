#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    req = requests.get(url, auth=requests.auth.HTTPBasicAuth(argv[1], argv[2]))
    obj = req.json()
    if obj == {}:
        print("None")
    else:
        print(req.json().get('id'))
