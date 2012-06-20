import socket

class handmade_socket:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sock_connect(self, host, port):
        self.sock.connect((host, port))

    def sock_send(self, msg):
        self.sock.send(msg)

    def sock_receive(self):
        return self.sock.recv(1024)

    def sock_close(self):
        self.sock.close()
