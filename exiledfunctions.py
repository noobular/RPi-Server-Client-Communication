
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