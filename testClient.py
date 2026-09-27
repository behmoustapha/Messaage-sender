import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2110))


try :
    data = client.recv(1024).decode()
    try :
        print("Invité: ", data) 
        client.send(input("Votre message : ").encode())

    except KeyboardInterrupt:
        print("Arrêt du client")
        client.close()
        sys.exit(0)
except ConnectionResetError:
    print("Connexion interrompue par l'invité")
    client.close()
    sys.exit(0)

except ConnectionAbortedError:
    print("Connexion interrompue par l'invité")
    client.close()
    sys.exit(0)