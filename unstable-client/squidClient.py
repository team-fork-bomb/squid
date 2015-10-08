#Team Fork Bomb
#Morgan Brown, Casey Freeburg, Levi Muniz, Jason Walker
import socket, loadingBar

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.21.1.222", 50709))
print("Connected")
s.send("0")
name = s.recv(1024)
s.send("I'm ready!")
size = int(s.recv(1024))
s.send("Get in my belly!")

frootloops = size/1024
rem = size%1024
steps = frootloops
print ("Size: " + str(round(size/(1024.0**2.0), 2)) + " MB")
if rem > 0:
	steps += 1

loadingbar = loadingBar.loadingBar(steps)
f = open(name, "wb")

try:
	for i in range (frootloops):
		data = s.recv(1024)
		f.write(data)
		s.send("Feed me, Semour!")
		loadingbar.stepComplete()
	data = s.recv(rem)
	f.write(data)
	loadingbar.stepComplete()
	s.close()
	f.close()
except KeyboardInterrupt:
	s.close()
	f.close()