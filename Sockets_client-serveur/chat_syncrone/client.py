import socket
import sys

host = "127.0.0.1"
port = 7777

def socket_client(message: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((host, port))
            client.sendall(message.encode("utf-8"))
        except ConnectionRefusedError:
            return -1
        except:
            return -2

        if message == "bye" or message == "arret":
            client.close()
            sys.exit(0)

        buffer = client.recv(1024)
        message = buffer.decode("utf-8")

    return message


if __name__ == "__main__":
    while True:
        message = input("SEND> ")

        if socket_client(message) == -1:
            print("Le serveur n'accepte pas la connexion ou est indisponible")
        elif socket_client(message) == -2:
            print("Erreur de communication avec le serveur ")
        else:
            print("RECEIVE:", socket_client(message))
