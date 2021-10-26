import socket

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

print('My IP Address is: ' + ipAddress)