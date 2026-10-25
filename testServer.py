import socket
import sys
import threading


serv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 2110))
serv.listen(1)
client, addr = serv.accept()

def nm():
    global pseudo
    name = input("Comment vous appelez vous ?: ")
    if name == "":
        while name =="":
            name = input("Comment vous appelez vous ?: ")
    client.send(name.encode())


    data = client.recv(1024).decode()
    pseudo = data
    print("Nom du client: ", pseudo)


def receive():
    try:
        data = client.recv(1024).decode()
        att = data.split(".", 1)
        count = int(att[0])
        message = att[1]
        print(f"{pseudo}: {message}")
        oldcount = count
        while True:
            data = client.recv(1024).decode()
            att = data.split(".", 1)
            count = int(data[0])
            message = att[1]
            if count == oldcount:
                pass
            else:
                print(f"{pseudo}:{message}")
    except (KeyboardInterrupt, ConnectionAbortedError, ConnectionResetError) as e:
        print("Connexion interrompue: ", e)
        client.close()
        sys.exit(0)


def send():
    count = 0
    while True:
        count += 1
        client.send(f"{count}. {input()}".encode())

messg = threading.Thread(target=receive, daemon=True)

try:
    nm()
    messg.start()
    send()
except (KeyboardInterrupt, ConnectionAbortedError, ConnectionResetError) as e:
        print("Connexion interrompue", e)
        client.close()
        sys.exit(0)
