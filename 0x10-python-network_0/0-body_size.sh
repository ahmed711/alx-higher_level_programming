#!/bin/bash
#get content length of api rest calls
curl -s -o /dev/null -w "%{size_download}\n" $1
