#!/usr/bin/env python
# coding: utf-8 
#
# Clay Wells
# 
# A single SYN packet is sent to single/multiple hosts and single/multiple
# ports and will quit after receving a single response.
#
# MUST BE RUN USING SUDO --OR-- AS ROOT 
#
# Updates:
# 
# The results are not interesting at all. Will fix soon.
#
# 20161111, Clay
# - get a single IP target from command-line (start with a single IP address)
# 
#
###############################################################################

# require scapy
from scapy.all import *
import sys

print '[*]'
print '[*] SYN-Packet'
print '[*]'

# hosts to include in scan
#hosts = ["204.79.197.200","173.194.43.96"]
target = sys.argv[1]
print '[*] Target: ', target 

# set the ports to send a SYN packet (should makes sense to send it)
#ports = '22,80,443'

# Build and send to port(s) of target
res,nores = sr(IP(dst=target)/TCP(sport=RandShort(),dport=[80],flags="SA"))

# =============================================================================
# Results can be displayed in different ways.
# =============================================================================

# This needs some work! Why not use nmap istead?

# only display packets with the “SA” flag set
res.nsummary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA")

print '[+] ==========================================================================='

# show what's open (single host)
res.summary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA",
    prn=lambda(s,r):(s.dst, r.sprintf("%TCP.sport% is open")))

print '[+] done'

