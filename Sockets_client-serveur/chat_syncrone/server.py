import socket
import sys

host = "127.0.0.1"
port = 7777

def socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1)

        while True:
            conn, address = server.accept()
            while True:
                buffer = conn.recv(1024)
                message = buffer.decode("utf-8")

                print("RECEIVE:", message)
                    
                if message == "arret":
                    server.close()
                    sys.exit(0)
                elif message == "bye":
                    break
                
                send_message = input("SERVER> ")
                conn.send(send_message.encode("utf-8"))


if __name__ == "__main__":
    socket_server()
