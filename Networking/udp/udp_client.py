import socket

HOST = '127.0.0.1'
PORT = 2000

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto("Hello from client!".encode(), (HOST, PORT))
    print(client_socket.recvfrom(1024).decode())
    client_socket.close()
except socket.error:
    print(socket.error)