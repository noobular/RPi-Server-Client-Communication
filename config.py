print("Config Imported...")
## Importing
import socket
from gpiozero import LED

def initialize():
	global HOST, PORT
	## Server IP / Hostname
	HOST = '192.168.1.16' 
	## Open Port
	PORT = 21012 
