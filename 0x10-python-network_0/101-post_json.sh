#!/bin/bash
# Displays only the status code
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
