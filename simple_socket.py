import socket

pr4e_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pr4e_socket.connect(('data.pr4e.org', 80))
request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
pr4e_socket.send(request)

while True:
    data = pr4e_socket.recv(512)

    if len(data) < 1: break
    print(data.decode(), end="")

pr4e_socket.close()