#!/usr/bin/env python

from netaddr import *
import sys
import os
import fileinput
import getopt

# This is coded to run without the python command, e.g., ./net/cidr-info.py
# Be sure to chmod u+x cidr-info.py

def usage():
    comm = os.path.basename(sys.argv[0])

    if os.path.dirname(sys.argv[0]) == os.getcwd():
        comm = "./" + comm
    print "Usage: ./cidr-info.py option \n"
    print "       -s: subnet in CIDR notation"
    print "       -f: file containing many CIDR notated subnets, one subnet per line"
    print "       -h: display usage details"
    print "\nExamples:"
    print "        " + comm + " -s 192.168.1.0/24"
    print "        " + comm + " -f subnets-all.csv"


def show_banner():
    print ' '
    print '    Classless Inter-Domain Routing Address Block Information'
    print ' '
    print ' ######  #### ########  ########     #### ##    ## ########  #######'
    print '##    ##  ##  ##     ## ##     ##     ##  ###   ## ##       ##     ##'
    print '##        ##  ##     ## ##     ##     ##  ####  ## ##       ##     ##'
    print '##        ##  ##     ## ########      ##  ## ## ## ######   ##     ##'
    print '##        ##  ##     ## ##   ##       ##  ##  #### ##       ##     ##'
    print '##    ##  ##  ##     ## ##    ##      ##  ##   ### ##       ##     ##'
    print ' ######  #### ########  ##     ##    #### ##    ## ##        #######'
    print ' '
    print '====================================================================='
    print ' '


def process_line(line):
    subnet = IPNetwork(str(line))

    print '[*] subnet: %s' % line
    print '[*] network: %s, broadcast %s' % (subnet.network, subnet.broadcast)
    print '[*] netmask: %s, hostmask: %s' % (subnet.netmask, subnet.hostmask)
    print '[*] total number of hosts: %s' % subnet.size
    print ' '

    ip_list = list(subnet)
    try:
        fs = open(str(subnet.ip) + '-hosts.txt', 'w')
    except IOError:
        print '[-] ERROR: could not open file for writing'
    for ip in ip_list:
        # Print each IP, may want to leave this commented out
        #print '%s' % ip
        line = str(ip) + '\n'
        try:
            fs.write(line)
        except IOError:
            print '[-] ERROR: could not write to file'

    fs.close()
    print '[*] IP addresses written to ' + str(subnet.ip) + '-hosts.txt'
    print '    ================================================'


def mymain(argv):
    if len(argv) != 2:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "s:f:h")
    except getopt.GetoptError:
        usage()
        sys.exit()

    show_banner()

    # Only one method will be used, -s or -f
    for opt, arg in opts:
        if opt == '-s':
            process_line(arg)
        elif opt == '-f':
            for line in fileinput.input(arg):
                process_line(line)
        elif opt == '-h':
            usage()
            sys.exit()
        else:
            print '[-] No valid opts found'


# Main section
# ============
if __name__ == "__main__":
    try:
        mymain(sys.argv[1:])
    except KeyboardInterrupt:
        print "Process interrupted by user.."
    except:
        sys.exit()
