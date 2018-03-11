global reply
def messageCheck(data):
	global reply
	reply = ''
	if data == 'quit':
		conn.send('Terminating'.encode())
		return False
	elif data == "1":
		print("Test check 1")
		reply = 'Test Check 1'
	elif data == "2":
		print("Test check 2")
		reply = 'Test Check 2'
	else:	
		reply = 'Unknown command'
