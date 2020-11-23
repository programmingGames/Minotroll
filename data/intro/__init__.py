import pygame 
from data import intro
from data.backgrounds import Backgound as Back
from data import Hysto 
class Intro(object):
    def __init__(self, screen, nrImage):
        self.background = Back(nrImage)
        self.screen = screen
        self.history = Hysto()
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 12,1)
        self.timeout = 0


    def introDisplay(self):

        tx, ty = 165, 120
        for paragrafo in self.history.historyData():
            self.background.settingBackground(self.screen)
            self.screen.blit(self.painel, (105, 70))
            self.screen.blit(self.title, (210, 10))
            if(self.timeout >= 50):
                    self.screen.fill((0, 0, 0))
                    self.timeout = 0
            for line in paragrafo:
                line = self.font.render(line, True, (0, 0,0))
                self.screen.blit(line, (tx, ty))
                ty += 15
            #parControl += 1
            ty=165
        self.timeout += 1
        print(self.timeout)
        return 3
