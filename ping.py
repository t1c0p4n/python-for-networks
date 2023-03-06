import scapy.all as scapy

ip = '192.168.1.1'

reply = scapy.sr1(scapy.IP(dst=ip)/scapy.ICMP(id=1, seq=1, length=64), timeout=3)
if reply is not None:
    print('reply')
    print (reply.src)
    print(reply.dst)
else:
    print ("Não teve resposta do endereço ")