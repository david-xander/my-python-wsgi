#!/usr/bin/env python
from server import Server

def do_something(client_socket):
    pass

def main():
    server = Server('127.0.0.1', 8000)
    server.serve()


if __name__ == '__main__':
    main()
