import config
import func
from config import HOST,PORT
import socket

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
	reply = ''
	
	## When the message is recieved, input it into the messageCheck function
	if data == 'quit':
		conn.send('Terminating'.encode())
		break
	######## INPUT CHECKS HERE ##############	
	elif data == "1":
		print("Test check 1")
		reply = 'Test Check 1'
	elif data == "2":
		print("Test check 2")
		reply = 'Test Check 2'
	#########################################
	else:
		reply = 'Unknown command'


	# Sending reply
	try:
		conn.send(reply.encode())
	except Exception:
		print("Problem encoding the message...")
	
print("Shutting Down Server...")
conn.send("Server Shutdown.".encode())
conn.close() # Close connections