import socket
import threading

host = "127.0.0.1"
port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
conn, address = server.accept()

receive_message = ""

def receive():
    global receive_message
    global conn

    while receive_message != "arret":
        receive_message = ""
        buffer = conn.recv(1024)
        receive_message = buffer.decode("utf-8")

        if receive_message == "arret":
            conn.send(receive_message.encode("utf-8"))
        elif receive_message == "bye":
            conn.send(receive_message.encode("utf-8"))
            conn, address = server.accept()
        else:
            print("RECEIVE:", receive_message)

def send():
    global receive_message

    while receive_message != "arret":
        message = input("SEND> ")
        conn.send(message.encode("utf-8"))
    

if __name__ == "__main__":
    t1 = threading.Thread(target=receive)
    t2 = threading.Thread(target=send)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    server.close()
