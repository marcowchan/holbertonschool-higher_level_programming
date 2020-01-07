#!/bin/bash
# Sets params for a POST request.
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
