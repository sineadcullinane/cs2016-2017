# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
# get hostname of machine and store in variable 'hostname'
hostname = gethostname()
#get ip address of machine and store in variable 'ipaddr'
ipaddr = gethostbyname(hostname)
server_address = (hostname, 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
print('ip address at %s' % ipaddr)
# Connect the socket to the host and port
sock.connect(server_address)

try:
    
    # Send data
    # prompt client for data
    message = input('Enter server message now: ')
    # message = 'This is the message.  It will be repeated.'
    print('sending %s' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(16).decode()
        amount_received += len(data)
        print('received %s' % data)

finally:
    print('closing socket')
    sock.close()
