#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    email = parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    url = request.Request(sys.argv[1], email)
    with request.urlopen(url) as response:
        html = response.read()
    print(content.decode())
