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
            except:
                print("Erreur de communication avec le serveur ")
            else:
                while True:
                    send_message = input("CLIENT> ")
                    client.send(send_message.encode("utf-8"))
                    
                    if send_message == "bye" or send_message == "arret":
                        client.close()
                        sys.exit(0)

                    buffer = client.recv(1024)
                    rc_message = buffer.decode("utf-8")

                    print("RECEIVE:", rc_message)


if __name__ == "__main__":
    socket_client()
