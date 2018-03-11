# IMPORTING 
import config
from config import HOST,PORT

import func

import socket
#####################################

try:
	#Setting up pins
	R = LED(3) #GPIOZero's version of GPIO.setup
	G = LED(4) #GPIOZero's version of GPIO.setup
	B = LED(27) #GPIOZero's version of GPIO.setup

except Exception:
	print("Failed to create LED information...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#managing error exception
try:
	global HOST, NAME
	s.bind((HOST, PORT))
except socket.error:
	print('Bind failed ')

s.listen(5)
print('Socket awaiting messages...')
	
conn, addr = s.accept()
print('Client has connected...')

# awaiting for message
while True:
	try:
		data = conn.recv(1024)
		data = str(data.decode())
	except Exception:
		print("There was a problem recieving the message...")
	print('## MESSAGE RECIEVED: ' + data)
	reply = func.messageCheck(data)
	# Sending reply
	try:
		conn.send(reply.encode())
	except Exception:
		print("Problem encoding the message...")
	
print("Shutting Down Server...")
conn.send("Server Shutdown.".encode())
conn.close() # Close connections
