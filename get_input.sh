#!/bin/bash

[ ${#$1} -gt 2 ] && return

curl -o "$1.0" "https://codingquest.io/api/puzzledata?puzzle=$1"
