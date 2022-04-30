import sys

# opens key file and reads is
file = open("key2","rb")
k = file.read()
file.close()

#opens ciphertext file from stdin
m = bytearray(sys.stdin.buffer.read())

l = len(k)
result=[]
# xor's each bit in each file
for i in range(len(m)):
	h = k[i%l]
	result.append(m[i] ^ h)
#writes the output to stdout
sys.stdout.buffer.write(bytearray(result))
