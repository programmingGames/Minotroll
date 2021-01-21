import pygame
from pygame.locals import *
from data.gameplay.enimy.simpleAI import SimpleEnimysAI as EnimysAI
from data.gameplay.collisionControl import Colision
# from sys import exit
# import random


class Golens:
    def __init__(self, screen,pos, patrolRadius, golemType):
        self.screen = screen
        self.golemType = golemType
        self.name = ''
        self.renameTheGolemType()
        self.patrolRadius = patrolRadius
        self.state = 'Idle'
        self.move_direction = 'right'
        self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_0.png").convert_alpha()
        self.rect = self.imgGolens.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.initialPosition = pos[0]
        self.ai = EnimysAI(self.screen, self.patrolRadius,100, self.rect.x)
        self.collision = Colision()
        self.move_right = False
        self.move_left = False
        self.air_timer = 0
        self.vertical_momentum = 0
        self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_0.png").convert_alpha()
        self.move_frame = 0
        self.attacking = False
        self.isMe = False
    def renameTheGolemType(self):
        if(self.golemType == 1):
            self.name = 'fire golem'
        elif(self.golemType == 2):
            self.name = 'stone golem'
        elif(self.golemType == 3):
            self.name = 'ice golem'

    def controlingCollision(self, golens_move, platform_rects, player_rect, playerOnAttack):
        rect, plat_collisions = self.collision.platformCollision(golens_move,self.rect, platform_rects)
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
        if(self.rect.x in range(player_rect.x - 20, player_rect.x + 20)):
            self.isMe = True
        else:
            self.isMe = False
        # print(player_rect.x - 20, self.rect.x, player_rect.x + 20)
        # print(playerOnAttack[0], playerOnAttack[1], self.isMe)
        if playerOnAttack[0] and playerOnAttack[1] and self.isMe:

            self.impactDelay = 0
            self.collisionImpact()

    def collisionImpact(self):
        if(self.impactDelay <= 5):
            # self.player_rect, platformCollisions = self.collision.platformCollision(player_movement,self.player_rect,tile_rects)
            if(self.move_direction == 'right'):
                self.move_direction = 'left'
                self.rect.x -= 5
                self.rect.y -= 10
            elif(self.move_direction == 'left'):
                self.move_direction = 'right'
                self.rect.x += 5
                self.rect.y -= 10
            self.impactDelay += 1

    def add(self, platform_rects,player_rect,playerOnAttack, scroll):
        golens_move = [0, 0]
        if self.move_right:
            golens_move[0] += 1

        if self.move_left:
            golens_move[0] -= 1

        if (self.attacking and playerOnAttack == False):
            self.startAttack()
            '''if(self.move_direction =='right'):
                golens_move[0]+=4
            if(self.move_direction == 'left'):
                golens_move[0]-=4'''

        # if move_right and move_left not True call idle
        if ((not self.move_right)and(not self.move_left)):
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
        self.controlingCollision(golens_move, platform_rects, player_rect, playerOnAttack)
        self.screen.blit(self.imgGolens,(self.rect.x-scroll[0], self.rect.y-scroll[1]))
        # print(self.attacking, self.move_direction)
        return self.rect, self.name

    def determinateAttack(self):
        if((self.rect.x - self.initialPosition)>self.patrolRadius):
            self.move_right = False
            self.attacking = True
        elif((self.rect.x - self.initialPosition)<(-1*self.patrolRadius)):
            self.move_left = False
            self.attacking = True
        if((self.move_direction == 'right')and(self.move_right)):
            self.rect.x += 10
        elif((self.move_direction == 'left')and(self.move_left)):
            self.rect.x -= 10

    def walk(self):
        self.state = 'Walking'
        if(((self.move_right)or(self.move_left))and(self.move_frame <= 23)):        #resources\image\enimy\golens\Golem_1\Idle\left\0_Golem_Idle_000.png
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((self.move_right)or(self.move_left))and(self.move_frame > 23)):
            self.move_frame = 0
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()   
        else:
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()   

    def idle(self):
        self.state = 'Idle'
        if(((not self.move_right)or(not self.move_left ))and(self.move_frame <= 17)):
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()   
            self.move_frame += 1
        elif(((not self.move_right)or(not self.move_left))and(self.move_frame > 17)):
            self.move_frame = 0
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()

    def startAttack(self):
        self.state = 'Slashing'
        if((self.attacking)and(self.move_frame <= 11)):
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif((self.attacking)and(self.move_frame > 11)):
            self.move_frame = 0
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.imgGolens = pygame.image.load("resources/image/enimy/golens/Golem_"+str(self.golemType)+"/"+self.state+"/"+self.move_direction+"/0_Golem_"+self.state+"_"+str(self.move_frame)+".png").convert_alpha()
        