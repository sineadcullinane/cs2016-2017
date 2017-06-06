# from the socket module import all
from socket import *
# from datetime import all
from datetime import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# get hostname of machine and store in variable 'hostname'
hostname = gethostname()
#get ip address of machine and store in variable 'ipaddr'
ipaddr = gethostbyname(hostname)
server_address = (hostname, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
print('*** ip address at %s ***' % ipaddr)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
	
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            if data:
	        # get the date and time of when the message was received
                date_time = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
                # create/open a log file 'filename.txt'
                client_file = open('filename.txt', 'a')
                # write/append the data and the date/time to the log file 'filename.txt'
                client_file.write('Message: ' + data + ' Date/Time: ' + date_time + '\n')
                # close the log file 'filename.txt'
                client_file.close()
                # print the received data to the command line
                print('received %s' % data)
                print('sending data back to the client')
                # encode() function returns bytes object
                connection.sendall(data.encode())
                # tell client that message was logged
                connection.sendall(('\n Msg_Logged').encode())
            else:
	        # tell server that no more data was received
                print('no more data from', client_address)
                break
    except IOError:
        # error checking
        print('no more data from', client_address)
        pass

    finally:
        # Clean up the connection
        connection.close()

# now close the socket
sock.close();
