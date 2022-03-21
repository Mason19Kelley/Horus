#!/usr/bin/env python3

####################################################
# Group Name: Team Horus
# Group Members: Clay H., Anassas A., Jimmy B., Chance H., Mason K., Patrick M., Johnathon T.
# Date: March 25, 2022
# Description: Program #2: Vigener Cipher
####################################################

import sys

# global variables
message = ""
key = ""
cypher = ""

# this user defined function will take a 'crypt_type'
#that should either be '-e' or '-d' to determine wether
#we are encrypting or decrypting our message. Then it will
#proceed to either decrypt or encrypt the message and print
#it to the terminal. Note: it encrypts using the formula Ci=(Pi+Ki)%26
#and decrypts using Pi=(26+Ci-Ki)%26
def cryption(crypt_type):
    # declare/setup local variables
    cypher = ""
    tmp_i = 0   # counter to keep track where we are in our key

    # if we are encrypting then...
    if crypt_type == "-e":
        # iterate through our message
        for p in message:
            # if we exceeded our key length then cycle back
            #to the beginning of our key
            if tmp_i >= len(key):
                tmp_i = 0
            k = key[tmp_i]
            tmp_i += 1
            
            # if our message is capital then..
            if p.isupper():
                # make our key capital to retain message's lettercase
                k = k.upper()
                # use mathematical formula to encrypt message with regards
                #to uppercase ASCII characters (ie p-65)
                #Note: chr() converts a decimal to ASCII character and
                #ord() converts ASCII character to a decimal
                cypher += chr(65 + (ord(p) - 65 + ord(k) - 65) % 26)

            # otherwise if our message is lowercase then..
            elif p.islower():
                # make our key lowercase to retain message's lettercase
                k = k.lower()
                # use mathematical formula to encrypt message with regards
                #to lowercase ASCII characters (ie p-97)
                cypher += chr(97 + (ord(p) - 97 + ord(k) - 97) % 26)

            # otherwise p in message is not a letter A-Z or a-z
            #so ignore it and continue to the next character
            else:
                tmp_i -= 1
                cypher += p
                continue

        # print encrypted message to terminal
        print(cypher)

    # otherwise if we are decrypting our message then...
    elif crypt_type == "-d":
        # iterate through our message
        for c in message:
            # if we exceeded our key length then cyble back
            #to the beginning of our key
            if tmp_i >= len(key):
                tmp_i = 0
            k = key[tmp_i]
            tmp_i += 1

            # if our message is capital then..
            if c.isupper():
                # make our key capital to retain message's lettercase
                k = k.upper()
                # use mathematical formula to decrypt message with regards
                #to uppercase ASCII characters (ie c-65)
                cypher += chr(65 + (26 + (ord(c) - 65 - (ord(k) - 65))) % 26)

            # otherwise if our message is lowercase then..
            elif c.islower():
                # make our key lowercase to retain message's lettercase
                k = k.lower()
                # use mathematical formula to decrypt message with regards
                #to lowercase ASCII characters (ie c-97)
                cypher += chr(97 + (26 + ord(c) - 97 - (ord(k) - 97)) % 26)
            
            # otherwise c in message is not a letter A-z or a-z
            #so ignore it and continue to the next character
            else:
                tmp_i -= 1
                cypher += c
                continue

        # print decrypted message to terminal
        print(cypher)

# main code here
# if atleast 3 args given
if len(sys.argv) > 2:
    # if we are getting input from user
    if sys.stdin.isatty():
        # infinite loop until ctrl+d is pressed
        while 1:
            # get input from terminal
            try:
                message = input()

            # if ctrl+d is pressed it raises an error
            #with input() so we manually handle it
            #and just break out of the while loop
            except:
                break
            
            # strip() gets rid of any unwanted newlines or
            #spaces in the message
            message = message.strip()
            key = sys.argv[2]               # key will be second arg given
            key = key.replace(" ", "")      # remove spaces in key
            cryption(sys.argv[1])           # call cryption function
    
    # otherwise we are getting input from a file
    else:
        # get input from terminal
        for line in sys.stdin:
            message += line

        # strip() gets rid of any unwanted newlines or
        #spaces in the message
        message = message.strip()
        key = sys.argv[2]               # key will be second arg given
        key = key.replace(" ", "")      # remove spaces in key
        cryption(sys.argv[1])           # call cryption function
