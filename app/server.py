import socket
from Fork import Fork


class Server:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def serve(self):
        self.listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listenfd.bind((self.host, self.port))
        self.listenfd.listen(5)

        while True:
            try:
                (confd, address) = self.listenfd.accept()

                # the idea now is multithreading and multiprocess, we Fork by now
                ct = Fork(confd)
                ct.proces_request()

                confd.close()
            except:
                self.listenfd.close()
                break

    def shutdown(self):
        self.listenfd.close()