#import
import pygame
from colors import *
from classes import *
from scores import *


pygame.init()

#lists
all_sprites_list = pygame.sprite.Group()
stars_list= pygame.sprite.Group()
bad_list=pygame.sprite.Group()
block_list = pygame.sprite.Group()


## init sprites
#you
hero=TheGUY()
all_sprites_list.add(hero)
block_list.add(hero)

#stars
for i in range(50):
    stars= star()
    all_sprites_list.add(stars)
    stars_list.add(stars)
    
#bad guys
for i in range(5):
    badGuy= bad_guy()
    all_sprites_list.add(badGuy)
    bad_list.add(badGuy)
    block_list.add(badGuy) 
    
## font render
font = pygame.font.SysFont('Calibri', 25, True, False)


#screen stuff
size=(700,500)

screen=pygame.display.set_mode(size)
done=False
miles=0.0
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)

#sscreen Loop
while not done:
    pygame.display.set_caption('The Cool Game     %s'%(clock))
    distance = font.render("distance: %f Miles" %(miles),True, color['green'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
    screen.fill(color['black'])
    screen.blit(distance,[5,475])
    miles+=score_flag(hero.pos_Y())
    
    #print('x axis %g, y axis %g' %(hero.rect.x,hero.rect.y)) #test cordinates of good guy
    stars_list.update() #makes the stars move
    hero.mous_pos()#changes cordinates of player
    bad_list.update()#moves the bad guys
    blocks_hit_list = pygame.sprite.spritecollide(hero, block_list, False)
    ###print(blocks_hit_list) #test collsion WARNING FRAMERATE DROP
    
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

