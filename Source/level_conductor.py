from classes import *
import pygame

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