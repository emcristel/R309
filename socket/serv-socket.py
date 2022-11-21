import socket

server_socket = socket.socket() #création de socket
server_socket.bind(('localhost', 10000)) #association du host(@IP)
print("Serveur démarré...")
server_socket.listen(1)
conn, address= server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
conn.clos()