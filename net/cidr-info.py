#!/usr/bin/env python

from netaddr import *
import pprint
import os

# We could get this value in different ways.
# - query for the current ip and netmask of an interface
# - pass the value as an argument to the script
cidr = '192.168.210.0/21'

subnet = IPNetwork(str(cidr))

print '[*] Classless Inter-Domain Routing Address Block Information'
print '[*] ========================================================'
print '[*] ip: %s' % subnet.ip
print '[*] network: %s, broadcast %s' % (subnet.network, subnet.broadcast)
print '[*] netmask: %s, hostmask: %s' % (subnet.netmask, subnet.hostmask)
print '[*] size: %s' % subnet.size

ip_list = list(subnet)

try:
	fs = open('results/' + str(subnet.ip) + '-hosts.txt', 'w')
except IOError:
	print '[-] ERROR: could not open file for writing'


for ip in ip_list:
	print '%s' % ip
	line = str(ip) + '\n'
	try:
		fs.write(line)
	except IOError:
		print '[-] ERROR: could not write to file'

fs.close()

print '[*] hosts written to results/' + str(subnet.ip) + '-hosts.txt'

