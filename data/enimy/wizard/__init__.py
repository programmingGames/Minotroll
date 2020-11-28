import pygame
from pygame.locals import *
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
        self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara - BlueIdle_0.png")

    
    def collision(self, tiles):
        hit_list = []
        for tile in tiles:
            if (self.rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list

    def playerCollision(self, tiles):
        
        pass

    def platformCollision(self,move, tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect.x += move[0]
        hit_list = self.collision(tiles)
        for tile in hit_list:
            if(move[0]>0):
                self.rect.right = tile.left
                collision_types['right'] = True
            elif(move[0]<0):
                self.rect.left = tile.right
                collision_types['left'] = True
        
        self.rect.y += move[1]
        hit_list = self.collision(tiles)
        for tile in hit_list:
            if move[1]>0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            if move[1]<0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
        return collision_types

    
    def moveChoise(self, event):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.move_direction = 'right'
                    self.move_right = True
                if event.key == K_LEFT:
                    self.move_direction = 'left'
                    self.move_left = True
            else:
                self.move_right, self.move_left = False, False

    def makeMove(self, platform_rects):
        wizard_move = [0, 0]
        if self.move_right:
            wizard_move[0] += 4

        if self.move_left:
            wizard_move[0] -= 4

        wizard_move[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 6:
            self.vertical_momentum = 6

        platform_collisions = self.platformCollision(wizard_move, platform_rects)
        if platform_collisions['bottom']:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1

    def move(self, event, platform_rects):
        self.moveChoise(event)
        self.makeMove(platform_rects)
        self.draw()

    def idle(self):
        pass

    def attack(self):
        pass

    def walk(self):
        pass

    def draw(self):
        self.screen.blit(self.img,(self.rect.x, self.rect.y))