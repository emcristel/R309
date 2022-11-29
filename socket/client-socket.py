import socket


client_socket = socket.socket() #Création de la socket
client_socket.connect(('localhost', 10000)) #Connexion au host et au port host = "@IP" -> localhost
print("Connexion établie...")

message = "" #message saisit par utilisateur et envoyé
data = "" #ce qui est reçu par l'utilisateur du serveur
menu = input("Menu général, que voulez-vous faire ?\n1. Envoyer un message\n2. Quitter\n")


if menu == "1" : # Si demande d'envoi de message, ouverture d'une boucle

    while message != "quit" and message != "bye" and data != "bye" and data != "quit": #Création boucle pour laisser connexion ouverte tant que != de quit ou bye
        message = input("que voulez-vous envoyer : ")
        print("Message envoyé... en attente d'une réponse")
        client_socket.send(message.encode()) #Envoi de données
        data = client_socket.recv(1024).decode() #Réception de données
        print(f"Message reçu : {data}")
    client_socket.close() #Fermeture de la communication

    sortie = input("voulez vous quitter ? (y/n) : ")
    if sortie == "y" or message == "kill":
        connexion == "0" 