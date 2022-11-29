import socket
import sys
import threading

host = "127.0.0.1"
port = 7777

conn = ""

def socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1)
        message = ""

        while message != "arret":
            message = ""
            conn, address = server.accept()
            while message != "bye" and message != "arret":
                buffer = conn.recv(1024)
                message = buffer.decode("utf-8")

                print("RECEIVE:", message)
        server.close()

def send_message():
    send_message = input("SERVER> ")
    conn.send(send_message.encode("utf-8"))



if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1)
        message = ""

        while message != "arret":
            message = ""
            conn, address = server.accept()
            while message != "bye" and message != "arret":
                buffer = conn.recv(1024)
                message = buffer.decode("utf-8")

                print("RECEIVE:", message)
        server.close()