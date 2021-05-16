# Python Socket Programming Tutorial

import socket
import threading
import translators as ts

HEADER = 64
PORT = 5050
SERVER = "192.168.1.5"
# SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            ts_dic = eval(msg)
            print(ts_dic)
            print(type(ts_dic))
            print(getattr(ts, ts_dic["provider"])(ts_dic["text"], from_language=ts_dic["from_language"], to_language=ts_dic["to_language"]))
            # # print(ts.google(msg, from_language='auto', to_language='fa'))
            #
            conn_msg = getattr(ts, ts_dic["provider"])(ts_dic["text"], from_language=ts_dic["from_language"], to_language=ts_dic["to_language"])
            conn.send(conn_msg.encode(FORMAT))
            # conn.send(ts.google(msg, from_language='auto', to_language='fa').encode(FORMAT))
            # conn.send(f"Msg received".encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


print("[STARTING] server is starting...")
start()


