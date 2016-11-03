#!/bin/bash

INFILE=$1

while read IP; do
  if [ "$IP" == '' ]; then
    echo 'None'
  else
	# don't include the cruft
    host $IP | awk '{print $5}'
  fi
done < $INFILE

