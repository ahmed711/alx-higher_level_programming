#!/bin/bash
#get content length of api rest calls
curl -sLw "%{http_code}" -o /dev/null "$1"
