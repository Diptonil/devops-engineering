import socket

HOST = '127.0.0.1'
PORT = 2000

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(server_socket.recvfrom(1024).decode())
    server_socket.sendto("Hello from server!".encode(), (HOST, PORT))
    server_socket.close()
except socket.error:
    print("Some error occured.")
