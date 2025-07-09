# Module for everything networks related
import socket
import sys
import os
from datetime import datetime

# Clear the screen with previous information
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.getenv('TERM'):
        os.system('clear')


clear_screen()

# Enter IP Address
remoteServer = input("Enter a remote host to scan: ")

try:
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("_" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("_" * 60)

    t1 = datetime.now()

    # AF_INET is Address Family Internet for IPv4 addresses
    # SOCK_STREAM is to use the TCP connection. UDP is SOCK_DGRAM
    # Connects to the IP address initially entered
    for port in range(1, 11): # Specify number of ports here
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {} : Open".format(port))
        else:
            print("Port {} : Closed".format(port))
        sock.close()

# Stop script from running
except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved. Exiting...")
    sys.exit()

except socket.error:
    print("\nCouldn't connect to server")
    sys.exit()

# Calculate time taken now (t2) subtracted by time taken then (t1) for scan to complete
t2 = datetime.now()
total = t2 - t1
print("Scanning completed in:", total)
