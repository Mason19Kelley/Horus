################################################################
# Anassas Anderson, James Brooks, Chance Harlon, Clay Hopkins, #
# Mason Kelley, Patrick McDonald, Johnathon Terry              #
# CSC 442/542, CYEN 301                                        #
# Program #7: Steg                                             #
# May 6, 2022                                                  #
################################################################


# libraries
import sys
import re
import os

# constant
SENTINEL = bytearray([0, 255, 0, 0, 255, 0])

# function to check and get conditions passed to program
def get_conditions():
    # condition using regular expressions to determine if
    # proper parameters were given to the program
    condition = re.compile(r'^-(s|r) -(b|B) -o(\d*)( -i(\d*))? (-w([^ ]*))( -h([^ ]*))?$')
    
    # args variable to store our arguments given to program
    args = ""

    # process given parameters to program
    i = 0
    for arg in sys.argv:
        # if first element in argv...
        if (i == 0):
            # then skip it because
            # it is just the name of the program
            i += 1
            continue

        # otherwise if not the first element then add it to args
        args += arg

        # add a space in between args for regular expression check
        if (i < len(sys.argv)-1):
            args += " "
        i += 1
    
    # search() function will check if args matches required
    # regular expression condition
    tmp = condition.search(args)

    # if args does not match the condition then exit program
    if (tmp == None):
        print("bad inputs")
        exit()

    # if conditions met then get our arg values using groups() function
    store, bit, offset, skip1, interval, skip2, wrapper, skip3, hidden = tmp.groups()

    # by default the offset will be 0
    if (offset == ''):
        offset = 0
    # by default the interval will be 1
    if (interval == '' or interval == None):
        interval = 1
    args = [store, bit, int(offset), int(interval), wrapper, hidden]

    # return the now processed arguments
    return args

# function to store hidden file by byte method
def store_by_byte(wrap, hide, offset, interval):
    try:
        with open(os.path.join(sys.path[0], wrap), "rb") as f:
            W = bytearray(f.read())
    except:
        print("Bad wrapper file, make sure it is spelled correctly and in the current directory")
    try:
        with open(os.path.join(sys.path[0], hide), "rb") as f:
            H = bytearray(f.read())
    except:
        if (hide != ''):
            print("Bad hidden file, make sure it is spelled correctly and in the current directory")
   
    i = 0
    while (i < len(H)):
        W.pop(offset)
        W.insert(offset, H[i])
        offset += interval
        i += 1

    i = 0
    while (i < len(SENTINEL)):
        W.pop(offset)
        W.insert(offset, SENTINEL[i])
        offset += interval
        i += 1
    sys.stdout.buffer.write(W)

# function to store hidden file by bit method
def store_by_bit(wrap, hide, offset, interval):
    try:
        with open(os.path.join(sys.path[0], wrap), "rb") as f:
            W = bytearray(f.read())
    except:
        print("Bad wrapper file, make sure it is spelled correctly and in the current directory")
    try:
        with open(os.path.join(sys.path[0], hide), "rb") as f:
            H = bytearray(f.read())
    except:
        if (hide != ''):
            print("Bad hidden file, make sure it is spelled correctly and in the current directory")

    i = 0
    while (i < len(H)):
        for j in range(0, 8):
            tmp = W.pop(offset)
            tmp &= 0b11111110
            W.insert(offset, (tmp | ((H[i] & 0b10000000) >> 7)))
            tmp = H.pop(i)
            H.insert(i, (tmp << 1))
            offset += interval
        i += 1

    i = 0
    while (i < len(SENTINEL)):
        for j in range(0, 8):
                tmp = W.pop(offset)
                tmp &= 0b11111110
                W.insert(offset, (tmp | ((SENTINEL[i] & 0b10000000) >> 7)))
                tmp = SENTINEL.pop(i)
                SENTINEL.insert(i, (tmp << 1))
                offset += interval
        i += 1
    sys.stdout.buffer.write(W)

# function to extract hiddent file by byte method
def extract_by_byte(wrap, hide, offset, interval):
    try:
        with open(os.path.join(sys.path[0], wrap), "rb") as f:
            W = bytearray(f.read())
    except:
        print("Bad wrapper file, make sure it is spelled correctly and in the current directory")

    H = bytearray([])

    while (offset < len(W)):
        b = W[offset]

        if (b == 0):
            i = interval
            o = offset
            tmp = [W[o+i], W[o+(2*i)], W[o+(3*i)], W[o+(4*i)], W[o+(5*i)]]
            check = [255, 0, 0, 255, 0]
            if (tmp == check):
                break
        H.append(b)
        offset += interval
    sys.stdout.buffer.write(H)

# function to extract hidden file by bit method
def extract_by_bit(wrap, hide, offset, interval):
    try:
        with open(os.path.join(sys.path[0], wrap), "rb") as f:
            W = bytearray(f.read())
    except:
        print("Bad wrapper file, make sure it is spelled correctly and in the current directory")

    H = bytearray([])

    #print(f"len of w = {len(W)}")
    #print(f"interval = {interval}")

    while (offset < len(W)):
        b = 0
        for j in range(0, 8):
            b |= (W[offset] & 0b00000001)
            if (j < 7):
                b <<= 1
                offset += interval
        
        # check
        if (b == 0):
            i = interval
            o = offset + i
            tmp = []
            for j in range(0, 5):
                tmp_b = 0
                for k in range(0, 8):
                    tmp_b |= (W[o] & 0b00000001)
                    if (k < 7):
                        tmp_b <<= 1
                        o += i
                tmp.append(tmp_b)
                o += i
            check = [255, 0, 0, 255, 0]
            if (tmp == check):
                break

        H.append(b)
        offset += interval
    sys.stdout.buffer.write(H)

# function to determine which store/retrieval function to call
# and calls it
def choose(args):
    # if storing
    if (args[0] == 's'):
        # if using bit method
        if (args[1] == 'b'):
            store_by_bit(args[4], args[5], args[2], args[3])
        # otherwise we use the Byte method
        else:
            store_by_byte(args[4], args[5], args[2], args[3])

    # otherwise we're retrieving
    else:
        # if using bit method
        if (args[1] == 'b'):
            extract_by_bit(args[4], args[5], args[2], args[3])
        # otherrwise we use the Byte method
        else:
            extract_by_byte(args[4], args[5], args[2], args[3])

############
### MAIN ###
############

# get our arguments
args = get_conditions()

# determine which function to call and call it
choose(args)
