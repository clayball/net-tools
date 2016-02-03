#!/usr/bin/env python
# coding: utf-8 
#
# Clay Wells
# 
# syn-packet.py is based on a classic SYN scan. A single SYN packet is sent
# to a single/multiple hosts and single/multiple ports and will quit after
# receving a single response.
#
# MUST BE RUN USING SUDO --OR-- AS ROOT 
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

# require scapy
from scapy.all import *

print '==============================================================================='
print '[+] SYN-Packet'
print '[+]'

# hosts to include in scan
hosts = ["204.79.197.200","173.194.43.96"]

# set the ports to send a SYN packet (should makes sense to send it)
#ports = '22,80,443'

# send to single/multiple hosts/ports
res,nores = sr(IP(dst=hosts)/TCP(sport=RandShort(),dport=[80],flags="SA"))

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

