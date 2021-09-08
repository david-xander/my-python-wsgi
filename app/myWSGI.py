#!/usr/bin/env python
import socket


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    host_and_port = (socket.gethostname(), port)

    # bind the socket to a public host, and a well-known port
    my_socket.bind(host_and_port)

    # become a server socket
    my_socket.listen(5)

    # while True:
    #     # accept connections from outside
    #     (clientsocket, address) = my_socket.accept()
    #     # now do something with the clientsocket
    #     # in this case, we'll pretend this is a threaded server
    #     ct = client_thread(clientsocket)
    #     ct.run()

if __name__ == '__main__':
    main()
