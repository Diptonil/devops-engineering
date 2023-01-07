import socket

HOST = '127.0.0.1'
PORT = 2000

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    while True:
        client_socket, address = server_socket.accept()
        print(address, "has connected.")
        client_socket.send("Hello, there!".encode())
        print(client_socket.recv(1024))
        client_socket.close()
except socket.error:
    print ("Some error has occured.")