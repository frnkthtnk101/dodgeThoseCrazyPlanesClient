import pygame
from classes import *
from level_reader  import level_reader

class level_conductor:
    def __init__(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.stars_list= pygame.sprite.Group()
        self.bad_list=pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.hero = TheGUY()
        self.total_deployed = 0

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
        return True
    
    def get_a_level(self):
        level_rder = level_reader('/Users/francopettigrosso/ws/dodgeThoseCrazyPlanesClient/data.json')
        self.level = level_rder.get_level()

    def update_total_deployed(self):
        j = 0
        for i in self.bad_list:
            if i.deployed:
                j += 1
        return j

    def update_objects(self, frame_number):
        self.stars_list.update()
        self.hero.mous_pos()
        if len(self.level['Data']['level']) > 0 and \
         frame_number == self.level['Data']['level'][0]['tick']:
            information = self.level['Data']['level'].pop(0)
            #see the type and number
            if information["enemies"] == "downers" and \
            (self.total_deployed + information['number']) <= 5:
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
        self.update_total_deployed()
        


        