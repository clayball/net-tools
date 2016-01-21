#!/bin/bash

# TODO: add flag to specify URL on command line (query single host)
#       add flag to specify URL file on command line (query multiple hosts)
#       add usage details

# Read host from arg1
URL=$1

curl --head $URL

# Read host list
#echo "Fetching headers from host(s)"
#echo "============================================================="
#while IFS='' read -r line || [[ -n $line ]]; do
#    echo "Host read from file: $line"
#    curl --head $line
#    echo "============================================================="
#done < "$1"

