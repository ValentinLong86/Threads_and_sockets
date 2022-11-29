import socket 
import threading
import sys

host = "0.0.0.0"
port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

receive_message = ""
ipAddress = ""


def thread_socket(conn, ip, port):
    print(f"[+] Nouveau thread démarré pour {ip}:{port}")
    global receive_message
    global ipAddress
    
    receive_message = ""

    while receive_message != "arret" and receive_message != "bye":
        buffer = conn.recv(2048)
        receive_message = buffer.decode("utf-8")
        ipAddress = ip

    conn.send(receive_message.encode("utf-8"))

def sendToALL(conn, ip):
    rc = ""
    while True:
        if receive_message != rc and ip != ipAddress:
            msgToSendToALL = f"{ipAddress}: {receive_message}"
            conn.send(msgToSendToALL.encode("utf-8"))
            rc = receive_message


if __name__ == "__main__":
    mythreads = [] 

    while receive_message != "arret":
        server.listen(5)
        (conn, (ip,port)) = server.accept()
        thread = threading.Thread(target=thread_socket, args=[conn, ip, port])
        thread2 = threading.Thread(target=sendToALL, args=[conn, ip])
        thread.start()
        thread2.start()
        mythreads.append(thread)
        mythreads.append(thread2)

    for t in mythreads: 
        t._stop
