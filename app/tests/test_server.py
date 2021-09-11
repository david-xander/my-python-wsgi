from os import name
from myserver import MyServer
import unittest, socket
import threading
import time

class MouckUpServer:
    def __init__(self) -> None:
        self.address = "127.0.0.1"
        self.port = 8000
        self.server = MyServer(self.address, self.port)
        self.server.serve()
    
    def shutdown(self):
        self.server.shutdown()

class MouckUpClient:
    def __init__(self) -> None:
        self.address = "127.0.0.1"
        self.port = 8000     
        self.direccion = (self.address, self.port)

    def connect(self):
        self.listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.listenfd.connect_ex((self.address, self.port))


class TestServer(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.server = None
    #     self.stop_thread = False
    #     self.oneworker = threading.Thread(
    #         target=self.worker,
    #         name="my_mockup_server", 
    #         args=(id, lambda: self.stop_thread), 
    #         daemon=True)
    #     self.oneworker.start()

    # def worker(self, id, stop_thread):
    #     while True:
    #         if self.server == None:
    #             self.server = MouckUpServer()
    #         elif stop_thread:
    #             self.server.shutdown()
            
    # def tearDown(self) -> None:
    #     self.stop_thread = True
    #     self.oneworker.join(1)


    def test_server_port_is_opened(self):
        time.sleep(0.3)
        c = MouckUpClient()
        self.assertEqual(0, c.connect())
        c.listenfd.close()

    def test_sending_echo_a(self):
        time.sleep(0.3)
        c = MouckUpClient()
        c.connect()
        sent = c.listenfd.send("ECHO A".encode())
        self.assertEqual('ECHO A', c.listenfd.recv(1024).decode())
        c.listenfd.close()
    

if __name__ == '__main__':
    unittest.main()