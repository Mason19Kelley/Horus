import sys

# decides whether input is 7 bit or 8 bit ASCII
# returns tuple of (7), (8), or (7,8)
def checkLength(byte):
	if len(byte) % 7 == 0:
		if len(byte) % 8 == 0:
			return (7,8)
		return (7,)
	else:
		return (8,)

def binary2Int(bin):
	return int(bin, 2)

def str2strList(array, length):
	return [array[length*x:length*(x+1)] for x in range(len(array)//length)]

# main code block
if __name__ == "__main__":
	for line in sys.stdin:
		bits = line.strip()

	length = checkLength(bits)

	asciiArray = []
	# iterates through length tuple(either 1 or 2 passes)
	# splits array into a string array of "bytes"
	for i in range(len(length)):
		asciiArray.append(str2strList(bits, length[i]))

	# iterates through all bytes in the asciiArray 
	# to convert to ASCII int
	for i in range(len(asciiArray)):
		for j in range(len(asciiArray[i])):
			asciiArray[i][j] = binary2Int(asciiArray[i][j])

	# converts each int to their ASCII representation,
	# accounting for backspace
	finalArray=[]
	for i in asciiArray:
		for j in i:
			if j == 8 and finalArray:
				finalArray.pop()
			else:
				finalArray.append(chr(j))

	

	print("".join(finalArray))
	