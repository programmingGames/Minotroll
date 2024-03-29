import pygame
from pygame.locals import *
from sys import exit
import os
from data.music import Sounds
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
from data.menus.levelincomplet import LevelIncompleted
from data.menus.settings import Settings
from data.menus.controls import Controls
from data.menus.congrats import Congrats
from data.menus.delete import Delete
from data.gameplay import GamePlay


#  Class for controling all the menu on the game
class Menus(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 480), 0, 32)
        pygame.display.set_caption("Minotroll")
        self.painelState = 0
        self.sounds = Sounds()
        self.createUser = CreateUserMenu(self.screen)
        self.exitMenu = ExitMenu(self.screen)
        self.mainMenu = MainMenu(self.screen)
        self.intro = Intro(self.screen)
        self.userMenu = UserMenu(self.screen)
        self.loadUser = LoadUser(self.screen)
        self.initiation = Initiation(self.screen)
        self.gameOver = GameOver(self.screen)
        self.delete = Delete(self.screen)
        self.soundControl = None
        self.musicControl = None
        self.readSoundsState()
        self.settings = Settings(self.screen, self.soundControl, self.musicControl)
        self.levelComplet = LevelComplet(self.screen)
        self.levelincompleted = LevelIncompleted(self.screen)
        self.pause = PauseMenu(self.screen)
        self.controls = Controls(self.screen)
        self.congrats = Congrats(self.screen)
        self.player_rect = pygame.Rect(0, 0, 0, 0)
        self.cardsActive = None
        self.count = 0
        self.suport = 0
        self.painelState = 0  # this is to control where we are in the game
        self.user = '' # keep the current user name
        self.pygameEvent = 0 # to keep all the pygame.event in the game loop
        self.complet = False
        self.qtlife = 0
        self.greenFire = 0
        self.blueFire = 0
        self.currentenimysKilled = 0

    # Method to control the sounds state
    def readSoundsState(self):
        file = open("data/menus/mainMenu/soundState.txt", 'r')
        data = file.read()
        file.close()
        states = data.split(' ')
        self.soundControl = int(states[0])
        self.musicControl = int(states[1])


    # Method to move in the main menu
    def interMenuMoving(self):
        for event in pygame.event.get():
            self.pygameEvent = event
            if event.type == QUIT:
                pygame.time.delay(10)
                self.suport = self.painelState
                if(self.painelState == 7):
                    self.saveUserData()
                self.painelState = 5
        key = pygame.key.get_pressed()
        ## Controling the map display in the game Envirement
        if((key[K_m])and(self.painelState == 7)and(self.count >= 10)):
            self.painelState = 10
            self.count = 0
        elif((key[K_m] or key[K_ESCAPE])and(self.painelState == 10)and(self.count >= 10)):
            self.painelState = 7
            self.count = 0

        self.count += 1

        if(self.painelState==0):
            self.painelState = self.initiation.settingStart()
        if(self.painelState == 1):
            self.painelState = self.mainMenu.movingInMainMenu()
        elif(self.painelState == 2):
            self.painelState, self.user = self.createUser.drawUserMenu()
            # self.player = Player(self.screen, self.nivel, self.skills,self.lastPassPoint)
        elif(self.painelState == 3):
            self.painelState = self.userMenu.movingInUserMenu(self.user)
            if self.painelState != 3:
                self.getUpdateUserData()
        elif(self.painelState == 6):
            self.painelState = self.intro.introDisplay()
        elif(self.painelState == 5):
            if self.exitMenu.movingInExitMenu():
                self.painelState = 5
            else:
                pygame.time.delay(10)
                self.painelState = self.suport
        elif(self.painelState == 4):
            self.painelState, self.user = self.loadUser.movingInLoadMenu()
        elif(self.painelState == 7):
            self.painelState, self.player_rect, self.qtlife, self.currentenimysKilled, self.greenFire, self.blueFire = self.gamplay.drawingTheGamePlayEnvirement(self.soundControl, self.musicControl)
            self.map.updateProgressInMap(self.player_rect.x)
            self.saveUserData()
            if self.painelState != 7:
                self.userMenu = UserMenu(self.screen)
        elif(self.painelState == 9):
            self.painelState, self.cardsActive = self.skills.movingInPainelSkills()
        elif (self.painelState == 8):
            self.painelState = self.pause.drawUserMenu()
            self.saveUserData()
        elif(self.painelState == 10):
            self.map.drawMapInTheScreen()
        elif(self.painelState == 11):
            self.updatingUserData()
            self.painelState, self.complet = self.gameOver.showGameOverPainel()
        elif(self.painelState == 13):
            self.painelState, self.complet = self.levelComplet.drawingLevelCompletPainel(self.currentenimysKilled)
        elif(self.painelState == 12):
            self.updatingUserData()
            self.getUpdateUserData()
            self.painelState = 7
        elif(self.painelState == 14):
            self.updatingUserData()
            self.getUpdateUserData()
            self.painelState = 7
        elif(self.painelState == 20):
            self.painelState, self.soundControl, self.musicControl = self.settings.movingInSettingsMenu()
        elif(self.painelState == 21):
            self.painelState = self.controls.settingControls()
        elif(self.painelState == 18):
            self.painelState, self.complet = self.levelincompleted.showPainel(self.currentenimysKilled)
        elif(self.painelState == 19):
            self.painelState, self.complet = self.congrats.drawingcongratsPainel()

        elif(self.painelState == 17):
            self.painelState = self.delete.movingInDeleteMenu(self.user)
        self.chekingSoundsToPlay()

    # Methdo to control the sounds
    def chekingSoundsToPlay(self):
        key = pygame.key.get_pressed()
        if self.soundControl:
            if self.painelState == 0:
                self.sounds.startSounds()
            elif(((key[K_UP])or(key[K_DOWN]))and(self.painelState!=7 and self.painelState!=0)):
                self.sounds.upDownMenu()
            elif((key[K_RETURN])and(self.painelState!=7 and self.painelState!=0)):
                self.sounds.selected()
            elif(((key[K_RIGHT])or(key[K_LEFT]))and(self.painelState == 9)and self.cardsActive):
                self.sounds.skillschange()
        if self.musicControl and self.painelState != 7:
            self.sounds.menubackSong()
        else:
            self.sounds.menuBackSongStop()
    
    # Method to control the user data update if the level is completed or not
    def updatingUserData(self):
        if not self.complet:
            # setting the user data in the defaul level start
            os.chdir('users/'+self.user)
            # os.remove('data.txt')
            file = open('data.txt', 'w')
            #          nivel      Position   Initial Life
            if(self.nivel == 0):
                file.write(str(self.nivel)+' '+str(500)+' '+str(120)+' '+str(218)+' '+str(0)+' '+str(0)+' '+str(0))
            elif(self.nivel == 1):
                file.write(str(self.nivel)+' '+str(500)+' '+str(88)+' '+str(218)+' '+str(0)+' '+str(5)+' '+str(0))
            elif(self.nivel == 2):
                file.write(str(self.nivel)+' '+str(500)+' '+str(440)+' '+str(218)+' '+str(0)+' '+str(10)+' '+str(5))
            elif(self.nivel == 3):
                file.write(str(self.nivel)+' '+str(500)+' '+str(200)+' '+str(218)+' '+str(0)+' '+str(10)+' '+str(5))
            file.close()
            os.chdir('../..')
            
        else:
            os.chdir('users/'+self.user)
                # os.remove('data.txt')
            file = open('data.txt', 'w')
            if self.nivel < 3:
                self.nivel += 1
                #          nivel      Position   Initial Life
                if(self.nivel == 1):
                    file.write(str(self.nivel)+' '+str(500)+' '+str(88)+' '+str(218)+' '+str(0)+' '+str(5)+' '+str(0))
                elif(self.nivel == 2):
                    file.write(str(self.nivel)+' '+str(500)+' '+str(440)+' '+str(218)+' '+str(0)+' '+str(10)+' '+str(5))
                else:
                    file.write(str(self.nivel)+' '+str(500)+' '+str(120)+' '+str(218)+' '+str(0)+' '+str(10)+' '+str(5))
                
                self.complet = not self.complet
            else:
                file.write(str(self.nivel)+' '+str(self.player_rect.x)+' '+str(self.player_rect.y)+' '+str(self.qtlife)+' '+str(self.enimysKilled+self.currentenimysKilled)+' '+str(self.greenFire)+' '+str(self.blueFire))
            os.chdir('../..')
            file.close()
            self.getUpdateUserData()
            # restarting the game whit new data
        
    # Method that save the user data
    def saveUserData(self):
        os.chdir('users/'+self.user)
        file = open('data.txt', 'w')
        #          nivel      Position   Initial Life
        file.write(str(self.nivel)+' '+str(self.player_rect.x)+' '+str(self.player_rect.y)+' '+str(self.qtlife)+' '+str(self.enimysKilled+self.currentenimysKilled)+' '+str(self.greenFire)+' '+str(self.blueFire))
        file.close()
        os.chdir('../..')

    # Method that get the update user data
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
        self.enimysKilled = int(allUserData[4])
        self.greenFire = int(allUserData[5])
        self.blueFire = int(allUserData[6])
        # restarting the game whit new data
        self.gamplay = GamePlay(self.screen, self.nivel, self.lastPassPoint,self.qtlife, self.pygameEvent, self.enimysKilled, self.greenFire, self.blueFire)
        self.skills = Skills(self.screen, self.nivel)
        self.map = Map(self.screen, self.nivel)
        