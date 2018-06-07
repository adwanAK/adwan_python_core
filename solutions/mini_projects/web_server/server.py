'''
Build a small web server following the first part of the tutorial at:
https://ruslanspivak.com/lsbaws-part1/

'''

import socket


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f"Serving HTTP on port {PORT}...")

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = b"""
HTTP/1.1 200 OK

Hei there everyone!
"""

    client_connection.sendall(http_response)
    client_connection.close()
