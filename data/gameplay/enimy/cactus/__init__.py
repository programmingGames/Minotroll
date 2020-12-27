import pygame
import random

class Cactus:
    def __init__(self, screen):
        self.y = 200
        self.screen = screen
        self.x = random.randint(600, 700)
        self.img = pygame.image.load("resources/image/platform/florest/Cactus-1.png").convert_alpha()

    def draw(self, x, y):
        self.screen.blit(self.img, (y, x))