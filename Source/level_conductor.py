from classes import *
import pygame

class level_conductor:
    def __init__(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.stars_list= pygame.sprite.Group()
        self.bad_list=pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.hero = TheGUY()