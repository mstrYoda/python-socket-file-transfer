import socket

s = socket.socket()

port = 4595
host = socket.gethostname()

s.bind((host,port))

s.listen(1)

while True:
	c,addr = s.accept()
	print 'got connection from' , addr
	f = open('received.jpeg','wb') 
	
	gelen = c.recv(2048)
	if gelen == 'Close':
			print 'Server shutting down by client..'
			break
	while (gelen):
			f.write(gelen)
			gelen = c.recv(2048)

	c.close()
	f.close()
	s.close()
	break
		


