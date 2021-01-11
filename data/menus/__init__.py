import pygame
from pygame.locals import *
from sys import exit
import os
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
from data.menus.levelComplet import LevelComplet
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
        self.levelComplet = LevelComplet(self.screen)
        self.pause = PauseMenu(self.screen)
        self.player_rect = pygame.Rect(0, 0, 0, 0)
        self.count = 0
        self.suport = 0
        self.painelState = 0  # this is to control where we are in the game
        self.user = '' # keep the current user name
        self.pygameEvent = 0 # to keep all the pygame.event in the game loop
        self.complet = False

        
    # Method to move in the main menu
    def interMenuMoving(self):
        for event in pygame.event.get():
            self.pygameEvent = event
            if event.type == QUIT:
                self.suport = self.painelState
                if(self.painelState == 7):
                    self.saveUserData()
                self.painelState = 5
        key = pygame.key.get_pressed()
        if((key[K_ESCAPE])and(self.painelState == 7)):
            self.saveUserData()
            self.painelState = 8
        ## Controling the map display in the game Envirement
        elif((key[K_m])and(self.painelState == 7)and(self.count >= 10)):
            self.painelState = 10
            self.count = 0
        elif((key[K_m])and(self.painelState == 10)and(self.count >= 10)):
            self.painelState = 7
            self.count = 0

        if(key[K_KP_ENTER]):
            exit()
        self.count += 1

        if(self.painelState==0):
            self.painelState = self.initiation.settingStart()
        if(self.painelState == 1):
            self.painelState = self.mainMenu.movingInMainMenu()
        elif(self.painelState == 2):
            self.painelState, self.user = self.createUser.drawUserMenu(self.pygameEvent)
            # self.player = Player(self.screen, self.nivel, self.skills,self.lastPassPoint)
        elif(self.painelState == 3):
            self.painelState, self.user, self.nivel, self.lastPassPoint, self.qtlife = self.userMenu.movingInUserMenu(self.user)
            # self.getUpdateUserData()
            self.gamplay = GamePlay(self.screen, self.nivel, self.lastPassPoint, self.qtlife, self.pygameEvent)
            self.skills = Skills(self.screen, self.nivel)
            self.map = Map(self.screen, self.nivel)
            self.map.updateProgressInMap(self.lastPassPoint[0])

        elif(self.painelState == 6):
            self.painelState = self.intro.introDisplay()
        elif(self.painelState == 5):
            if self.exitMenu.movingInExitMenu():
                self.painelState = 5
            else:
                self.painelState = self.suport
        elif(self.painelState == 4):
            self.painelState, self.user = self.loadUser.movingInLoadMenu()
        elif(self.painelState == 7):
            self.painelState, self.player_rect, self.qtlife = self.gamplay.drawingTheGamePlayEnvirement()
            # updating the map progress
            self.map.updateProgressInMap(self.player_rect.x)
        elif(self.painelState == 9):
            self.painelState = self.skills.movingInPainelSkills()
        elif (self.painelState == 8):
            self.painelState = self.pause.drawUserMenu()
        elif(self.painelState == 10):
            self.map.drawMapInTheScreen()
        elif(self.painelState == 11):
            self.getUpdateUserData()
            self.painelState, self.complet = self.gameOver.showGameOverPainel()
        elif(self.painelState == 13):
            self.painelState, self.complet = self.levelComplet.drawingLevelCompletPainel()
        elif(self.painelState == 12):
            self.updatingUserData()
            self.painelState = 7
        elif(self.painelState == 14):
            self.updatingUserData()
            self.painelState = 7

        ## controling atribute self.user
        if(len(os.listdir('users')) == 0):
            self.user=''


    def updatingUserData(self):
        if not self.complet:
            # setting the user data in the defaul level start
            os.chdir('users/'+self.user)
            # os.remove('data.txt')
            file = open('data.txt', 'w')
            #          nivel      Position   Initial Life
            if(self.nivel == 0):
                file.write(str(self.nivel)+' '+str(500)+' '+str(120)+' '+str(240))
            elif(self.nivel == 1):
                file.write(str(self.nivel)+' '+str(500)+' '+str(88)+' '+str(240))
            elif(self.nivel == 2):
                file.write(str(self.nivel)+' '+str(500)+' '+str(440)+' '+str(240))
            elif(self.nivel == 3):
                file.write(str(self.nivel)+' '+str(500)+' '+str(200)+' '+str(240))
            file.close()
            os.chdir('../..')
            
        else:
            self.nivel += 1
            os.chdir('users/'+self.user)
            # os.remove('data.txt')
            file = open('data.txt', 'w')
            #          nivel      Position   Initial Life
            if(self.nivel == 1):
                file.write(str(self.nivel)+' '+str(500)+' '+str(88)+' '+str(240))
            elif(self.nivel == 2):
                file.write(str(self.nivel)+' '+str(500)+' '+str(440)+' '+str(240))
            elif(self.nivel == 3):
                file.write(str(self.nivel)+' '+str(500)+' '+str(200)+' '+str(240))
            file.close()
            os.chdir('../..')
            self.complet = not self.complet
            # restarting the game whit new data
        # restarting the game whit new data
        self.gamplay = GamePlay(self.screen, self.nivel, self.lastPassPoint,self.qtlife, self.pygameEvent)
        self.skills = Skills(self.screen, self.nivel)
        self.map = Map(self.screen, self.nivel)

    def saveUserData(self):
        os.chdir('users/'+self.user)
        file = open('data.txt', 'w')
        #          nivel      Position   Initial Life
        file.write(str(self.nivel)+' '+str(self.player_rect.x)+' '+str(self.player_rect.y)+' '+str(self.qtlife))
        file.close()
        os.chdir('../..')
        # self.getUpdateUserData()

    def getUpdateUserData(self):
        file = open('users/'+self.user+'/data.txt', 'r')
        data = file.read()
        file.close()
        allUserData = data.split(' ')
        self.nivel = int(allUserData[0])    # The current level of the player 
        lastPassPoint_x = int(allUserData[1])   # the last point in the game tha the user pass to in x
        lastPassPoint_y = int(allUserData[2])   # the last point in the game tha the user pass to in y
        self.lastPassPoint = (lastPassPoint_x, lastPassPoint_y)
        self.qtlife = int(allUserData[3])  # the last quantity of life save by the user