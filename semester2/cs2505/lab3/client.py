#!/usr/bin/python

# import sys to be able to take in command line arguements
import sys

# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# Assign variables to each arguement in the command line
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]
# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
# Set the server_address equal to the command line arguements
server_address = (server_host, int(server_port))
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)

# Connect the socket to the host and port
sock.connect(server_address)
# While the client is connected to the server
try:
      
      # Send data
      try: 
         # Send the GET request to the server
         httpRequest = ("""GET %s HTTP/1.1 """ % (filename))
      except NameError:
         pass
      # Data is transmitted to the server with sendall()
      # encode() function returns bytes object
      sock.sendall(httpRequest.encode())

      # Look for the response
      amount_received = 0
      amount_expected = len(httpRequest)
      
      while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        # Change encoding from 16-bit to 64-bit
        data = sock.recv(1024).decode()
        amount_received += len(data)
        # Print the server message to screen
        print('%s' % data)

# If client is no longer connected to the server, close the connection
except IOError:
    print('closing socket')
    sock.close()
