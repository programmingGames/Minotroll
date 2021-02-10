import pygame
from pygame.locals import *

# Class to control all the colision on the game
class Colision(object):
    def __init__(self):
        self.colisionPos = 0
    
    # Method to make a list of all the possible platform collision
    def TestCollision(self,rect, tiles):
        hit_list = []
        for tile in tiles:
            if (rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list

    # Method to control the platforms colision
    def platformCollision(self,move,rect, tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        rect.x += move[0]
        hit_list = self.TestCollision(rect,tiles)
        for tile in hit_list:
            if(move[0]>0):
                rect.right = tile.left
                collision_types['right'] = True
            elif(move[0]<0):
                rect.left = tile.right
                collision_types['left'] = True
        
        rect.y += move[1]
        hit_list = self.TestCollision(rect,tiles)
        for tile in hit_list:
            if move[1]>0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            if move[1]<0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect,collision_types

    # Method to make a list of all the possible platform collision
    def enimysTestCollision(self, playerRect, enimysRects):
        hit_list = []
        count = 0
        for tile in enimysRects:
            if (playerRect.colliderect(tile)):
                hit_list.append(tile)
                self.colisionPos = count
            count += 1
        return hit_list

    # Method to test the enimys colision an player collision
    def enimysCollision(self,playerMove, playerRect, enimysRects):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        hit_list = self.enimysTestCollision(playerRect,enimysRects)
        for tile in hit_list:
            if(playerMove[0]>0):
                playerRect.right = tile.left
                collision_types['right'] = True
            elif(playerMove[0]<0):
                playerRect.left = tile.right
                collision_types['left'] = True
        
        hit_list = self.enimysTestCollision(playerRect,enimysRects)
        for tile in hit_list:
            if playerMove[1]>0:
                playerRect.bottom = tile.top
                collision_types['bottom'] = True
            if playerMove[1]<0:
                playerRect.top = tile.bottom
                collision_types['top'] = True
        return collision_types, self.colisionPos
