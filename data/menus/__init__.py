import pygame
from pygame.locals import *
from sys import exit
from data.backgrounds import Backgound as Back
from data.menus.createUser import CreateUserMenu
from data.menus.exitMenu import ExitMenu 
from data.menus.mainMenu import MainMenu
from data.menus.userMenu import UserMenu
from data.menus.intro import Intro
from data.menus.loadMenu import LoadUser

#  Class for controling all the menu on the game
class Menus(object):
    def __init__(self, screen, painelState):
        self.screen = screen
        self.painelState = painelState
        self.createUser = CreateUserMenu(screen)
        self.exitMenu = ExitMenu(screen)
        self.mainMenu = MainMenu(screen)
        self.intro = Intro(screen)
        self.userMenu = UserMenu(screen)
        self.loadUser = LoadUser(screen)
        self.user = ''

    # Method to move in the main menu
    def interMenuMoving(self, screenState, event):
        self.event = event
        self.painelState = screenState
        # print(self.painelState)
        if(self.painelState == 1):
            self.painelState = self.mainMenu.movingInMainMenu()
        elif(self.painelState == 2):
            self.painelState = self.createUser.drawUserMenu(self.event)
        elif(self.painelState == 3):
            self.painelState = self.userMenu.movingInUserMenu(self.user)
        elif(self.painelState == 6):
            self.painelState = self.intro.introDisplay()
        elif(self.painelState == 5):
            self.painelState = self.exitMenu.movingInExitMenu()
        elif(self.painelState == 4):
            self.painelState, self.user = self.loadUser.movingInLoadMenu()
                 
        return self.painelState