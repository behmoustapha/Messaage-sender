import socket
import sys

serv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 2110))
serv.listen(1)
try : 
    client, addr = serv.accept()
    data = client.recv(1024).decode()
    try :
        print("Invité: ", data)
        client.send(input("Votre message : ").encode())

    except KeyboardInterrupt:
        print("Arrêt du server")
        serv.close()
        sys.exit(0)
except ConnectionResetError:
    print("Connexion interrompue par le client")
    serv.close()
    sys.exit(0)

except ConnectionAbortedError:
    print("Connexion interrompue par le client")
    serv.close()
    sys.exit(0)