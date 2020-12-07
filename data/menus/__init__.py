import pygame
from pygame.locals import *
from sys import exit
from data.backgrounds import Backgound as Back
from data.menus.createUser import CreateUserMenu
from data.menus.exitMenu import ExitMenu 
from data.menus.mainMenu import MainMenu
from data.menus.intro import Intro

#  Class for controling all the menu on the game
class Menus(object):
    def __init__(self, screen, backgroundImage, painelState, nivel):
        self.screen = screen
        self.painelState = painelState
        self.createUser = CreateUserMenu(screen, backgroundImage,painelState, nivel)
        self.exitMenu = ExitMenu(screen)
        self.mainMenu = MainMenu(screen, backgroundImage, painelState, nivel)
        self.intro = Intro(screen, backgroundImage, painelState, nivel)

    # Method to move in the main menu
    # screenState == painelState
    def interMenuMoving(self, screenState, event):
        self.painelState = screenState
        # print(self.painelState)
        if(self.painelState == 1):
            self.painelState = self.mainMenu.movingInMainMenu()
        elif(self.painelState == 2):
            self.painelState = self.createUser.drawUserMenu(event)
        elif(self.painelState == 3):
            self.painelState = self.intro.introDisplay()
                 
        return self.painelState