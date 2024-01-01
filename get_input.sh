#!/bin/bash

[ ${#1} -gt 2 ] && exit 1

curl -o "$1.0" "https://codingquest.io/api/puzzledata?puzzle=$1"
