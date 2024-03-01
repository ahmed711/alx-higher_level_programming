#!/bin/bash
#get content length of api rest calls
curl -sI -X OPTIONS $1 | grep "Allow" | cut -d " " -f2-
