import config
'''
    This is how you would add a comment to the check..
    elif check == "recieved message":
        print("Print to the server console")
        reply = 'Print to the client'
        #Any other functions you'd like to add here.
'''
## This is a list of all the commands you've got listed.
possibleCommands = "upload, download, help, commands."

## Message Check function; Checks the messages that are recieved by the server.
def messageCheck(check):
    reply = ''
    if check == 'quit':
        conn.send('Terminating'.encode())
        return False
    ##V=====INPUT CHECKS HERE======V##
    elif check == "upload":
        print("$$ Attempting to upload data...")
        svr_uploadfile()
        reply = 'Server Attempting to upload file ....'
    elif check == "download":
        print("$$ Attempting to send data to client")
        cli_downloadfile()
        reply = 'Server Attempting to send data...'
    ##^============================^##
    elif check == "help" or check == "commands":
        print("$$ Sending Help Information")
        reply = 'Possible commands:' + possibleCommands
    else:   
        reply = 'Unknown command'
    return reply

### ADD YOUR FUNCTIONS AFTER THIS LINE ###

def svr_uploadfile():
    print("$$ Test upload function ran.")

def cli_downloadfile():
    print("$$ Test download function ran.")