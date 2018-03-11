def messageCheck(data):
	if data == 'quit':
		conn.send('Terminating'.encode())
		return False
	######## INPUT CHECKS HERE ##############	
	elif data == "1":
		print("Test check 1")
	elif data == "2":
		print("Test check 2")
	#########################################
	else:
		reply = 'Unknown command'
