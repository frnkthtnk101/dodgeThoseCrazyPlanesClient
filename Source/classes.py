'''
code for the objects in the game
you will find the bad guys, the player,
and the "stars"
'''
from pathlib import Path
HOME = str(Path.home())
import pygame
import sys
sys.path.append(f'{HOME}/dodgeThoseCrazyPlanesClient')
from colors import *
import random

'''
This is the main player class
it inherents the sprite class
in pygame
'''
class TheGUY(pygame.sprite.Sprite):
    '''
    creates an instance of the TheGUY
    '''
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(f'{HOME}/dodgeThoseCrazyPlanesClient/Sprites/hero.png')
        self.image.set_colorkey(color['white'])
        self.rect= self.image.get_rect()

    '''
    shows the y pos of the player
    '''
    def pos_Y(self):
        pos=pygame.mouse.get_pos()
        return float(pos[1])

    '''
    shows the x pos of the player
    also, keeps the player on the
    screen
    '''
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

'''
the little stars on the screen
the make the player 'feel' like
the player is moving but they 
really aren't
'''
class star(pygame.sprite.Sprite):
    '''
    creates a star - puts in 
    random location
    '''
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(f'{HOME}/dodgeThoseCrazyPlanesClient/Sprites/star.png')
        self.image.set_colorkey(color['white'])
        self.rect= self.image.get_rect()
        self.rect.x=random.randrange(700)
        self.rect.y=random.randrange(-500,0)
    
    '''
    makes the star goe down 
    3 pixels, eventualy it 
    will put it back on the
    top of the screen
    '''
    def update(self):
        self.rect.y+=3
        if self.rect.y >= 500:
            self.rect.y=random.randrange(-500,0)
            self.rect.x=random.randrange(700)

'''
makes the bad guys in the game
'''
class bad_guy(pygame.sprite.Sprite):
    
    '''
    creates a bad_guy. puts it in a
    random positon.
    '''
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(f'{HOME}/dodgeThoseCrazyPlanesClient/Sprites/badguys.png')
        self.image.set_colorkey(color['white'])
        self.rect= self.image.get_rect()
        self.rect.x=random.randrange(600)
        self.rect.y=random.randrange(-500,0)
        self.deployed = False
        self.on_screen = True

    '''
    puts the bad_guy back on top 
    of the screen
    '''    
    def reset_pos(self):
        self.rect.y=random.randrange(-500,0)
        self.rect.x=random.randrange(600)
        self.on_screen = True
    
    '''
    moves the bad-guy down
    also tell the conductor if this 
    bad guy is already moving or not
    '''
    def update(self):
        if self.on_screen and self.deployed:
            self.rect.y+=7
        if self.rect.y >= 500:
            self.on_screen = False
            self.deployed = False
            self.reset_pos()

            
            
    
        
            
            

    
    
    
