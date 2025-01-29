#!/usr/bin/python

from scapy.all import *
import time

source="140.233.103.156"
hostname="140.233.103.130"
port=4000

# scapy auto TCP handshale fx
# SYN
sport = random.randint(1024, 65535)
ip = IP(src=source, dst=hostname)
SYN = TCP(sport=sport, dport=port, flags="S", seq=1000)
SYNACK = sr1(ip/SYN)

# ACK
ACK = TCP(sport=sport, dport=port, flags="A", seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)
send(ip/ACK)

