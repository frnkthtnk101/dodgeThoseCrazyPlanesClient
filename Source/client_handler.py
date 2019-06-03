'''
client_handler.py
this is the skeleton 
for the client's conn-
ection to the server
'''
import socket
import json
from Classes.Message_ids import *
from Classes.PDU import *

class client_hander:
    '''
    defines the what a session_id
    is
    '''
    def __init__(self):
        self.session_id = None
        self.port = 80
        self.ip = '127.0.0.1'
        self.buffer_size = 4096
    
    '''
    used to create a game
    '''
    def initialize_game(self):
        raise Exception('not created')
    
    '''
    used to report a bad level given
    '''
    def send_bad_level(self):
        raise Exception('not created')
    
    '''
    used when the player dies
    '''
    def end_game(self):
        raise Exception('not created')
    
    '''
    used when the player quits
    '''
    def quit_game(self):
        raise_Exception('not created')
    
    '''
    used to get a new level
    '''
    def get_level(self):
        raise Exception('not created')

    '''
    used to send information to the machine
    '''
    def send(self, request):
        request_json = json.dumps(request)
        s = socket.socket()
        s.connect((self.ip, self.port))
        s.send(request)
        temp = s.recv(self.buffer_size)
        return json.loads(temp)

