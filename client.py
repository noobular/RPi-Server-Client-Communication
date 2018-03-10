import socket               

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = s.gethostname()
port = 22
s.bind((host, port))
     
s.connect((host, port))
print(s.recv(1024))
s.close()