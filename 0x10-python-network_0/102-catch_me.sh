#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL -H "X-School-User-Id: 98" -X PUT 0.0.0.0:5000/catch_me
