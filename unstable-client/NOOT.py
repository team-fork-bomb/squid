import socket, loadingBar

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 50709))
print("Connected")
s.send("0")
name = s.recv(1024)
print(name)
size = int(s.recv(1024))
print(str(size))

frootloops = size/1024
print(frootloops)
rem = size%1024
print(rem)
steps = frootloops
if rem > 0:
	steps += 1
print(steps)

loadingbar = loadingBar.loadingBar(steps)
f = open(name, "wb")
s.recv(1024)
try:
	for i in range (frootloops):
		data = s.recv(1024)
		f.write(data)
		loadingbar.stepComplete()
	print("\nExit frootloops")
	data = s.recv(rem)
	f.write(data)
	loadingbar.stepComplete()
	s.recv(1024)
	s.close()
	f.close()
except KeyboardInterrupt:
	s.close()
	f.close()