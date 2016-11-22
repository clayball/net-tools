#!/usr/bin/env python

from netaddr import *
import sys
import fileinput

# TODO add option -f file
# We could get this value in different ways.
# - hard-coded ugliness 192.168.1.0/24
# - pass the subnet as an argument to the script
# TODO add flags allowing one subnet as a command option or read from a file


def process_line(line):
    #
    subnet = IPNetwork(str(line))

    print '[*] Classless Inter-Domain Routing Address Block Information'
    print '[*] ========================================================'
    print '[*] ip: %s' % subnet.ip
    print '[*] network: %s, broadcast %s' % (subnet.network, subnet.broadcast)
    print '[*] netmask: %s, hostmask: %s' % (subnet.netmask, subnet.hostmask)
    print '[*] size: %s' % subnet.size

    ip_list = list(subnet)

    try:
        fs = open(str(subnet.ip) + '-hosts.txt', 'w')
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
    print '[*] hosts written to ' + str(subnet.ip) + '-hosts.txt'
# End: process()


#cidr = '130.91.176.0/22'
#cider = sys.argv[1]

# Read from a file that lists CIDR subnets of interest.
cidrfile = sys.argv[1]

# If -f file then iterate over file
for line in fileinput.input():
    process_line(line)
