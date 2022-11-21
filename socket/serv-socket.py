import socket
message = "rien"

server_socket = socket.socket() #création de socket
server_socket.bind(('localhost', 10000)) #association du host(@IP)
print("Serveur démarré...")
server_socket.listen(1) #Attente de la connexion et nombre de connexion établie

connexion = input("Menu général, que voulez-vous faire ?\n1. Etablir connexion avec client \n2. Quitter\n")

while connexion ==1:
    conn, address= server_socket.accept() #Etablissement de la communication
    
    while message != "quit":
        data = conn.recv(1024).decode() #Réception de données
        print(f"Message reçu : {data}")
        message = input("que voulez-vous envoyer : ")
        print("Message envoyé... en attente d'une réponse")
        conn.send(reply.encode()) #Envoi de données
    
    conn.close() #Fermeture de la communication
    sortie = input("voulez vous quitter ? (y/n) : ")
    if sortie == "y" or message == "quit":
        connexion == "0" 