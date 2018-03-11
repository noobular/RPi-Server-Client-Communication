print("Config Imported...")
## Importing
import socket
from gpiozero import LED
global HOST, PORT

def init():
	print("Config Being Initialized...")
	global HOST, PORT
	## Server IP / Hostname
	HOST = '192.168.1.16' 
	## Open Port
	PORT = 21012 
	print("Config Initialized...")


init()