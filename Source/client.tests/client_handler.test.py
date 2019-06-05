'''
client_handler.test.py
Used to test out the client handler
FYI you need the server running
'''
from pathlib import Path
HOME = str(Path.home())
import unittest
import sys
sys.path.append(f'{HOME}/dodgeThoseCrazyPlanesClient/Source')
from client_handler import *

'''
class to test the client handler
'''
class client_handler_should(unittest.TestCase):
    
    '''
    set up ccreates the client_handler
    then initializes a game with the server
    '''
    def setUp(self):
        self.controller = client_hander('','easy')
        able_to_initialize = self.controller.initialize_game()
        self.method_quit = False
        if able_to_initialize is False:
            raise Exception('We were not able to initialize with server')
    
    '''
    after the test is complete, we need to
    close out the game
    '''
    def tearDown(self):
        if self.method_quit is False:
            the_game_ended = self.controller.end_game()
            if the_game_ended is False:
                raise Exception('we couldnt close the game')

    '''
    test to see if we get a level
    '''
    def test_should_get_level(self):
        we_got_a_level, data = self.controller.get_level('easy', ['downers'])
        if we_got_a_level:
            is_level_easy = data['Difficulty'] == 'easy'
            did_we_get_same_planes = data['PlaneTypes'] == ['downers']
            self.assertTrue(is_level_easy)
            self.assertTrue(did_we_get_same_planes)
        else:
            self.fail('something went wrong')

    '''
    we want to try out just quiting after initialization
    '''
    def test_should_quit_game(self):
        self.method_quit = True
        the_game_ended = self.controller.quit_game()
        self.assertTrue(the_game_ended)

    '''
    we are just telling the server we recieved a bad level
    we should get bad a level
    '''
    def test_should_get_bad_level(self):
        server_ack_ok, data = self.controller.send_bad_level([2,5], 'easy', ['downers'])
        if server_ack_ok:
            is_level_easy = data['Difficulty'] == 'easy'
            did_we_get_same_planes = data['PlaneTypes'] == ['downers']
            self.assertTrue(is_level_easy)
            self.assertTrue(did_we_get_same_planes)
        else:
            self.fail('something went wrong')

#how one starts a unit test
if __name__ == "__main__":
    unittest.main()