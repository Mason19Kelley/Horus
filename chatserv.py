# import necessary libraries for TCP and timing
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

# variable to keep track of port to use
# ZERO and ONE variable to keep track of
# timing for covert message to be sent
port = 1337
ZERO = 0.025
ONE = 0.1

# make a socket to host this server
s = socket(AF_INET, SOCK_STREAM)

# bind it to ip and port
# here any ip can connect on port 1337
s.bind(("", port))

# open port for client socket
s.listen(0)
print("Server is listening...")

# c is the client we have accepted
#addr is the address of the client
client, addr = s.accept()

# overt message
msg = "Some sort of overt message is being transmitted here. But there is a hidden message being covertly transmitted! Can you guess it?\n"

# covert_msg = "secret code" + "EOF"
covert_msg = "Spectacular achievement is always preceded by unspectacular preparation. -- Robert H. Schuller\n"

# variable to store covert message converted to binary
covert_msg_bin = ""

# loop to iterate through our covert message to convert
# it to binary
for c in covert_msg:
    covert_msg_bin += bin(ord(c))[2:].zfill(8)         # bin(ord('s'))[2:].zfill(8)  -->  '01110011'

# print statements for debugging purposes
#print(len(covert_msg_bin))
#print(covert_msg_bin)

# n variable to keep track of where we are in the
# covert binary message. len_bin_msg variable to
# keep track of how much of the covert binary message
# has been processed (sent)
n = 0
len_bin_msg = 0

# loop to 
while len_bin_msg < len(covert_msg_bin):
    for i in msg:
        client.send(i.encode())
        if covert_msg_bin[n] == '0':
            sleep(ZERO)
        else:
            sleep(ONE)
        n = (n + 1) % len(covert_msg_bin)
    len_bin_msg += len(msg)

# send 'EOF' to denote that the covert message has
# been fully sent
client.send("EOF".encode())
print("Message sent...")

# Finally close the connection to the client
client.close()
