import pygame
from pygame.locals import *
from data.gameplay.enimy import SimpleEnimysAI as EnimysAI
from data.gameplay.collisionControl import Colision
# from sys import exit
# import random


class Wizard:
    def __init__(self, screen):
        self.screen = screen
        self.ai = EnimysAI(self.screen, 100, 1000)
        self.collision = Colision()
        self.rect = pygame.Rect(40, 30, 20, 42)
        self.state = 'idle'
        self.move_direction = 'right'
        self.move_right = False
        self.move_left = False
        self.air_timer = 0
        self.vertical_momentum = 0
        self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-0.png")
        self.rect.x = 1000
        self.move_frame = 0
        self.attacking = False


    def controlingCollision(self, wizard_move, platform_rects):
        plat_collisions = self.collision.platformCollision(wizard_move,self.rect, platform_rects)
        # right, left collision
        if(plat_collisions['right']):
            self.move_right = False
        elif(plat_collisions['left']):
            self.move_left = False

        # bottom collision
        if plat_collisions['bottom']:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1
        
    def addingWizard(self, platform_rects, scroll):
        wizard_move = [0, 0]
        if self.move_right:
            wizard_move[0] += 1

        if self.move_left:
            wizard_move[0] -= 1
        
        if self.attacking:
            self.attack()

        # if move_right and move_left not True call idle
        if ((not self.move_right)and(not self.move_left)):
            self.idle()
        else:
            self.walk()

        wizard_move[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 8:
            self.vertical_momentum = 8

        
        self.rect.x += wizard_move[0]
        
        
        self.move_direction, self.move_right, self.move_left, self.attack = self.ai.activation(self.rect)
        self.controlingCollision(wizard_move, platform_rects)
        self.screen.blit(self.img,(self.rect.x-scroll[0], self.rect.y-scroll[1]))
        return self.rect   

    def walk(self):
        self.state = 'walk'
        if(((self.move_right)or(self.move_left))and(self.move_frame <= 19)):
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((self.move_right)or(self.move_left))and(self.move_frame > 19)):
            self.move_frame = 0 
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()        
        else:
            self.player_img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()

    def idle(self):
        self.state = 'idle'
        if(((not self.move_right)or(not self.move_left ))and(self.move_frame <= 19)):
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.move_right)or(not self.move_left))and(self.move_frame > 19)):
            self.move_frame = 0
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()
            
    def attack(self):
        # image = 15
        self.state = 'attack'
        if((self.attacking)and(self.move_frame <= 15)):
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Dash3-"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif((self.attacking)and(self.move_frame > 15)):
            self.move_frame = 0
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Dash3-"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Dash3-"+str(self.move_frame)+".png").convert_alpha()

        if(self.move_direction == 'right'):
            self.rect.x += 10
        elif(self.move_direction == 'left'):
            self.rect.x -= 10

        