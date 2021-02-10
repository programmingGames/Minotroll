import pygame
import random
from data.gameplay.collisionControl import Colision


class Plants():
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.plantPosition = []
        self.determinatePlantPosition()
        self.plants = [SomePlant(self.screen, pos) for pos in self.plantPosition]

    def add(self,scroll):
        # drawing plant animations
        i = 0
        for pos in self.plantPosition:
            if(pos[0] in range(scroll[0]-450), scroll[0]+650):
                self.plants[i].add(scroll)
            i+=1

    def determinatePlantPosition(self):
        if(self.nivel == 0):
            self.plantPosition = [(510,120), (690,120),(862,120),(2734,296),(2852,296),(5376,40),(5496,40)]
        elif(self.nivel == 1):
            self.plantPosition = [(440,88), (668,88),(1344,184),(3386,184), (1503,184), (3386,184), (4272,184), (4808,104), (5437,168)]
        elif(self.nivel == 2):
            self.plantPosition = []
        elif(self.nivel == 3):
            self.plantPosition = [ (380,200), (548,200), (2720,280), (3200,120), (3396,120), (3416,120), (3639,120), (3659,120), (3779,120), (3877,120)]
        

class SomePlant():
    # 1 ajuste 1.2
    # 2 ajuste 1.2
    # 3 ajuste 1.25
    # 4 ajuste 1.3
    def __init__(self, screen, pos):
        self.screen = screen
        self.ajust = 0
        self.plnt = 0
        self.randomPlants()
        self.plant = pygame.image.load("resources/image/animation/arvores/"+str(self.plnt)+".png").convert_alpha()
        self.rect = self.plant.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.collision = Colision()
    
    def randomPlants(self):
        self.plnt = random.randint(1, 4)
        if self.plnt == 1 or self.plnt == 2:
            self.ajust = 1.2
        elif self.plnt == 3:
            self.ajust = 1.25
        else:
            self.ajust = 1.3
    def add(self,scroll):
        self.screen.blit(self.plant,(self.rect.x-scroll[0]-self.rect.width/self.ajust, self.rect.y-scroll[1]-self.rect.height/self.ajust))
