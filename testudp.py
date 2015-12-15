#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.sendto("hahaha", (host,port))
s.close                     # Close the socket when done
