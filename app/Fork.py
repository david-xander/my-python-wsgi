from appsocket import SocketHandler

class Fork:
    def __init__(self, clientsocket) -> None:
        self.clientsocket = clientsocket
    def proces_request(self):
        ms = SocketHandler(self.clientsocket)
        cosa = ms.receive()
        ms.send(cosa)