import socket
import sys

host = "127.0.0.1"
port = 7777

def socket_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((host, port))
        except ConnectionRefusedError:
            print("Le serveur n'accepte pas la connexion ou est indisponible")
            sys.exit(0)
        except:
            print("Erreur de communication avec le serveur ")
            sys.exit(0)

        message = ""

        while message != "arret" and message != "bye":
            message = input("SEND> ")
            client.send(message.encode("utf-8"))

            buffer = client.recv(1024)
            receive_message = buffer.decode("utf-8")

            print("RECEIVE:", receive_message)

        client.close()


if __name__ == "__main__":
    socket_client()