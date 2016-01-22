# utf-8

import socket
import time
from config import my_port

s = socket.socket()
# create a socket object
host = "127.0.0.1"
port = my_port
s.connect((host,port))


class Actor(object):
    """ define our socket actor """
    def __init__(self, _my_socket):
        self.my_socket = _my_socket

    def act(self):
        """
        Can only maintain one connection, p2p socket
        """
        count = 0
        while True:
            image_pth = r"/home/furaoing/roy_tensorflow_cv/test_samples/Male_13.jpg"
            self.my_socket.send(image_pth)
            self.my_socket.recv(1024)
            time.sleep(0.1)
            count += 1
            print(count)
        self.my_socket.close()
            

my_actor = Actor(s)
my_actor.act()
