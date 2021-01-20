import pygame 
from data.gameplay.headUpDisplay.rects import Rects

class Life:
    def __init__(self, screen, qtlife):
        self.screen = screen
        self.lifeBox = pygame.image.load("resources/image/headUpDisplay/conteiner/box1.png")
        self.lifeRect = pygame.Rect(0,0,0,0)
        self.qtlife = 218
        self.maxLife = 218
        self.start = True
        ## pixel of the life is equal 242

    def updateLife(self, qtlife):
        if(self.qtlife <= 218):
            if(self.qtlife+qtlife > 218):
                self.qtlife = 218
            else:
                self.qtlife = self.qtlife + qtlife

    def draw(self):
        self.screen.blit(self.lifeBox, (82, 42))
        if (self.start):
            self.lifeRect = Rects(self.screen, self.qtlife, 12, 98, 55, (0,255, 0))
            self.start = False
        
        self.lostLifeDrawEffect()
        return self.qtlife
        
    def lostLifeDrawEffect(self):
        if(self.qtlife >= 200):
            self.lifeRect.drawGradientEffect(0, self.qtlife)
        elif((self.qtlife >= 160)and(self.qtlife < 200)):
            self.lifeRect.drawGradientEffect(1, self.qtlife)
        elif((self.qtlife >= 120)and(self.qtlife < 160)):
            self.lifeRect.drawGradientEffect(2, self.qtlife)
        elif((self.qtlife >= 80)and(self.qtlife < 120)):
            self.lifeRect.drawGradientEffect(3, self.qtlife)
        elif((self.qtlife >= 40)and(self.qtlife < 80)):
            self.lifeRect.drawGradientEffect(4, self.qtlife)
        elif((self.qtlife >= 20)and(self.qtlife < 40)):
            self.lifeRect.drawGradientEffect(5,self.qtlife)
        else:
            self.lifeRect.drawGradientEffect(6, self.qtlife)