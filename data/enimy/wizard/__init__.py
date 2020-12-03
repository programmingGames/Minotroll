import pygame
from pygame.locals import *
from sys import exit
import random


class Wizard:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(40, 30, 20, 42)
        self.state = 'idle'
        self.move_direction = 'right'
        self.move_right = False
        self.move_left = False
        self.air_timer = 0
        self.vertical_momentum = 0
        self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara-0.png")
        self.rect.x = 600
        self.move_frame = 0
        self.attacking = False

    
    def platformTestCollision(self, tiles):
        hit_list = []
        for tile in tiles:
            if (self.rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list

    # def playerTestCollision(self, tiles):
    #     hit_list = []
    #     if (self.rect.colliderect(tiles)):
    #         hit_list.append(tiles)
    #     return hit_list

    # def playerCollision(self,move, tiles):
    #     collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    #     self.rect.x += move[0]
    #     hit_list = self.playerTestCollision(tiles)
    #     for tile in hit_list:
    #         if(move[0]>0):
    #             self.rect.right = tile.left
    #             collision_types['right'] = True
    #         elif(move[0]<0):
    #             self.rect.left = tile.right
    #             collision_types['left'] = True
        
    #     self.rect.y += move[1]
    #     hit_list = self.playerTestCollision(tiles)
    #     for tile in hit_list:
    #         if move[1]>0:
    #             self.rect.bottom = tile.top
    #             collision_types['bottom'] = True
    #         if move[1]<0:
    #             self.rect.top = tile.bottom
    #             collision_types['top'] = True
    #     return collision_types

    def platformCollision(self,move, tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect.x += move[0]
        hit_list = self.platformTestCollision(tiles)
        for tile in hit_list:
            if(move[0]>0):
                self.rect.right = tile.left
                collision_types['right'] = True
            elif(move[0]<0):
                self.rect.left = tile.right
                collision_types['left'] = True
        
        self.rect.y += move[1]
        hit_list = self.platformTestCollision(tiles)
        for tile in hit_list:
            if move[1]>0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            if move[1]<0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
        return collision_types


    def makeMove(self, platform_rects):
        wizard_move = [0, 0]
        
        if self.move_right:
            wizard_move[0] += 2

        if self.move_left:
            wizard_move[0] -= 2
        
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

        
        platform_collisions = self.platformCollision(wizard_move, platform_rects)
        if platform_collisions['bottom']:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1
        
        
        

    def move(self, event, platform_rects, scroll, move_right, move_left, attacking, direction):
        # self.moveChoise(event)
        
        self.move_right = move_right
        self.move_left = move_left
        self.attacking = attacking
        self.move_direction = direction
        self.makeMove(platform_rects)
        self.draw(scroll)
        

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

    def draw(self, scroll):
        self.screen.blit(self.img,(self.rect.x-scroll[0], self.rect.y-scroll[1]))


## Simple AI add to this enimy

class WizardSimpleAI:
    def __init__(self, screen):
        self.patrolRadius = 100
        self.attacking = False
        self.patroling = False
        self.wizard = Wizard(screen)
        self.move_right = False
        self.move_left = False
        self.initialPosition = self.wizard.rect.x
        self.direction = 'right'
        self.timer = 0 
        
    def activation(self, event, platform_rects, scroll, player_rect):
        ## Making the partro
        if(self.timer == 50):
            self.choisingMove()
            self.timer = 0
        else:
            self.timer += 1
        
        # Controlling the radius of patroling
        if((self.wizard.rect.x-self.initialPosition)>self.patrolRadius):
                self.move_right = False
        elif((self.wizard.rect.x-self.initialPosition)<(-1*self.patrolRadius)):
            self.move_left = False

        ## this will return true if the player is next to the wizard
        # if self.calculateProximity(player_rect):
        #     self.attacking = True
        # else:
        #     self.attacking = False

        self.wizard.move(event, platform_rects, scroll, self.move_right, self.move_left, self.attacking, self.direction)
        return self.wizard.rect

    # Next time i'm going to do this part here
    def calculateProximity(self, player_rect):
        print("________")
        print("w", self.wizard.rect.x)
        print("p", player_rect.x)
        print(self.wizard.rect.x-player_rect.x)
        if((self.wizard.rect.x-player_rect.x)<=80):
            return True
        else:
            return False 

    def choisingMove(self):
        rand = random.random()
        if (rand<0.3):
            self.direction = 'left'
            self.move_right = False
            self.move_left = True
        elif((rand>=0.3)and(rand<0.7)):
            self.move_left = False
            self.move_right = False
        else:
            self.direction = 'right'
            self.move_left = False
            self.move_right = True