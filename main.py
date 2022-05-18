import pyfiglet
import sys
import socket
from datetime import datetime
import re
  
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern to extract the number of ports you want to scan. 
# You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port numbers, will be using the variables later on.
port_min = 0
port_max = 65535

open_ports = []
# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning all 
    # the ports is not advised.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (Ex. would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

# Basic socket port scanning
for port in range(port_min, port_max + 1):
    # Connect to socket of target machine. We need the ip address and the port number we want to connect to.
    try:
        # Create a socket object

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            # We put a timeout at 0.5s. So for every port it scans it will allow 0.5s to connect to the server.
 
            s.settimeout(0.5)
            # connects to ip address and socket
            s.connect((ip_add_entered, port))
            # If the following line runs then then it was successful in connecting to the port.
            open_ports.append(port)

    except:
        # We don't need to do anything here. If we were interested in the closed ports we'd put something here.
        pass

# We only care about the open ports.
for port in open_ports:
    # We use an f string to easily format the string with variables so we don't have to do concatenation.
    print(f"Port {port} is open on {ip_add_entered}.")