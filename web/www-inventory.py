#!/usr/bin/env python3
#
# www-inventory.pl (Python3)
#
# Clay Wells <cwells@cwells.org>
#
# Find all web servers on a subnet.
#
###############################################################################
# This program is free software: you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)   #
# any later version.                                                          #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               # 
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program. If not, see <http://www.gnu.org/licenses/>.              #
###############################################################################
#
# Change Log
# ==========
#
#
# Future Improvements
# ===================
# 
# - get subnets to search from user input or config file (use variable for now)
# - output to a file for use in another application (inventory, etc.)
#
# Notes
# =====
#
# After compiling our list of hosts with port 443 open we can run the
# following command to obtain certifcate details.
#
# openssl s_client -connect hostname:443
#
# Requirements
# ============
#
#   python3, python3-nmap
#
###############################################################################

import sys
import os
import nmap

# Set the subnet you'd like to scan.
subnet = '192.168.1.0/24'
ports = '80,443'

print('==========================================================================')
print('[+] HTTPS Inventory')
print('[+]')
print('[+] scanning for port 443 on subnet %s' % subnet )
print('[+]  ..this could take a minute.. please wait..')
try:
	nm = nmap.PortScanner()
except nmap.PortScannerError:
	print('[-] Nmap not found', sys.exc_info()[0])
	sys.exit(1)
except:
	print("[-] Unexpected error:", sys.exc_info()[0])
	sys.exit(1)

#nm.scan(subnet, '443')
nm.scan(hosts=subnet, arguments='-p%s --scan-delay 1' % ports)

print('[+] ======================================================================')
for host in nm.all_hosts():
	if nm[host]['tcp'][443]['state'] == 'open':
		print('[+] %s has hostname %s | port 443=%s' % (host,nm[host].hostname(),nm[host]['tcp'][443]['state']))
print('==========================================================================')
# EOF
