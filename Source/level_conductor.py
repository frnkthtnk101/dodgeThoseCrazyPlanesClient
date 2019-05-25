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
    
    def initialize_connection_with_server():
        return True
    
    def get_a_level():
        level_rder = level_reader('/Users/francopettigrosso/ws/dodgeThoseCrazyPlanesClient/data.json')
        self.level = level_rder.get_level()
        