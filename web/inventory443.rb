#!/usr/bin/env ruby

###############################################################################
# Porting this from Python to Ruby.
#
# Clay Wells
#
# This script requires ruby-nmap..
#
#   https://github.com/sophsec/ruby-nmap
#
#
# Find all HTTPS servers on a subnet. 
# 
# Enhancements
# ============
# - get subnet/hosts from the command line
# - save output file with the date, e.g. results443-YYYYMMDD.xml
# - output as hostname:443 so we can use the resulting ouput as input for sslyze.
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


require 'nmap/program'

subnet='192.168.1.1-254'

Nmap::Program.scan do |nmap|
  nmap.syn_scan = false
  nmap.service_scan = true
  nmap.os_fingerprint = false
  nmap.xml = 'results443.xml'
  nmap.ports = [443]
  nmap.targets = "#{subnet}"
end

