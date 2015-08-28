net-tools
=========

This is a repo for the small scripts I find useful.


Packet
------

Packet crafting scripts live here.


### syn-packet.py

syn-packet.py is based on a classic SYN scan. A single SYN packet is sent
to a single/multiple hosts and single/multiple ports and will quit after
receving a single response.


Web
---

Web related scripts live here.


### www-inventory.py

Find all web servers on a subnet.

Edit the script and set the following variables

  - subnet = '192.168.1.0/24'
  - ports = '80,443'


