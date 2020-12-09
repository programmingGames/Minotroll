import pygame 
from data.menus import intro
from data.backgrounds import Backgound as Back
from data import Hysto 

class Intro(object):
    def __init__(self, screen, nrImage, menuEsc, nivel):
        self.background = Back(nrImage, menuEsc, nivel)
        self.screen = screen
        self.history = Hysto()
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 12,1)
        self.timeout = 0
        self.next = True
        self.change = 0

    def introDisplay(self):
        tx, ty = 165, 165
        paragrafoControl = 0
        if((self.timeout == 100)):
            self.timeout = 0
            self.change += 1

        for paragrafo in self.history.historyData():
            self.background.settingBackground(self.screen)
            self.screen.blit(self.painel, (105, 70))
            self.screen.blit(self.title, (275, 90))
            for line in paragrafo:
                line = self.font.render(line, True, (0, 0,0))
                self.screen.blit(line, (tx, ty))
                ty += 15
            if(self.change == paragrafoControl):
                break
            else:
                ty = 165
                paragrafoControl += 1
            
        if(self.change == 5):
            return 4
        else:
            self.timeout += 1
            return 3