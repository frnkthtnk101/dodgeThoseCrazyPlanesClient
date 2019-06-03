'''
Used to test out the client handler
'''

import unittest
import sys
sys.path.append('/Users/francopettigrosso/ws/dodgeThoseCrazyPlanesClient/Source')
from client_handler import *

class client_handler_should(unittest.TestCase):
    
    def setUp(self):
        self.controller = client_hander()
        able_to_initialize = initialize_game()
        self.method_quit = False
        if able_to_initialize is False:
            raise Exception('We were not able to initialize with server')
    
    def tearDown(self):
        if self.method_quit:
            the_game_ended = end_game()
            if the_game_ended:
                raise Exception('we couldnt close the game')

    def test_should_send_bad_level(self):
        raise Exception('Not ready')

    def test_should_quit_game(self):
        raise Exception('Not ready')

    def test_should_get_level(self):
        raise Exception('Not ready')
