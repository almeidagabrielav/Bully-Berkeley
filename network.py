import socket

class Network:

    _MAX_PACKET_SIZE = 1000000

    def __init__(self, host = 'localhost', port = 8000):
        self.NetworkSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.NetworkSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.NetworkSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.NetworkSocket.settimeout(10)
        self.NetworkSocket.bind((host, port))
        self.DEFAULT_HOST = host
        self.DEFAULT_PORT = port

    def send(self, data, address = False, ip = False):
        if address == False:
            if ip == False:
                address = ('<broadcast>', self.DEFAULT_PORT)
            else:
                address = (ip, self.DEFAULT_PORT)
        self.NetworkSocket.sendto(data, address)
        return True

    def recv(self):
        return self.NetworkSocket.recvfrom(self._MAX_PACKET_SIZE)