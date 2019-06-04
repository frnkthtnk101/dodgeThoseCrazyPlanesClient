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
        able_to_initialize = self.controller.initialize_game()
        self.method_quit = False
        if able_to_initialize is False:
            raise Exception('We were not able to initialize with server')
    
    def tearDown(self):
        if self.method_quit:
            the_game_ended = self.controller.end_game()
            if the_game_ended:
                raise Exception('we couldnt close the game')

    def test_should_send_bad_level(self):
        we_got_a_level, data = self.controller.get_level('easy', ['downers'])
        if we_got_a_level:
            is_level_easy = data['Difficulty'] == 'easy'
            did_we_get_same_planes = data['PlaneTypes'] == ['downers']
            self.assertTrue(is_level_easy)
            self.assertTrue(did_we_get_same_planes)
        else:
            self.fail('something went wrong')

    def test_should_quit_game(self):
        self.method_quit = True
        the_game_ended = self.controller.end_game()
        self.assertTrue(the_game_ended)

    def test_should_get_level(self):
        server_ack_ok, data = self.controller.end_bad_level([2,5], 'easy', ['downers'])
        if server_ack_ok:
            is_level_easy = data['Difficulty'] == 'easy'
            did_we_get_same_planes = data['PlaneTypes'] == ['downers']
            self.assertTrue(is_level_easy)
            self.assertTrue(did_we_get_same_planes)
        else:
            self.fail('something went wrong')


if __name__ == "__main__":
    unittest.main()