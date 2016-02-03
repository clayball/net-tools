net-tools
=========

This is a repo for the small scripts I find useful. Some of the shell script I plan on adding could
be BASH aliases instead. I hope to add to these and make them more useful and perhaps be used to
create output to be used as input for other scripts/tools.

TLS
---

todo

Packet
------

Packet crafting scripts live here.


### syn-packet.py

syn-packet.py is based on a classic SYN scan. A single SYN packet is sent
to a single/multiple hosts and single/multiple ports and will quit after
receving a single response.

### ntpd-check.py

TODO add this script.

Web
---

Web related scripts live here.


### www-inventory.py

Find all web servers on a subnet.

Edit the script and set the following variables

  - subnet = '192.168.1.0/24'
  - ports = '80,443'


