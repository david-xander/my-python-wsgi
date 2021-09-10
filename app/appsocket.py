import socket, select, sys
import Request

class SocketHandler:

    def __init__(self, listenfd=None):
        self.MSGLEN = 4096
        if listenfd is None:
            self.listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.listenfd = listenfd

    def connect(self, host, port):
        self.listenfd.connect((host, port))

    def send(self, msg):
        try:
            sent = self.listenfd.send(msg)
        except:
            self.listenfd.close()
    
    def receive(self):
        chunk = ""
        try:
            chunk = self.listenfd.recv(1024)
            if chunk == b'':
                self.listenfd.close()
        except:
            pass
        return chunk