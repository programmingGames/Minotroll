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
        self.maxLife = 240
        self.count = 0
        self.start = True
        ## pixel of the life is equal 242

    def damageLife(self, damage):
        for i in range(damage):
            self.lifeArray = self.lifeArray[:-1]
            self.qtlife -= 1
            if(self.x >= 100):
                self.x -= 1

    def incrementLife(self, qtlife):
        for i in range(qtlife):
            life = Rects(self.screen, 1, 23, self.x, self.y, (0,255, 0))
            self.lifeArray.append(life)
            self.qtlife += qtlife
            if(self.x <= 340):
                self.x += 1

    def draw(self):
        if (self.start):
            self.initialLife()
            self.start = False

        self.lostLifeDrawEffect()
        self.screen.blit(self.lifeBox, (95, 20))
        
        if(len(self.lifeArray) == 0):
            pass

    def initialLife(self):
        for i in range (self.qtlife):
            life = Rects(self.screen, 1, 23, self.x, self.y, (0,255, 0))
            self.lifeArray.append(life)
            if(self.x <= 340):
                self.x += 1

    def lostLifeDrawEffect(self):
        if(self.qtlife >= 200):
            [life.drawGradientEffect(0) for life in self.lifeArray]
        elif((self.qtlife >= 160)and(self.qtlife < 200)):
            [life.drawGradientEffect(1) for life in self.lifeArray]
        elif((self.qtlife >= 120)and(self.qtlife < 160)):
            [life.drawGradientEffect(2) for life in self.lifeArray]
        elif((self.qtlife >= 80)and(self.qtlife < 120)):
            [life.drawGradientEffect(3) for life in self.lifeArray]
        elif((self.qtlife >= 40)and(self.qtlife < 80)):
            [life.drawGradientEffect(4) for life in self.lifeArray]
        elif((self.qtlife >= 20)and(self.qtlife < 40)):
            [life.drawGradientEffect(5) for life in self.lifeArray]
        else:
            [life.drawGradientEffect(6) for life in self.lifeArray]