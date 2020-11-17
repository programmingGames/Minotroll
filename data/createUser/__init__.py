import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back
from data.textInput import Textinput as textInput

class CreateUser:
    def __init__(self, screen, nrImage):
        self.screen = screen
        self.background = Back(nrImage)
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha() 
        self.text = textInput()
    def settingUserName(self, event):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (100, 60))
        self.text.settingInputText(self.screen, event)
