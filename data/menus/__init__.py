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
from data.menus.pauseMenu import PauseMenu
from data.menus.skills import Skills
from data.menus.start import Initiation
from data.menus.map import Map
from data.menus.gameOver import GameOver
from data.gameplay import GamePlay


#  Class for controling all the menu on the game
class Menus(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 480), 0, 32)
        pygame.display.set_caption("Minotroll")
        self.painelState = 0
        self.createUser = CreateUserMenu(self.screen)
        self.exitMenu = ExitMenu(self.screen)
        self.mainMenu = MainMenu(self.screen)
        self.intro = Intro(self.screen)
        self.userMenu = UserMenu(self.screen)
        self.loadUser = LoadUser(self.screen)
        self.initiation = Initiation(self.screen)
        self.gameOver = GameOver(self.screen)
        self.pause = PauseMenu(self.screen)
        self.painelState = 0  # this is to control where we are in the game
        self.user = '' # keep the current user name
        self.pygameEvent = 0 # to keep all the pygame.event in the game loop

        
    # Method to move in the main menu
    def interMenuMoving(self):
        for event in pygame.event.get():
            self.pygameEvent = event
            if event.type == QUIT:
                exit()
        key = pygame.key.get_pressed()
        if((key[K_ESCAPE])and(self.painelState == 7)):
            self.painelState = 8
        elif((key[K_ESCAPE])and(self.painelState == 10)):
            self.painelState = 3
        if(key[K_KP_ENTER]):
            exit()

        if(self.painelState==0):
            self.painelState = self.initiation.settingStart()
        if(self.painelState == 1):
            self.painelState = self.mainMenu.movingInMainMenu()
        elif(self.painelState == 2):
            self.painelState, self.user = self.createUser.drawUserMenu(self.pygameEvent)
            # self.player = Player(self.screen, self.nivel, self.skills,self.lastPassPoint)
        elif(self.painelState == 3):
            self.painelState, self.nivel,self.lastPassPoint, self.qtlife = self.userMenu.movingInUserMenu(self.user)
            self.gamplay = GamePlay(self.screen, self.nivel, self.lastPassPoint,self.qtlife, self.pygameEvent)
            self.skills = Skills(self.screen, self.nivel)
            self.map = Map(self.screen, self.nivel)
        elif(self.painelState == 6):
            self.painelState = self.intro.introDisplay()
        elif(self.painelState == 5):
            self.painelState = self.exitMenu.movingInExitMenu()
        elif(self.painelState == 4):
            self.painelState, self.user = self.loadUser.movingInLoadMenu()
        elif(self.painelState == 7):
            self.painelState = self.gamplay.drawingTheGamePlayEnvirement()
        elif(self.painelState == 9):
            self.painelState = self.skills.movingInPainelSkills()
        elif (self.painelState == 8):
            self.painelState = self.pause.drawUserMenu()
        elif(self.painelState == 10):
            self.map.drawMapInTheScreen()
        elif(self.painelState == 11):
            self.gameOver.showGameOverPainel()
        # print(self.painelState)