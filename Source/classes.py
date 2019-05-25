import pygame
from colors import *
import random
#import math too hard to play

class TheGUY(pygame.sprite.Sprite):
    def __init__(self):
    

        #super init
        super().__init__()
        self.image= pygame.image.load('../Sprites/hero.png')
        self.image.set_colorkey(color['white'])
        self.rect= self.image.get_rect()

    def pos_Y(self):
        pos=pygame.mouse.get_pos()
        return float(pos[1])

    def mous_pos(self):
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        if x <=650:
            self.rect.x=pos[0]
        else:
            self.rect.x=650
        if y<=450:
            self.rect.y=pos[1]
        else:
            self.rect.y=425

class star(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        self.image= pygame.image.load('../Sprites/star.png')
        self.image.set_colorkey(color['white'])
        self.rect= self.image.get_rect()
  

        self.rect.x=random.randrange(700)
        self.rect.y=random.randrange(-500,0)
    

    def update(self):
        self.rect.y+=3
        if self.rect.y >= 500:
            self.rect.y=random.randrange(-500,0)
            self.rect.x=random.randrange(700)

class bad_guy(pygame.sprite.Sprite):
    def __init__(self):
        #super init
        super().__init__()
        self.image= pygame.image.load('../Sprites/badguys.png')
        self.image.set_colorkey(color['white'])
        self.rect= self.image.get_rect()
        self.rect.x=random.randrange(600)
        self.rect.y=random.randrange(-500,0)
        self.deployed = False
        self.on_screen = True
        
    def reset_pos(self):
        self.rect.y=random.randrange(-500,0)
        self.rect.x=random.randrange(600)
        
    def Where_am_i(self):
        if self.rect.y >= 500:
            self.on_screen = False;
            self.deployed = False;

    def update(self):
        if self.on_screen and self.deployed:
            self.rect.y+=7
        if self.rect.y >= 500:
            self.reset_pos()
            
    
        
            
            

    
    
    
