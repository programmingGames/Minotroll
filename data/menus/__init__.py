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
from data.skills import Skills
from data.player import Player
from data.plataforma import Plataform
from data.start import Initiation
from data.enimy.wizard import WizardSimpleAI as Wizard
from data.menus.map import Map


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
        self.pause = PauseMenu(self.screen)
        self.painelState = 0  # this is to control where we are in the game
        self.user = '' # keep the current user name
        self. nivel = 1 # default value of the level started usualy in 1 
        self.skills = 1 # default value of skills the player have
        self.lastPassPoint = 500 # default Value for position of the player in the platform
        self.player_rect = pygame.Rect(0, 0, 0, 0) # To control the player rects
        self.scroll = [0, 0]  # Variable to control the scroll of the screen
        self.pygameEvent = 0 # to keep all the pygame.event in the game loop

        # test
        self.wizard = Wizard(self.screen)

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
        if(key[K_TAB]):
            exit()

        if(self.painelState==0):
            self.painelState = self.initiation.settingStart()
        if(self.painelState == 1):
            self.painelState = self.mainMenu.movingInMainMenu()
        elif(self.painelState == 2):
            self.painelState, self.user = self.createUser.drawUserMenu(self.pygameEvent)
            self.player = Player(self.screen, self.nivel, self.skills,self.lastPassPoint)
        elif(self.painelState == 3):
            self.painelState, self.nivel, self.skills, self.lastPassPoint = self.userMenu.movingInUserMenu(self.user)
            self.player = Player(self.screen, self.nivel, self.skills,self.lastPassPoint)
            self.skills = Skills(self.screen, self.nivel)
            self.map = Map(self.screen, self.nivel)
        elif(self.painelState == 6):
            self.painelState = self.intro.introDisplay()
        elif(self.painelState == 5):
            self.painelState = self.exitMenu.movingInExitMenu()
        elif(self.painelState == 4):
            self.painelState, self.user = self.loadUser.movingInLoadMenu()
        elif(self.painelState == 7):
            plataforma = Plataform(self.screen)
            tile_rects, tile_item = plataforma.settingPlataform(self.scroll)
            self.scroll, player_rect = self.player.settingPlayer(self.pygameEvent, tile_rects,tile_item, self.scroll)
            wizard_rect = self.wizard.activation(self.pygameEvent, tile_rects, self.scroll, player_rect)
            # tile_rects.append(wizard_rect)
            tile_rects.append(player_rect)
        elif(self.painelState == 9):
            self.painelState = self.skills.movingInPainelSkills()
        elif (self.painelState == 8):
            self.painelState = self.pause.drawUserMenu()
        elif(self.painelState == 10):
            self.map.drawMapInTheScreen()
        # print(self.painelState)