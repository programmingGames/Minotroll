import pygame 
from data import intro
from data.backgrounds import Backgound as Back

class Intro(object):
    def __init__(self, screen, nrImage, menuEsc, nivel):
        self.screen = screen
        self.time = 0
        self.background = Back(nrImage, menuEsc, nivel)
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.SysFont(None, 32)
        self.text1 = "jknfjkwn"
        # self.parts =
        

    def introDisplay(self):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (210, 10))


        ##  write code 
        text_surf = self.font.render(self.text1, True, (0, 0, 0))
        self.screen.blit(text_surf, (200, 200))

        return 4
        # pygame.time.set_timer(self.NEW_BASIC_SOUL, 3000)