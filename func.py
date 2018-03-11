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
def messageCheck(check):
    reply = ''
    if check == 'quit':
        conn.send('Terminating'.encode())
        return False
    ##======INPUT CHECKS HERE=======##
    elif check == "upload":
        print("Attempting to upload data...")
        svr_uploadfile()
        reply = 'Server Attempting to upload file ....'
    elif check == "download":
        print("Attempting to send data to client")
        cli_downloadfile()
        reply = 'Server Attempting to send data...'
    ##^============================^##
    elif check == "help" or check == "commands":
        print("Sending Help Information")
        reply = 'Possible commands:' + possibleCommands
    else:   
        reply = 'Unknown command'
    return reply




### ADD YOUR FUNCTIONS AFTER THIS LINE ###

def svr_uploadfile():
    print("Test upload function")

def cli_downloadfile():
    print("Test download function")