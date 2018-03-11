import config

def messageCheck(check):
    reply = ''
    if check == 'quit':
        conn.send('Terminating'.encode())
        return False
    ##======INPUT CHECKS HERE=======##
    elif check == "1":
        print("Test check 1")
        reply = 'Test Check 1'
    elif check == "2":
        print("Test check 2")
        reply = 'Test Check 2'
    ##^============================^##
    else:   
        reply = 'Unknown command'
    return reply

