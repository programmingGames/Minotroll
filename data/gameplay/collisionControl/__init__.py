import pygame
from pygame.locals import *

class Colision(object):
    def __init__(self):
        pass
    
    def TestCollision(self,rect, tiles):
        hit_list = []
        for tile in tiles:
            if (rect.colliderect(tile)):
                hit_list.append(tile)
        return hit_list

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
        return collision_types