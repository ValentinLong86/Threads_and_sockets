import socket

host = "127.0.0.1"
port = 7777

def socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1)
        receive_message = ""

        while receive_message != "arret":
            receive_message = ""
            conn, address = server.accept()
            
            while receive_message != "arret" and receive_message != "bye":
                buff = conn.recv(1024)
                receive_message = buff.decode("utf-8")

                if receive_message == "arret" or receive_message == "bye":
                    conn.send(receive_message.encode("utf-8"))
                
                else:
                    print("RECEIVE:", receive_message)
                    
                    message = input("SEND> ")
                    conn.send(message.encode("utf-8"))
        
        server.close()


if __name__ == "__main__":
    socket_server()