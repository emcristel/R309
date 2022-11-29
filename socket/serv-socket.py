import socket
message = "rien"
data = "rien"

server_socket = socket.socket() #création de socket
server_socket.bind(('127.0.0.1', 10000)) #association du host(@IP)
print("Serveur démarré...")
server_socket.listen(1) #Attente de la connexion et nombre de connexion établie

while message != "kill" and data!="kill":
    conn, address= server_socket.accept() #Etablissement de la communication
    
    while message != "quit" and message!="kill" and data!= "quit" and data!="kill":
        data = conn.recv(1024).decode() #Réception de données
        print(f"Message reçu : {data}")
        message = input("que voulez-vous envoyer : ")
        print("Message envoyé... en attente d'une réponse")
        conn.send(message.encode()) #Envoi de données
    
    conn.close() #Fermeture de la communication
    sortie = input("voulez vous quitter ? (y/n) : ")
    if sortie == "y" or message == "kill":
        connexion == "0" 