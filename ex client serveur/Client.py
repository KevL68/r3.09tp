import socket

#Code client
client_socket = socket.socket()
client_socket.connect(('10.128.4.43',6253))

while True:
    message = input("Entrez un message (pour quitter entrez 'bye') : ")
    client_socket.send(message.encode())

    if message == "bye":
        print("Fin de la conversation.")
        break

    reply = client_socket.recv(1024).decode()
    print("Message du serveur : " + reply)

client_socket.close()