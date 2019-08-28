import socket


class HTTPServer:
    def __init__(self):
        self.__address = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        self.__socket = socket.socket()
        self.__socket.bind(self.__address)
        self.__socket.listen(1)

    def handle(self, callback):
        client, address = self.__socket.accept()
        # stream = client.makefile('rwb', 0)
        response = callback()
        client.send(response)
        client.close()
