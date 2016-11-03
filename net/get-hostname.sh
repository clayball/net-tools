#!/bin/bash

# Enhancements/TODO
# 
# Scanning one subnet or address range fine for now but it might be nice to
# enhance this script by adding the following.
# 
# - add CIDR support, i.e. 192.168.2.0/24
# - add automation for 3rd octet, e.g., 192.168.*.*
# - use a number of different DNS servers
# - randomize 1-254 (avoid repeats)


#SUBNET="192.168.1"
SUBNET="10.10.10"

HIGH=254
#LOW=1
i=1

while [ $i -le "$HIGH" ]
do
	HOSTX="${SUBNET}.${i}"
	echo -n -e "${HOSTX}\t"
	host "${HOSTX}" >> subnet-${SUBNET}.csv
	i=$(($i+1))
	# feel like being nice or a little less obvious?
	sleep 0.3
done

echo ""
echo "[+] Done"
