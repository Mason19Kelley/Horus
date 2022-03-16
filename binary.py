import sys

# decides whether input is 7 bit or 8 bit ASCII
# returns tuple of (7), (8), or (7,8)
def checkLength(byte):
	if len(byte) % 7 == 0:
		if len(byte) % 8 == 0:
			return (7,8)
		return (7)
	else:
		return (8)


# main code block
if __name__ == "__main__":
	for line in sys.stdin:
		bits = line.strip()

	length = checkLength(bits)

	# iterates through length tuple(either 1 or 2 passes)
	for i in length:
		pass
	

