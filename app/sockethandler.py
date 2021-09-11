import socket, select, sys

class SocketHandler:

    def __init__(self, listenfd=None):
        self.stop_worker = False
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
        
        # if self.stop_worker:
        #     break
    
    def receive(self):
        chunk = ""
        try:
            chunk = self.listenfd.recv(1024)
            if chunk == b'':
                self.listenfd.close()
        except:
            pass

        self.send(chunk)

        # if self.stop_worker:
        #     break
    
    def process(self):
        cosa = self.receive()
        self.send( cosa )
    