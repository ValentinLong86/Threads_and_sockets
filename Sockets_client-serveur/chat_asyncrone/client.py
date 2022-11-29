import socket
import threading

host = "127.0.0.1"
port = 7777

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive(client):
    message = ""

    while message != "arret" and message != "bye":
        message = input("SEND> ")
        client.send(message.encode("utf-8"))

def send(client):
    receive_message = ""

    while receive_message != "arret" and receive_message != "bye":
        buffer = client.recv(1024)
        receive_message = buffer.decode("utf-8")

        print("RECEIVE:", receive_message)


if __name__ == "__main__":
    t1 = threading.Thread(target=receive, args=[client])
    t2 = threading.Thread(target=send, args=[client])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    client.close()
