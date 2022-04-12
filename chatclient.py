# import necessary libraries for TCP, timing, and terminal
from socket import socket, AF_INET, SOCK_STREAM
from time import time
from sys import stdout

# Constants for determining one and zero
# based off of timing. Also a constant for
# debugging
DEBUG = True
ONE = 0.1
ZERO = 0.025

# socket for teacher's chat server
#ip = "138.47.99.64"
#port = 31337

# socket for my personal chat server
ip = "127.0.0.1"
port = 1337

# make a socket for our server
server = socket(AF_INET, SOCK_STREAM)

# connects to a specific ip and port
server.connect((ip, port))

# recieve first data being sent from server socket 
data = server.recv(4096).decode()

# since we know the server is sending an overt (in ASCII)
# and a covert (in binary) message, these vars will store them
overt_msg = ""
covert_bin = ""

# loop to iterate through each data sent for processing.
# Terminates when "EOF" occurs because this
# indicates covert message has been fully sent
while data.rstrip("\n") != "EOF":
    # print sent overt data to terminal and append it
    # to our overt msg var
    stdout.write(data)
    overt_msg += data
    stdout.flush()
    
    # t0 and t1 keeps track of when data began to be recieved
    # and when it was fully recieved
    t0 = time()
    data = server.recv(4096).decode()
    t1 = time()
    
    # delta keeps track of how long it took to recieve data
    delta = round(t1 - t0, 4)
    
    # if nothing when wrong then print delta to terminal
    if DEBUG:
        stdout.write(f" {delta}\n")
        stdout.flush()
    
    # if delta is close enough to our ONE value
    # then covert binary must be a one
    if abs(delta - ONE) <= 0.01:
        covert_bin += '1'

    # otherwise covert binary must be a zero
    else:
        covert_bin += '0'

# close the connection to server socket
server.close()

# variable to store human readable covert message
# and a variable to keep track of where we are in
# our covert binary variable
covert = ""
i = 0

# loop to iterate through our covert binary message
# to convert it into human readable ASCII values
while i < len(covert_bin):
    # get byte from covert binary variable for processing
    b = covert_bin[i:i+8]

    # try to convert the byte into ASCII representation
    try:
        covert += chr(int(f"0b{b}", 2))

    # if you fail miserably then print '?' to terminal
    except:
        covert += "?"

    # update i to grab the next byte in covert binary message
    i += 8

# finally print the covert and overt messagees to the terminal
print(f"overt message is: {overt_msg}")
print(f"covert message is: {covert[:-3]}")
