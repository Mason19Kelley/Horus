################################################################
# Anassas Anderson, James Brooks, Chance Harlon, Clay Hopkins, #
# Mason Kelley, Patrick McDonald, Johnathon Terry              #
# CSC 442/542, CYEN 301                                        #
# Program #2: Vigenere Cipher                                  #
# March 25, 2022                                               #
################################################################

# Import libraries
import sys # sys is used to take arguments from command line

# The vigenere encode method
def encode(message, key):
    cipher = ""
    for i in range(len(message)):
        messagecode = ord(message[i])
        keycode = ord(key[i])
        if keycode > 90:
            keycode -= 32
        keycode -= 65
        keycode = messagecode + keycode
        if (messagecode >= 65) and (messagecode <= 90):
            if keycode > 90:
                keycode -= 90
                keycode += 64
            newletter = chr(keycode)
        elif (messagecode >= 97) and (messagecode <= 122):
            if keycode > 122:
                keycode -= 122
                keycode += 96
            newletter = chr(keycode)
        else:
            newletter = chr(messagecode)
        cipher = cipher + newletter
    return cipher

# The viginere decode method
def decode(message, key):
    cipher = ""
    for i in range(len(message)):
        messagecode = ord(message[i])
        keycode = ord(key[i])
        if keycode > 90:
            keycode -= 32
        keycode -= 65
        keycode = messagecode - keycode
        if (messagecode >= 65) and (messagecode <= 90):
            if keycode < 65:
                keycode += 90
                keycode -= 64
            newletter = chr(keycode)
        elif (messagecode >= 97) and (messagecode <= 122):
            if keycode < 97:
                keycode += 122
                keycode -= 96
            newletter = chr(keycode)
        else:
            newletter = chr(messagecode)
        cipher = cipher + newletter
    return cipher

# Reads a given file and returns its contents as a string
def readFile(file):
    pass

# Writes a given string to a given file
def writeFile(file, result):
    pass

############################
# Main Part of the Program #
############################
    
args = sys.argv
mode = args[1]
key = args[2]
key = key.replace(" ", "")

if len(args) == 3:
    if mode == "-e":
        message = input("")
        result = encode(message, key)
    elif mode == "-d":
        message = input()
        result = decode(message, key)
    print(result)

elif len(args) == 5:
    direction = args[3]
    file = args[4]
    if direction == "<":
        message = readFile(file)
        if mode == "-e":
            result = encode(message, key)
        elif mode == "-d":
            result = decode(message, key)
        print(result)
    elif direction == ">":
        message = input()
        if mode == "-e":
            result = encode(message, key)
        elif mode == "-d":
            result = decode(message, key)
        writeFile(file, result)
