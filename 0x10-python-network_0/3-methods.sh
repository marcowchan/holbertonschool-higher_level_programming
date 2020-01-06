#!/bin/bash
# Displays allowed HTTP methods.
curl -sIX OPTIONS $1 | sed -ne 's/Allow: //p'
