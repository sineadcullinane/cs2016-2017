#Import socket module
from socket import *  
# from datetime import all
from datetime import *

# Create a UDP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_DGRAM is used for UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# get hostname of machine and store in variable 'hostname'
hostname = gethostname()
# Assign a port number
serverPort = 6789

# Assign server_address
server_address = ("", serverPort)

print('starting server at %s port %s' % server_address)
# Bind the socket to server address and server port
serverSocket.bind(server_address)


# Open the server and wait for messages
while True:
    print('Waiting for messages...')

    # Extract the client data and address
    data, client_address = serverSocket.recvfrom(1024)

    if data:
        # Get the date and time the data was sent
        date_time = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
        # Decode received data
        print("Received: " + data.decode())
        # Open a log file and log the client data and the date/time received
        log_file = open('logfile.txt', 'a')
        log_file.write('Client Message: ' + data.decode() + ' Date/Time: ' + date_time + '\n')
        # Close the log file
        log_file.close()
        # If the data is a string, change to uppercase
        if data is str:
            data = data.upper()
        # If the data is not a string/contains an int, return an error message
        else: 
            data = "Can't change int to uppercase"
        # Send the data back to the client
        print("Sending: " + data)
        serverSocket.sendto(data.encode(), client_address)
    # Close the socket
    else:
        serverSocket.close()
