#!/usr/bin/env python3

####################################################
# Group Name: Team Horus
# Group Members: Clay H., Anassas A., Jimmy B., Chance H., Mason K., Patrick M., Johnathon T.
# Date: March 25, 2022
# Description: Program #1: Binary Decoder
####################################################

# imports
from ftplib import FTP

# constants
IP = "138.47.99.64"
#IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/10"
USE_PASSIVE = True
METHOD = 10

# connecting to ftp server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# go to folder and get files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# close ftp connection
ftp.quit()

# local variables
tmp = ""
tmp_files = []
tmp_str = ""
tmp_bool = False

# below code takes file permissions
#and decodes them accordingly
for f in files:
    # reset tmp_bool to false for every file
    tmp_bool = False

    # if using method 10
    if METHOD == 10:
        # then iterate over each file
        #permission and designate zeros
        #to dashes and ones otherwise
        for c in f[:10]:
            if c == '-':
                tmp_str += '0'
            else:
                tmp_str += '1'

    # otherwise we are using method 7
    else:
        # then iterate over each file's
        #first three permission bits
        #to determine if it fits our
        #method 7 criteria
        for c in f[:3]:
            if c != '-':
                tmp_bool = True

        # if this file's permission
        #fits the method 7 criteria
        if tmp_bool == False:
            
            # then iterate over it's last
            #7 permission bits and
            #designate a zero to dashes
            #and ones otherwise
            for c in f[3:10]:
                if c == '-':
                    tmp_str += '0'
                else:
                    tmp_str += '1'

# the following for loop will convert binary permission
#values to decimal then to an ASCII character.
for i in range(0, len(tmp_str), 7):
    
    # if there are enough bits to convert to ASCII
    if i + 7 <= len(tmp_str):
        tmp += chr(int(int(tmp_str[i:i+7], 2)))

    # otherwise if we have less than 7 bits to convert
    #then pad the missing bits with zeros
    else:
        another_tmp = tmp_str[i:] + "0" * (7- len(tmp_str) % 7)
        tmp += chr(int(int(another_tmp, 2)))

# print ASCII character string to terminal
print(tmp)
