import pygame
import random
from data.gameplay.collisionControl import Colision

class Cactus:
    def __init__(self, screen, position):
        self.y = 200
        self.screen = screen
        self.collision = Colision()
        self.x = random.randint(600, 700)
        self.air_timer = 0
        self.vertical_momentum = 0
        self.img = pygame.image.load("resources/image/platform/florest/obstaculo/cactus.png").convert_alpha()
        self.cactusRects =self.img.get_rect()
        self.cactusRects.x = position

    def controlingCollision(self, move, platform_rects):
        plat_collisions = self.collision.platformCollision(move,self.cactusRects, platform_rects)

        # bottom collision
        if plat_collisions['bottom']:
            self.air_timer = 0
            self.vertical_momentum = 0
        else:
            self.air_timer += 1

    def addCactus(self, platform_rects, scroll):
        move = [0, 0]

        move[1] += self.vertical_momentum

        self.vertical_momentum += 0.2
        if self.vertical_momentum > 8:
            self.vertical_momentum = 8
        
        
        self.controlingCollision(move, platform_rects)
        self.screen.blit(self.img, (self.cactusRects.x-scroll[0], self.cactusRects.y-scroll[1]))

        return (self.cactusRects, 'cactus')