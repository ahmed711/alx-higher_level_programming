#!/bin/bash
#get content length of api rest calls
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
