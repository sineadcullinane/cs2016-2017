#!/usr/bin/python

# import sys to be able to take in command line arguements
import sys

# from the socket module import all
from socket import *

# Create a UDP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DRGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)

# Assign a variable to the server host
server_host = sys.argv[1]
# get hostname of machine and store in variable 'hostname'
ipaddr = gethostbyname(server_host)
# Assign a port number
serverPort = 6789

# Assign server_address
server_address = (ipaddr, serverPort)

# Try to send a message to the server
try:
    message = 'hello'
    print('sending: ' + message)
    sock.sendto(message.encode(), server_address)
    
    # Receive response from the server and print to screen
    data, server = sock.recvfrom(1024)
    print ('received: ' + data.decode())

# Error handling
except IOError:
    pass

# Close sockets when done
finally:
    print('closing socket')
    sock.close()
