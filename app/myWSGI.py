from myserver import MyServer
import signal
import sys

myserver = None

def signal_handler(sig, frame):
    print('Exiting!')
    global myserver
    myserver.shutdown()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')
    global myserver 
    myserver = MyServer('127.0.0.1', 8000)
    myserver.serve()
    signal.pause()


if __name__ == '__main__':
    main()
