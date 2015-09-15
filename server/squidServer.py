#Levi Muniz
#Morgan Brown
#Jason Walker
#Casey Freeburg
#Levi Muniz

'''
Something VERY experimental
'''

import socket, threading

port = 50708
threadNumber = 10
killTerm = False
Threads = []

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
			f = open("binary1600.jpg", "r")
			data = f.read()
			f.close()
			c.send(data)

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
