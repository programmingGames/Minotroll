import pygame
from pygame.locals import *
from data.gameplay.enimy.simpleAI import SimpleEnimysAI as EnimysAI
from data.gameplay.collisionControl import Colision
# from sys import exit
# import random


class Minotauro:
    def __init__(self, screen,pos, patrolRadius):
        self.screen = screen
        self.patrolRadius = patrolRadius
        self.state = 'Idle'
        self.move_direction = 'right'
        self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01_"+self.state+"_0.png").convert_alpha()
        self.rect = self.imgMinotaur.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.initialPosition = pos[0]
        self.ai = EnimysAI(self.screen, self.patrolRadius,100, self.rect.x)
        self.collision = Colision()
        self.move_right = False
        self.move_left = False
        self.air_timer = 0
        self.vertical_momentum = 0
        self.move_frame = 0
        self.attacking = False

    def controlingCollision(self, minotauro_move, platform_rects):
        plat_collisions = self.collision.platformCollision(minotauro_move,self.rect, platform_rects)
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

    def addingGolens(self, platform_rects,player_rect, scroll):
        golens_move = [0, 0]
        if self.move_right:
            golens_move[0] += 1

        if self.move_left:
            golens_move[0] -= 1

        if self.attacking:
            self.startAttack()
            '''if(self.move_direction =='right'):
                golens_move[0]+=4
            if(self.move_direction == 'left'):
                golens_move[0]-=4'''

        # if move_right and move_left not True call idle
        if ((not self.move_right)and(not self.move_left)and (not self.attacking)):
            self.idle()
        else:
            self.walk()

        golens_move[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 8:
            self.vertical_momentum = 8

        self.rect.x += golens_move[0]

        self.move_direction, self.move_right, self.move_left, self.attacking = self.ai.activation(self.rect, player_rect)
        self.determinateAttack()
        self.controlingCollision(golens_move, platform_rects)
        self.screen.blit(self.imgMinotaur,(self.rect.x-scroll[0], self.rect.y-scroll[1]))
        # print(self.attacking, self.move_direction)
        return self.rect, 'brown minotaur'

    def determinateAttack(self):
        if((self.rect.x - self.initialPosition)>self.patrolRadius):
            self.move_right = False
        elif((self.rect.x - self.initialPosition)<(-1*self.patrolRadius)):
            self.move_left = False
   

    def walk(self):
        self.state = 'Walking'
        if(((self.move_right)or(self.move_left))and(self.move_frame <= 17)):        
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((self.move_right)or(self.move_left))and(self.move_frame > 17)):#resources\image\enimy\minotauro\Minotaur_1\Idle\right\Minotaur_01_Idle_0.png
            self.move_frame = 0
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()

    def idle(self):
        self.state = 'Idle'
        if(((not self.move_right)or(not self.move_left ))and(self.move_frame <= 17)):
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((not self.move_right)or(not self.move_left))and(self.move_frame > 17)):
            self.move_frame = 0
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()

    def startAttack(self):
        self.state = 'Slashing'
        if((self.attacking)and(self.move_frame <= 11)):
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
            print("1")
        elif((self.attacking)and(self.move_frame > 11)):
            self.move_frame = 0
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            print("2")
        else:
            self.imgMinotaur = pygame.image.load("resources/image/enimy/minotauro/Minotaur_1/"+self.state+"/"+self.move_direction+"/Minotaur_01"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
