#!/usr/bin/env python3

# Script Name : CVE-2024–24919.py 
# Author : Subhankar Paul (starlox)
# Created : 23-03-2024
# Purpose : Simple Service Banner Grabbing
# Use python3 banner.py [For Details Information]

import socket
import sys

usage = "\033[1m[+]\033[0m \033[1m\033[32mUsage : python3 banner.py IP PORT\033[0m\033[0m"
banner = '''\n\033[1m\033[0m \033[1m\033[32m
     ___  ____              ___  ___
    / _/ /   / /|  / /|  / /    / _/  
   / _  / - / / | / / | / /--  / |
  /__/ /   / /  |/ /  |/ /___ /  |
 \033[0m\033[0m
                         \033[0m \033[1m\033[31m@starlox\033[0m\033[31m

'''

# Check if the IP is Valid
def is_valid_ip(ip_str):
    try:
        socket.inet_aton(ip_str)
        return True
    except socket.error:
        return False

# Check if the Port is Valid       
def is_valid_port(port_str):
    try:
        port = int(port_str)
        return 0 <= port <= 65535
    except ValueError:
        return False

# Take input Condition
if(len(sys.argv) <= 2):
    print(banner)
    print(usage)
    sys.exit()

# Take Input
ip = str(sys.argv[1])
port = str(sys.argv[2])

# Print Exception
if not is_valid_ip(ip):
    print("\n\033[1m[+]\033[0m \033[1m\033[32mInvalid IP address. Please provide a Valid IP.\033[0m\033[0m")
    sys.exit()
    
if not is_valid_port(port):
    print("\n\033[1m[+]\033[0m \033[1m\033[32mInvalid PORT number. Please provide a valid PORT in the range 0-65535.\033[0m\033[0m")
    sys.exit()

try:
    # Print banner
    print(banner)

    # Connect with Socket
    s = socket.socket()
    
    # Set Timeout
    s.settimeout(5)
    
    # Connect with that IP & Port
    s.connect((ip, int(port)))

    # Receive banner
    banner = s.recv(1024).decode('utf-8').strip()

    # Print Response with Highlighting
    print("\n\033[1m[+]\033[0m \033[1m\033[32mResponse:\033[0m\033[0m", banner, "\033[0m\033[0m")

except ConnectionRefusedError:
    print("\n\033[1m[+]\033[0m \033[1m\033[31mConnection refused. The specified port is not running or not reachable.\033[0m\033[31m")

except socket.timeout:
    print("\n\033[1m[+]\033[0m \033[1m\033[31mConnection timed out. The specified port may not be reachable or is taking too long to respond.\033[0m\033[0m")
except Exception as e:
    print("\n\033[1m[+]\033[0m \033[1m\033[31mAn error occurred:", str(e), "\033[0m\033[0m")

finally:
    # Close the socket
    s.close()
