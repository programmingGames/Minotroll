import pygame
import random


class Wizard:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.rect(42, 20, 42, 20)
        self.state = 'idle'
        self.move_direction = random.choices('left', 'right')
        self.img = pygame.image.load("resources/image/enimy/wizard/"+self.state+"/"+self.move_direction+"/Chara - BlueIdle_0")
        