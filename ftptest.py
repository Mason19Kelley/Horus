from ftplib import FTP

####################################################
# Group Name: Team Horus
# Group Members: Clay H., Anassas A., Jimmy B., Chance H., Mason K., Patrick M., Johnathon T.
# Date: March 25, 2022
# Description: Program #1: Binary Decoder
####################################################

# default global variables
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True
METHOD = 10


# ftp connection methods
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)


# changes pwd in ftp server to correct directory depending on METHOD var
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

# if using 10 bit method, divide up the bits into 7 bit increments
if METHOD == 10:
	files = [files[7*x:7*(x+1)] for x in range(len(files)//7)]
	for i,v in enumerate(files):
		files[i] = "".join(v)
# converts binary to chars and creates string
files = "".join([chr(int(i, 2)) for i in files])

print(files)
