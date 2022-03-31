from ftplib import FTP

IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True
METHOD = 10


ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)



ftp.cwd(FOLDER)
if METHOD == 7:
	ftp.cwd("7")
elif METHOD == 10:
	ftp.cwd("10")
files = []
ftp.dir(files.append)
ftp.quit()

# convert each char in perms to either 0 or 1
def perm2bin(code:str):
	new = []
	for i in code:
		if i == "-":
			new.append("0")
		else:
			new.append("1")
	return "".join(new)


# gets necesarry information from files then sorts and isolates perms
files = [[i.split()[8],i.split()[0]] for i in files]	
files.sort()
files = [i[1] for i in files]

# remove unneeded values if only looking at 7 bits or join 10 bit values
if METHOD == 7:
	files = [i for i in files if i[0:3] == "---"]
elif METHOD == 10:
	files = "".join(files)

# converts each string of perms to binary
files = list(map(perm2bin, files))


if METHOD == 10:
	files = [files[7*x:7*(x+1)] for x in range(len(files)//7)]
	for i,v in enumerate(files):
		files[i] = "".join(v)
# converts binary to chars and creates string
files = "".join([chr(int(i, 2)) for i in files])

print(files)
