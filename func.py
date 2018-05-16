import config
from paramiko import SSHClient
from scp import SCPClient
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
        'svr_uploadfile()
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
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def svr_uploadfile():
    ssh = createSSHClient(server, port, user, password)
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('example.com') 'IP Address for Server

    # SCPCLient takes a paramiko transport as an argument
    scp = SCPClient(ssh.get_transport())

    scp.put('test.txt', 'test2.txt')
    scp.get('test2.txt')

    # Uploading the 'test' directory with its content in the
    # '/home/user/dump' remote directory
    scp.put('test', recursive=True, remote_path='/home/user/dump')

    scp.close()
    print("$$ Test upload function ran.")

def cli_downloadfile():
    print("$$ Test download function ran.")
