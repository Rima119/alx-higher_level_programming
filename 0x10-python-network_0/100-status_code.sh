#!/bin/bash
# sends a request to a URL passed, displays only the status code of the respons
curl -s -o /dev/null -w '%{http_code}' "$1"
