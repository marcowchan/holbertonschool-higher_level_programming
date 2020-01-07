#!/bin/bash
# Displays the size of the body of the response.
curl -sI "$1" | sed -ne 's/Content-Length: //p'
