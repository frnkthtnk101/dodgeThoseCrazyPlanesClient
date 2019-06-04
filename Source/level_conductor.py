import pygame
from classes import *

from client_handler import *

class level_conductor:
    def __init__(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.stars_list= pygame.sprite.Group()
        self.bad_list=pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.hero = TheGUY()
        self.total_deployed = 0
        self.handler = client_handler()

    def add_objects_to_list(self):
        self.all_sprites_list.add(self.hero)
        self.block_list.add(self.hero)
        for i in range(50):
            stars= star()
            self.all_sprites_list.add(stars)
            self.stars_list.add(stars)
        for i in range(5):
            badGuy = bad_guy()
            self.all_sprites_list.add(badGuy)
            self.bad_list.add(badGuy)
            self.block_list.add(badGuy)
    
    def plane_collides(self):
        return pygame.sprite.spritecollide(
            self.hero,
            self.block_list,
            False
            )
    
    def initialize_connection_with_server(self):
        return self.handler.initialize_game()
    
    def get_a_level(self):
        good, temp_data = self.handler.get_level('easy',['downers'])
        if good:
            correct_difficulty = (temp_data['Difficulty'] == 'easy') == False
            correct_planes = (temp_data['PlaneTypes'] == ['Downers']) == False
            is_anything_incorrect = correct_difficulty or correct_planes
            if is_anything_incorrect:
                Reasons = [] 
                if correct_difficulty == False:
                    Reasons.append(5)
                if correct_planes == False:
                    Reasons.append(2)
                good, temp_data = self.handler.send_bad_level(Reasons,'easy',['downers'])
        self.level = temp_data

    def update_total_deployed(self):
        j = 0
        for i in self.bad_list:
            if i.deployed:
                j += 1
        return j

    def update_objects(self, frame_number):
        self.stars_list.update()
        self.hero.mous_pos()
        more_waves = len(self.level['level']) > 0
        same_frame = frame_number == self.level['level'][0]['tick']
        if more_waves and same_frame:
            information = self.level['level'].pop(0)
            #see the type and number
            same_enemies = information["enemies"] == 'downers'
            under_max_pop = (self.total_deployed + information['number']) <= 5
            if same_enemies and under_max_pop:
                i = 0
                for sprite in self.bad_list:
                    if i < information['number'] and \
                        sprite.deployed == False:
                            sprite.deployed = True
                            i += 1
                    else:
                        break
        #run
        self.bad_list.update()
        self.total_deployed  = self.update_total_deployed()

    def game_complete(self, frame_number):
        return frame_number >= self.level['CompleteAt']
        


        