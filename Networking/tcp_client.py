import socket

HOST = '127.0.0.1'
PORT = 2000

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(client_socket.recv(1024).decode())
    client_socket.send("Nice to meet you!".encode())
    client_socket.close()
except socket.error:
    print("Some error has occured.")