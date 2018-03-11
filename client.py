import config
from config import HOST,PORT
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	message = input('>#> ')
	s.send(message.encode())
	reply = s.recv(1024)
	if reply == 'terminate':
		break
	print(reply.decode())
