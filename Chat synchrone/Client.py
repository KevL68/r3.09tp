import socket

client_socket = socket.socket()
client_socket.connect(('10.171.251.94', 15307))

while True:

    message = input("Entrez un message (pour quitter entrez 'bye') : ")
    client_socket.send(message.encode())

    reply = client_socket.recv(1024).decode()
    print("Serveur : " + reply)

    if message == "bye":
        print("Fin de la conversation.")
        client_socket.close()
        break

    if reply == "arret":
        print("Le serveur a mis fin à la conversation.")
        client_socket.close()
        break
