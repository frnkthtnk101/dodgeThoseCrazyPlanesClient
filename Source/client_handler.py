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
from Classes.bad_levels import *

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
        self.version = (56).to_bytes(1,byteorder= 'big')
    
    '''
    used to create a game
    '''
    def initialize_game(self):
        init_pdu = PDU(Message_ids.INTIALIZE_GAME, None, (56).to_bytes(1, byteorder = 'big'), None)
        response = self.send(init_pdu)
        good_response = response['Message'] == Message_ids.RECEIVE_SESSION_ID.value
        if good_response:
            self.session_id = response['SessionId']
            return True
        return False
    
    '''
    used to report a bad level given
    '''
    def send_bad_level(self, reasons):
        bad_levels_pdu = PDU(Message_ids.BAD_LEVEL, self.session_id, self.version, reasons)
        response = self.send(bad_levels_pdu)
        good_response = response['MessageId'] == Message_ids.RECEIVE_LEVEL.value
        return good_response, response['Data']
    
    '''
    used when the player dies
    '''
    def end_game(self):
        end_game_pdu = PDU(Message_ids.END_GAME, self.session_id, self.version, None)
        response = self.send(end_game_pdu)
        good_response = response['MessageId'] == Message_ids.OK.value
        return good_response
    
    '''
    used when the player quits
    '''
    def quit_game(self):
        end_game_pdu = PDU(Message_ids.END_GAME, self.session_id, self.version, None)
        response = self.send(end_game_pdu)
        good_response = response['MessageId'] == Message_ids.OK.value
        return good_response
    
    '''
    used to get a new level
    '''
    def get_level(self, difficulty, plane_types):
        data = {'Difficulty' : difficulty, 'PlaneTypes' : plane_types}
        get_level_pdu = PDU( Message_ids.GET_LEVEL, self.session_id, self.version, data)
        response = self.send(get_level_pdu)
        good_response = response['MessageId'] == Message_ids.RECEIVE_LEVEL.value
        return good_response, response['Data'] 

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
