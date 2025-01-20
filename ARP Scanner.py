#!/usr/bin/env python3

# ARP scanner
from scapy.all import *

# Make sure you modify the variables below:
interface = "eth0"
iprange = "X.X.X.X/X"
macAdd = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=macAdd)/ARP(pdst = iprange) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%")) 
