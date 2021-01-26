import pygame 
from pygame.locals import *
from data.menus import intro
from data.backgrounds import Backgound as Back
from data import Hysto 

class Intro(object):
    def __init__(self, screen):
        self.background = Back(screen)
        self.screen = screen
        self.history = Hysto()
        self.painel = pygame.image.load("resources/image/menu/intro/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 11)
        self.esc = 'Press "Esc" to go back'
        self.font1 = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
        self.timeEfect1 = 0
        self.timeout = 0
        self.next = True
        self.change = 0

    def introDisplay(self):
        self.font.set_bold(True)
        key=pygame.key.get_pressed()
        ty = 165
        self.restart()
        paragrafoControl = 0
        if((self.timeout == 100)):
            self.timeout = 0
            self.change += 1

        for paragrafo in self.history.historyData():
            self.background.settingBackgroundMenu(2)
            self.screen.blit(self.painel, (105, 70))
            self.screen.blit(self.title, (275, 90))
            for line in paragrafo:
                size = pygame.font.Font.size(self.font, str(line))
                line = self.font.render(line, True, (0, 0,0))
                self.screen.blit(line, ((700/2-size[0]/2)+10, ty))
                ty += 15
            if(self.change == paragrafoControl):
                break
            else:
                ty = 165
                paragrafoControl += 1

        # exit load menu
        self.font1.set_bold(True)
        size = pygame.font.Font.size(self.font1, self.esc)
        line = self.font1.render(self.esc, True, (255, 255, 255))

        ## blitting the esc evente 
        if (self.timeEfect1 > 5):
            self.timeEfect1 = 0
        else:
            self.screen.blit(line, ((700/2-size[0]/2)+10, 390))
            self.timeEfect1 += 1
        if((self.change == 5) or key[K_ESCAPE]):
            return 3
        else:
            self.timeout += 1
            return 6
    # To start the display of the story again
    def restart(self):
        if(self.change == 5):
            self.change = 0