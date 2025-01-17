import socket

host='localhost'
port=4100
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Server listening on port: ",port)
s.listen(1)
c,addr=s.accept()
filename=c.recv(1024)
try:
    f = open(filename,'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"file not found")
c.send("Bye".encode())