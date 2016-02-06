#!/bin/bash

# Run this after web/inventory443.py
# - arg[1] = results file from inventory443.py

# sslyze is required, https://github.com/nabla-c0d3/sslyze 

# TODO:
# - It might be nice to place the .out files in reports/

while IFS='' read -r host || [[ -n "$host" ]]; do
    echo "[+] Checking host: ${host}"
    sslyze_cli.py --regular ${host} > ${host}.out
done < "$1"
