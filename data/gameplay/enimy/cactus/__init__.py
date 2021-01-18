import pygame
# import random
from data.gameplay.collisionControl import Colision

class Cactus:
    def __init__(self, screen, position):
        self.screen = screen
        self.name = 'cactus'
        self.collision = Colision()
        self.air_timer = 0
        self.vertical_momentum = 0
        self.img = pygame.image.load("resources/image/platform/florest/obstaculo/cactus.png").convert_alpha()
        self.cactusRects =self.img.get_rect()
        self.cactusRects.x = position[0]
        self.cactusRects.y = position[1]


    def controlingCollision(self, move, platform_rects):
        rct, plat_collisions = self.collision.platformCollision(move,self.cactusRects, platform_rects)
        del rct
        # bottom collision
        if plat_collisions['bottom']:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1

    def add(self, platform_rects, player_rect, scroll):
        del player_rect
        move = [0, 0]

        move[1] += self.vertical_momentum

        self.vertical_momentum += 0.2
        if self.vertical_momentum > 8:
            self.vertical_momentum = 8
        
        
        self.controlingCollision(move, platform_rects)
        self.screen.blit(self.img, (self.cactusRects.x-scroll[0], self.cactusRects.y-scroll[1]))

        return (self.cactusRects, self.name)