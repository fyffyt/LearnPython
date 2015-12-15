#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import os
import sys

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

os.unlink('io.tt')
s.bind('./io.tt')        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from'
    print addr
    print c.recv(1024)
    c.send('Thank you for connecting')
    c.close()                # Close the connection
