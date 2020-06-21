import socket
s=socket.socket()
s.connect(("localhost",4100))
fname = input("enter file name: ")
s.send(fname.encode())
content = s.recv(1024)
print(content.decode())
s.close()