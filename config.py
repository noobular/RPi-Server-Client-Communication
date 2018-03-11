print("Config Imported...")
## Importing
import socket
from gpiozero import LED
global HOST, PORT
HOST = '192.168.1.16' # Server IP or Hostname
PORT = 21012 #Pick an open Port (1000+ recommended), must match the client sport


