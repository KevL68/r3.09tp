#Code serveur
server_socket = socket.socket()
server_socket.bind(('10.171.251.168', 6253))
server_socket.listen(1)
conn, address = server_socket.accept()
message = conn.recv(1024).decode()
conn.send(reply.encode())
conn.close()
server_socket.close()