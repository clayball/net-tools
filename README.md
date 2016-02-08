net-tools
=========

This is a repo for the small scripts I find useful. Some of the shell script I plan on adding could
be BASH aliases instead. I hope to add to these and make them more useful and perhaps be used to
create output to be used as input for other scripts/tools.


## Packet ##

Packet crafting scripts live here.


### syn-packet.py ###

syn-packet.py is based on a classic SYN scan. A single SYN packet is sent
to a single/multiple hosts and single/multiple ports and will quit after
receving a single response.


## Web ##

Web related scripts live here.


### inventory443.py, inventory443.rb

20160208: For some reason this script has decided to stop working. After spending time
  trying to figure out the issue I've decided to port this to Ruby. I will leave the
  Python script here for the moment.

Find all HTTPS servers on a subnet. This scans a subnet for hosts with port 443 open.

Edit the script and set the following variables

  - subnet = '192.168.1.0/24'


## Scripts ##

A collection of scripts that may use the output from the web or packet scripts as input.

