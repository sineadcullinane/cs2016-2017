# from the socket module import all
from socket import *
from time import *

# Create a UDP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DRGRAM is used for UDP)
sock = socket(AF_INET, SOCK_DGRAM)

# Get the host name and ip address
server_host = gethostname()
ipaddr = gethostbyname(server_host)

# Assign a port number
serverPort = 12000

# Assign server_address
server_address = (ipaddr, serverPort)

# Set how long until timeout
sock.settimeout(1)

# Set the start time
startTime = time()

# Variable referring to sequence of ping packages
seq = 0

# While less than 10 pings have been sent
while seq < 10:
    # Increment sequence to 1
    seq += 1
    # Ping message contains ping, the package number and the time it was sent
    ping = "Ping " + str(seq) + " Start Time: " + str(startTime)
    # Send ping to server
    sock.sendto(ping.encode(), server_address)
    
    # Receive response from the server
    try: 
        data, server = sock.recvfrom(1024)
        # Get the end time
        endTime = time()
        # Calculate the round trip time (RTT)
        totalTime = endTime - startTime
        # Print the response to screen
        print (data.decode() + " RTT: " + str(totalTime))
    # If the connection times out, print error to screen
    except timeout:
        print ("Request timed out")

# Close sockets when done
sock.close()
