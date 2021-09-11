from sockethandler import SocketHandler
import threading
import time

class Forker:

    def __init__(self) -> None:
        self.workers = []
    
    def process_request(self, clientsocket):
        ms = SocketHandler(clientsocket)
        worker = threading.Thread(target=ms.process, daemon=True)
        self.workers.append(worker)
        worker.start()

    def stop_all(self):
        for worker in self.workers:
            worker.stop_worker=True
            worker.join()