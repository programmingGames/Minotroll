import pygame 
from data.gameplay.headUpDisplay.rects import Rects

class Life:
    def __init__(self, screen, qtlife):
        self.screen = screen
        self.lifeBox = pygame.image.load("resources/image/headUpDisplay/conteiner/box1.png")
        self.lifeArray = []
        self.x = 100
        self.y = 27
        self.qtlife = qtlife
        self.maxLife = 238
        self.count = 0
        self.start = True

    def settingLife(self):
        pass
    def damageLife(self, damage):
        for i in range(damage):
            self.lifeArray = self.lifeArray[:-1]
    def draw(self):
        if (self.start):
            self.initialLife()
            self.start = False
        self.x = 100
        [life.rectDraw() for life in self.lifeArray]
        self.screen.blit(self.lifeBox, (95, 20))
        
        if(len(self.lifeArray) == 0):
            pass

    def initialLife(self):
        for i in range (self.qtlife):
            life = Rects(self.screen, 1, 23, self.x, self.y, (0,255, 0))
            self.lifeArray.append(life)
            self.x += 1