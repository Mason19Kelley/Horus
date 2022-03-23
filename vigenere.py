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
    cipher = "" # Cipher starts as empty string
    j = 0 # This counter keeps track of the current position in the key
    
    # Do this for the length of the message
    for i in range(len(message)): 
        
        # Get the character code of the current letter in the message
        messagecode = ord(message[i])
        
        # If we're not at the end of the key yet, get the character code of the current letter in the key
        if (j < len(key)): 
            keycode = ord(key[j])
        # If we are at the end of the message, set the key back to the beginning and get the character code of the current letter in the key
        else: 
            j = 0 
            keycode = ord(key[j]) # Set the key to zero

        # This if statement just makes all key letters capital. Basically the key is the same regardless of capitalization
        # Capitalization in the message will be maintained though
        if keycode > 90:
            keycode -= 32

        # By subtracting 65, we're basically just getting the "displacement" required for the key
        # This is how much will be shifting the message letter's code by
        # 65 is the character code value of capital A
        keycode -= 65

        # This keycode is the code of the displaced letter, but we have to do some extra checks to account for capitalization and wraparound
        keycode = messagecode + keycode

        # If the character code of the current letter in the message is between 65 and 90, it's a capital letter
        if (messagecode >= 65) and (messagecode <= 90):
            # If the letter we are looking to use for the encryption is greater than 90, then we need to wrap around back to capital A
            if keycode > 90:
                keycode -= 90
                keycode += 64
            # With all those checks done, we can convert the keycode back into the encrypted letter and increase the key counter
            newletter = chr(keycode)
            j += 1

        # If the character code of the current letter in the message is between 97 and 122, it's a lowercase letter
        elif (messagecode >= 97) and (messagecode <= 122):
            # If the letter we are looking to use for the encryption is greater than 122, then we need to wrap around back to lowercase a
            if keycode > 122:
                keycode -= 122
                keycode += 96
            # With all those checks done, we can convert the keycode back into the encrypted letter and increase the key counter
            newletter = chr(keycode)
            j += 1

        # Otherwise, we've run into a character outside of the alphabet (A-Z, a-z)
        # In that case, we leave the character as it is
        # You'll notice there's no increase of the key counter (j += 1) here
        # The instructions basically implied to skip these letters, and in order to get the same result as the example,
        # the key needed to be skipped for these letters
        else:
            newletter = chr(messagecode)

        # Update the full cipher with the new encrypted letter and repeat until we've gone through the whole message
        cipher = cipher + newletter

    # Once the cipher is complete, return it
    return cipher

# The viginere decode method
# This literally does the same thing as the encode method above, just in reverse
# So it'll check to wraparound back to Z/z, keycode adjustments are subtracted instead of added, etc.
def decode(message, key):
    cipher = ""
    j = 0
    for i in range(len(message)):
        messagecode = ord(message[i])
        if (j < len(key)):
            keycode = ord(key[j])
        else:
            j = 0
            keycode = ord(key[j])
        if keycode > 90:
            keycode -= 32
        keycode -= 65
        keycode = messagecode - keycode
        if (messagecode >= 65) and (messagecode <= 90):
            if keycode < 65:
                keycode += 90
                keycode -= 64
            newletter = chr(keycode)
            j += 1
        elif (messagecode >= 97) and (messagecode <= 122):
            if keycode < 97:
                keycode += 122
                keycode -= 96
            newletter = chr(keycode)
            j += 1
        else:
            newletter = chr(messagecode)
        cipher = cipher + newletter
    return cipher

# Reads a given file and returns its contents as a string
def readFile(file):
    f = open(file)
    message = f.read()
    f.close()
    return message

# Writes a given string to a given file
def writeFile(file, result):
    f = open(file, 'w')
    f.write(result)
    f.close()
    return

############################
# Main Part of the Program #
############################

# Fetch arguments from command line
args = sys.argv

# This python file is *technically* the first argument
# The mode (encryption/decryption is the real first argument
# The key is the second
# Other arguments depend on how many are given
mode = args[1]
key = args[2]

# Closes and ignores spaces in the key
key = key.replace(" ", "")

# If only 3 (2) arguments are given
if len(args) == 3:
    
    # Run encode if mode is -e
    if mode == "-e":
        # Get the message as an input from the user
        message = input()
        result = encode(message, key)

    # Run decode if mode is -d
    elif mode == "-d":
        # Get the message as input from the user
        message = input()
        result = decode(message, key)

    # Print the result to command line
    print(result)

# If 5 (4) arguments are given
elif len(args) == 5:
    # The "direction" (either to the command line or to a file) is the third argument
    # The file itself is the fourth argument
    direction = args[3]
    file = args[4]

    # If we're going to the command line
    if direction == "<":
        # Read the file given
        message = readFile(file)

        # Run encryption on the text from the file if mode is -e
        if mode == "-e":
            result = encode(message, key)

        # Run decryption on the text from the file if mode is -d
        elif mode == "-d":
            result = decode(message, key)

        # Print the text to command line
        print(result)

    # If we're going to the file
    elif direction == ">":
        # Get the message as input from the user
        message = input()

        # Run encryption on the message if mode is -e
        if mode == "-e":
            result = encode(message, key)

        # Run decryption on the message if mode is -d
        elif mode == "-d":
            result = decode(message, key)

        # Write the text to the given file
        writeFile(file, result)
