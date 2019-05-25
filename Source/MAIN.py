#import
import pygame
from colors import *
from classes import *
from scores import *
from level_conductor import level_conductor

'''
we do it like this
we make 50 guys
and make a list on the levels
pop it when it his its mark
and tell it what guys to create.
once it hits the meter. stop it and make reqeust a new level
'''

pygame.init()
conductor = level_conductor()
## font render
font = pygame.font.SysFont('Calibri', 25, True, False)
#screen stuff
size=(700,500)
screen=pygame.display.set_mode(size)
done=False
miles=0.0
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)
frames = 0
#get the first level
#if it works, then play if not, then print to screen something happened.
#sscreen Loop
while not done:
    pygame.display.set_caption('The Cool Game     %s'%(clock))
    distance = font.render("distance: %f Miles" %(frames),True, color['green'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
    screen.fill(color['black'])
    screen.blit(distance,[5,475])
    miles+=score_flag(conductor.hero.pos_Y())
    
    #print('x axis %g, y axis %g' %(hero.rect.x,hero.rect.y)) #test cordinates of good guy
    stars_list.update() #makes the stars move
    hero.mous_pos()#changes cordinates of player
    bad_list.update()#moves the bad guys
    blocks_hit_list = pygame.sprite.spritecollide(hero, block_list, False)
    ###print(blocks_hit_list) #test collsion WARNING FRAMERATE DROP
    frames += 1
    #detects if the hero of this awesome game hits a bad guy
    if len(blocks_hit_list) > 1:
        print('GAME OVER.... DISTANCE TRAVELED: %f'%(miles))
        #print(blocks_hit_list)
        done=True
        #highscore= append_list(name,miles,highscore)
        #print(highscore)
    
        
    all_sprites_list.draw(screen) #makes everything move
    
  
    clock.tick(60) #keeps frame rate at 60 frames a sec
    pygame.display.flip()



pygame.quit()#stops pygame


