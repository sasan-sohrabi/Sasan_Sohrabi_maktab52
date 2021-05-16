import socket
import pickle

HEADER = 64
PORT = 5050
SERVER = "192.168.1.5"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# send("HELLO World!")
# send("Hello everyone!")
# send(DISCONNECT_MESSAGE)
provider = ['google', 'deepl', 'bing', 'alibaba']
info_dic = {}
info_dic["text"] = input("Enter text: ")
info_dic["provider"] = input("Enter Provider: ")
# if not info_dic["provider"] in provider:
#     raise ValueError("Please Enter valid provider!")
info_dic["from_language"] = input("Enter from_language: ")
info_dic["to_language"] = input("Enter to_language: ")
send(f'{info_dic}')

