#!/usr/bin/env python
#This script tries to connect to the subdomains and assumes the ones that accept the connection exist. Needs requests and sys libraries.

import requests 
import sys 

sub_list = open(<"subdomains.txt">).read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)