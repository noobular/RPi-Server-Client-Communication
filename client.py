import config
from config import HOST,PORT
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	command = input('Enter your command: ')
	s.send(str.encode(command))
	reply = s.recv(1024)
	if reply == lower('terminate'):
		break
	print(reply)
