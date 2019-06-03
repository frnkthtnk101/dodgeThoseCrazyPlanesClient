'''
client_handler.py
this is the skeleton 
for the client's conn-
ection to the server
'''

class client_hander:
    '''
    defines the what a session_id
    is
    '''
    def __init__(self):
        self.session_id = None
    
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
    def send():
        raise Exception('not created')