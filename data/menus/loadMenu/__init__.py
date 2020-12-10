import pygame 
import os
from pygame.locals import *
from data.backgrounds import Backgound as Back


class LoadUser(object):
    def __init__(self, screen, backgroundImage, painelState, nivel):
        self.screen = screen
        self.background = Back(backgroundImage, painelState, nivel)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = "Chose or user game"
        self.font = pygame.font.SysFont("Arial", 24)
        self.currentButtom = ''
        self.users = []
        self.allUser()
        self.menuControl = 150
        self.timeEfect = 0
        self.allButtom = []

    def displayButtoms(self):
        self.allButtom = []
        for user in self.users:
            if(self.currentButtom == user):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/initial_menu/"+user+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/initial_menu/"+user+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/initial_menu/"+user+"0.png").convert_alpha()
            self.allButtom.append(img)

    def movingInLoadMenu(self):
        self.draw()
        
        return 4
    
    def draw(self):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        self.font.set_bold(True)
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, (265, 150))
    
    def allUser(self):
        if(len(os.listdir('users')) == 0):
            pass
        else:
            self.users = os.listdir('users')
            self.currentButtom = self.users[0]    