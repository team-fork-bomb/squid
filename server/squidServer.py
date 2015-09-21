
#Team Fork Bomb
#Morgan Brown, Nicholas Coiner, Casey Freeburg, Levi Muniz, Jason Walker
import os
v = "Team Fork Bomb\nCasey Freeburg, Jason Walker, Levi Muniz, Morgan Brown, Nicholas Coiner"
print(v)

import socket, threading

print ("Welcome to Squid - server")

port = 50709
threadNumber = 10
killTerm = False
Threads = []
VM = ["Anime 404.mp4","binary1600.jpg"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(5)

def clientConn():
	global killTerm
	while killTerm == False:
		c, addr = s.accept()
		if c and killTerm == False:
			c.settimeout(60)
			c.send("\033[1;32mConnected\033[0m\n")
			ip, port = addr
			addr = None
			port = None
			print("\033[1;32mConnection established with: " + ip + "\033[0m")
			cli_data = c.recv(1024)
			try:
				x = os.path.getsize(VM[int(cli_data)])
				loops = x/1024
				rem = x%1024
				f = open(VM[int(cli_data)], "r")
				for i in range(loops):
					f.seek(1024,1)
					data = f.read()
			        f.close()
			        c.send(data)
			except:
			    c.send("Recieved a request that the server could not understand.")

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
