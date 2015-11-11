#Team Fork Bomb
#Morgan Brown Casey Freeburg, Levi Muniz, Jason Walker
import os, socket, threading
v = "Team Fork Bomb\nCasey Freeburg, Jason Walker, Levi Muniz, Morgan Brown"
print(v)

print ("Welcome to Squid - server")

port = 50709
threadNumber = 10
killTerm = False
Threads = []
VM = os.listdir(".")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(5)

def sendFile(theFile):
	try:
		x = os.path.getsize(theFile) #get size
		c.send(theFile) #name
		c.recv(1024)
		c.send(str(x)) #size
		c.recv(1024)
		loops = x/1024
		rem = x%1024
		f = open(theFile, "rb")
		for i in range(loops):
			data = f.read(1024) #data
			c.send(data)
			c.recv(1024)
		data = f.read(rem)
		c.send(data)
		f.close()
	except:
		c.send("Recieved a request that the server could not understand.")

def clientConn():
	global killTerm
	global VM
	while killTerm == False:
		c, addr = s.accept()
		if c and killTerm == False:
			c.settimeout(60)
			ip, port = addr
			addr = None
			port = None
			print("\033[1;32mConnection established with: " + ip + "\033[0m")
			cli_data = c.recv(1024)
			if cli_data == "$List$":
				c.send(str(VM))
			else:
				sendFile(cli_data)
					

try:
	for i in range (threadNumber):
		connThread = threading.Thread(target=clientConn)
		connThread.start()
		Threads.append(connThread)
		print("\033[1;32mThread " + str(i+1) + " started!\033[0m")
	while True:
		raw_input("")

except KeyboardInterrupt:
	print("\n\033[1;31mKilling!\033[0m")
	killTerm = True
	for i in Threads:
		s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s2.connect(("", port))
		s2.shutdown(socket.SHUT_RDWR)
		s2.close
	try:
		s.shutdown(socket.SHUT_RDWR)
		s.close()
	except:
		pass
	exit()