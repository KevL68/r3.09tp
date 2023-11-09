import socket

server_socket = socket.socket()
server_socket.bind(('10.171.251.94', 15307))
server_socket.listen(1)
conn, address = server_socket.accept()

while True:

    message = conn.recv(1024).decode()
    print("Client : ", message)

    if message == "bye":
        print("Le client est partie")
        conn.close()
        server_socket.listen(1)
        conn, address = server_socket.accept()

    else:
        reply = input("Serveur : ")
        conn.send(reply.encode())
        if reply == "arret":
            print("Fin de la conversation")
            conn.close()
            server_socket.close()
            break
