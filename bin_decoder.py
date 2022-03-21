#!/usr/bin/env python3

####################################################
# Group Name: Team Horus
# Group Members: Clay H., Anassas A., Jimmy B., Chance H., Mason K., Patrick M., Johnathon T.
# Date: March 25, 2022
# Description: Program #1: Binary Decoder
####################################################

import sys

# Main code below
# local variables
message = ""
is_bin7 = False
cypher = ""

# get input from terminal
for line in sys.stdin:
    message += line

# iterates through message and looks at only binary numbers (ie 1 or 0)
#then removes anything else from message so we only see binary nubmers
tmp_msg = ""
for i in message:
    if i == '1' or i == '0':
        tmp_msg += i
message = tmp_msg

# if  message is a 7 bit binary number
if len(message)%7 == 0:
    is_bin7 = True

# if message is 7 bit then..
if is_bin7:
    # pad 7 bit message with zeros to make it 8 bit binary number
    tmp_msg = ""
    for i in range(0, len(message), 7):
        tmp_msg += "0" + message[i:i+7]
    message = tmp_msg

    # convert binary sting to decimal int value
    bin_int = int(message, 2);
    
    # determine the number of bytes our message takes
    #using mathematical formula and the .bit_length()
    byte_num = bin_int.bit_length() + 7 // 8
    
    # converts decimal int to an array of bytes representing
    #the decimal int
    #(i.e. (1024).to_bytes(byte_length=2, byteorder='big') == b'\x04\x00')
    bin_arr = bin_int.to_bytes(byte_num, "big")

# otherwise it is 8 bit
else:
    # convert binary string to decimal int value
    bin_int = int(message, 2);

    # determine the number of bytes our message takes
    #using mathematical formula and the .bit_length()
    byte_num = bin_int.bit_length() + 7 // 8

    # converts decimal int to an array of bytes
    #representing the decimal int
    bin_arr = bin_int.to_bytes(byte_num, "big")

# .decode() will convert the binary array to ASCII characters
#then we print it to the screen
print(bin_arr.decode())
