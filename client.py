import socket
import config

HOST = '192.168.1.16' # Enter IP or Hostname of your server
PORT = 21012 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	command = input('Enter your command: ')
	s.send(command)
	reply = s.recv(1024)
	if reply == lower('terminate'):
		break
	print(reply)
