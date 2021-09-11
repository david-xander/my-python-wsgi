import socket
from fork import Forker


class MyServer:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.stop_server = False

    def serve(self):
        self.listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listenfd.bind((self.host, self.port))
        self.listenfd.listen(5)
        fork = Forker()
        # while True:
            # try:
        (confd, address) = self.listenfd.accept()

        # the idea now is multithreading or multiprocess, we Fork by now
        fork.process_request(confd)

        confd.close()
        # except:
        #     self.listenfd.close()
        #     break
        if self.stop_server:
            fork.stop_all()
            # break

    def shutdown(self):
        self.stop_server = True        
        self.listenfd.close()