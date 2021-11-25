import socket
s=socket.socket()
host = socket.gethostname()
port=12345
s.bind(('',port))
s.listen(5)
while True:
    s,addr=s.accept()
    print("got connection from",addr)
s.send("thank you for connection")
s.close()
