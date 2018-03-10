import socket               

s = socket.socket()        
host = '10.91.25.74'# ip of raspberry pi 
port = 12345               
s.connect((host, port))
print(s.recv(1024))
s.close()