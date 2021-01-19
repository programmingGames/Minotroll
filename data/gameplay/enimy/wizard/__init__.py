import pygame
from pygame.locals import *
from data.gameplay.enimy.simpleAI import SimpleEnimysAI as EnimysAI
from data.gameplay.collisionControl import Colision
# from sys import exit
# import random


class Wizard:
    def __init__(self, screen, pos, patrolRadius):
        self.screen = screen
        self.name = 'blue wizard'
        self.patrolRadius = patrolRadius
        self.rect = pygame.Rect(40, 30, 20, 42)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.initialPosition = pos[0]
        self.ai = EnimysAI(self.screen, self.patrolRadius,200, self.rect.x)
        self.collision = Colision()
        self.state = 'idle'
        self.move_direction = 'right'
        self.move_right = False
        self.move_left = False
        self.air_timer = 0
        self.vertical_momentum = 0
        self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-0.png")
        self.move_frame = 0
        self.impactDelay = 0
        self.attacking = False
        self.isMe = False


    def controlingCollision(self, wizard_move, platform_rects, player_rect, playerOnAttack):
        rect, plat_collisions = self.collision.platformCollision(wizard_move,self.rect, platform_rects)
        # right, left collision
        del rect
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
        
        if(self.rect.x in range(player_rect.x - 10, player_rect.x + 10)):
            self.isMe = True
        else:
            self.isMe = False
        print(playerOnAttack[0], playerOnAttack[1], self.isMe)
        if playerOnAttack[0] and playerOnAttack[1] and self.isMe:
            print("playerColision")
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
        wizard_move = [0, 0]
        if self.move_right:
            wizard_move[0] += 1

        if self.move_left:
            wizard_move[0] -= 1
        
        if (self.attacking and playerOnAttack == False):
            self.startAttack()

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
        
        
        self.move_direction, self.move_right, self.move_left, self.attacking = self.ai.activation(self.rect, player_rect)
        self.determinateAttack()
        self.controlingCollision(wizard_move, platform_rects, player_rect, playerOnAttack)
        self.screen.blit(self.img,(self.rect.x-scroll[0], self.rect.y-scroll[1]))
        # print(self.attacking, self.move_direction)
        return self.rect, self.name

    def determinateAttack(self):

        if((self.rect.x - self.initialPosition)>self.patrolRadius):
                self.move_right = False
        elif((self.rect.x - self.initialPosition)<(-1*self.patrolRadius)):
            self.move_left = False
        if((self.move_direction == 'right')and(self.move_right)):
            self.rect.x += 10
        elif((self.move_direction == 'left')and(self.move_left)):
            self.rect.x -= 10

    def walk(self):
        self.state = 'walk'
        if(((self.move_right)or(self.move_left))and(self.move_frame <= 19)):
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif(((self.move_right)or(self.move_left))and(self.move_frame > 19)):
            self.move_frame = 0 
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()        
        else:
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-"+str(self.move_frame)+".png").convert_alpha()

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
            
    def startAttack(self):
        # image = 15
        self.state = 'attack'
        if((self.attacking)and(self.move_frame <= 12)):
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Dash3-"+str(self.move_frame)+".png").convert_alpha()
            self.move_frame += 1
        elif((self.attacking)and(self.move_frame > 12)):
            self.move_frame = 0
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Dash3-"+str(self.move_frame)+".png").convert_alpha()
        else:
            self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Dash3-"+str(self.move_frame)+".png").convert_alpha()

        