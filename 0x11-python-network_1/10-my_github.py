#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    auth1 = HTTPBasicAuth(username=argv[1], password=argv[2])
    req = requests.get(url, auth=auth1)
    obj = req.json()
    print(obj.get('id'))
