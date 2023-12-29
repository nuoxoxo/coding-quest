#!/bin/bash

[ ${#$1} -gt 2 ] && return
[ $1 -gt 0 ] && [ $1 -lt 10 ] && FILENAME="0$1.0"
[ $1 -ge 10 ] && [ $1 -lt 26 ] && FILENAME="$1.0"

URL="https://codingquest.io/api/puzzledata?puzzle=$1"

curl -o ${FILENAME} ${URL}

