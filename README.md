# Apreca

Apreca - (app • ree • sha)

Apreca is a basic open-source python3-based web server. It grabs information from a text file of the website contents and broadcasts it using HTTP protocols over a port of your choice.

## The code

*available in python file in the repo - just look slightly above this markdown

```python
#apreca
#a basic python3 web server
#Written by Aaron Duce 2018
#github.com/aaronduce

import socket

portno = input("Please provide a port number to host on")
HOST, PORT = '', portno

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    file = open("WebpageContents.txt", "r")
    http_response = file.read()
    client_connection.sendall(http_response)
    client_connection.close()
```
