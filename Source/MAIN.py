'''
Main.py
this is what orcherstrates everything
this bring all the modules together to 
make this game.
'''
import pygame
import re
from colors import *
from classes import *
from scores import *
from level_conductor import *

#to make sure we are not getting anything silly
ip_address_regex = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b|'
lod_regex = '^easy$|^medium$|^hard$'
while True:
    ip_address = input('Please give me a ip... if its local just press enter')
    regex_ip = re.match(ip_address_regex,ip_address)
    pick_level_of_difficulty = input('please select level of difficulty [easy,medium,hard]')
    regex_lod = re.match(lod_regex,pick_level_of_difficulty)
    if regex_ip and regex_lod:
        break

pygame.init()
conductor = level_conductor(ip_address, pick_level_of_difficulty)
conductor.add_objects_to_list()
## font render
font = pygame.font.SysFont('Calibri', 25, True, False)
#screen stuff
size = (700, 500)
screen = pygame.display.set_mode( size)
done = False
miles = 0.0
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
frames = 0
#the conductor first attempts to talk to a server.
if conductor.initialize_connection_with_server() is False:
    raise Exception("cannot establish conneciton to the server")
    pygame.quit()
#get the first level
if conductor.get_a_level() == False:
    raise Exception("cannot get a level from server")
    pygame.quit()
#if it works, then play if not, then print to screen something happened.
#sscreen Loop
while not done:
    pygame.display.set_caption('The Cool Game     %s'%(clock))
    distance = font.render("distance: %f Miles" %(miles),True, color['green'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
    screen.fill(color['black'])
    screen.blit(distance,[5,475])
    miles+=score_flag(conductor.hero.pos_Y())
    is_the_game_done = conductor.game_complete(frames)
    if is_the_game_done is False:
        conductor.update_objects(frames)
    else:
        #once again we try to get a level by the server
        #since we are now in the game and it fails we should
        #kill the game
        if conductor.get_a_level() == False:
            raise Exception("cannot get a level from server")
            conductor.handler.end_game()
            pygame.quit()
        frames = 0
    frames += 1
    #detects if the hero of this awesome game hits a bad guy
    if len(conductor.plane_collides()) > 1:
        conductor.handler.end_game()
        print('GAME OVER.... DISTANCE TRAVELED: %f'%(miles))
        break
    conductor.all_sprites_list.draw(screen) #makes everything move
    clock.tick(60) #keeps frame rate at 60 frames a sec
    pygame.display.flip()
conductor.handler.quit_game()
pygame.quit()#stops pygame


