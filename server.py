import socket
from gpiozero import LED #conversion from GPIO to GPIOZero

R = LED(3) #GPIOZero's version of GPIO.setup
G = LED(4) #GPIOZero's version of GPIO.setup
B = LED(27) #GPIOZero's version of GPIO.setup

s = socket.socket()
host = '10.91.27.24' #ip of raspberry pi
port = "22"
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  R.on()
  c.send('Thank you for connecting')
  c.close()