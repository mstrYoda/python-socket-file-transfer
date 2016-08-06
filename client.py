import socket,sys , getopt

opts , args = getopt.getopt(sys.argv[1:],'f:ch',['file=','close','help'])

kapat = False

def baglan():
	s = socket.socket()
	host = socket.gethostname()
	port = 4595

	s.connect((host,port))

	if kapat:
		s.send('Close')
		s.close()
	else:
		f = open(dosya,'rb')
		l = f.read(2048)
		while(l):
			s.send(l)
			l = f.read(2048)
		f.close()
		s.close()

for opt,arg in opts:
	if opt in ('-f'):
		dosya = arg
		baglan()
	if opt in ('-c'):
		kapat = True
		baglan()
	if opt in ('-h'):
		print 'client.py -f filename //sending file \nclient.py -c //close remote server'
