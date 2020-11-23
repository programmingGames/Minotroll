import pygame 
from data import intro
from data.backgrounds import Backgound as Back
from data import Hysto 
class Intro(object):
    def __init__(self, screen, nrImage, menuEsc, nivel):
        self.background = Back(nrImage, menuEsc, nivel)
        self.screen = screen
        self.history = Hysto()
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 12,1)
        self.timeout = 0
        self.next_t = True

    def iterationCount(self):
        l_control = 0
        soma = 0
        for paragrafo in self.history.historyData():
            # self.background.settingBackground(self.screen)
            # self.screen.blit(self.painel, (105, 70))
            # self.screen.blit(self.title, (210, 10))
            for line in paragrafo:
                l_control = len(paragrafo)
                soma += l_control 
                # line = self.font.render(line, True, (0, 0,0))
                # self.screen.blit(line, (tx, ty))
                # ty += 15
        soma += len(self.history.historyData())
        return soma

    def introDisplay(self):
        tx, ty = 165, 140
        p_control = len(self.history.historyData())
        p_t = 0
        if((self.timeout == 200)):
            self.next_t=False
            self.timeout = 0
        else:
            self.next_t=True

        soma = self.iterationCount()
        
        # for i in range soma:

        #     for paragrafo in self.history.historyData():
        #         # self.background.settingBackground(self.screen)
        #         # self.screen.blit(self.painel, (105, 70))
        #         # self.screen.blit(self.title, (210, 10))
        #         for line in paragrafo:
        #             # line = self.font.render(line, True, (0, 0,0))
        #             # self.screen.blit(line, (tx, ty))
        #             # ty += 15
        
            
        ty=165
        # print(self.timeout)
        self.timeout += 1
        return 4
