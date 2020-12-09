import pygame
from pygame.locals import *
from sys import exit
from data.backgrounds import Backgound as Back

#  Class for controling all the menu on the game
class MainMenu(object):
    def __init__(self, screen, backgroundImage, painelState, nivel):
        self.screen = screen
        self.nivel = nivel
        self.background = Back(backgroundImage, painelState, nivel)
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        # self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame0.png").convert_alpha()
        # self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame0.png").convert_alpha()
        # self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame0.png").convert_alpha()
        # self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame0.png").convert_alpha()
        self.timeOut = 0
        self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Walking_"+str(self.timeOut)+".png")
        self.menuControl = 150
        self.timeEfect = 0
        self.imgNumber = 0
        self.buttoms = ['newGame','loadGame', 'SettingsGame', 'QuitGame']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(145, 150), (150, 200), (150, 250), (150, 300)]
        self.displayButtoms()
        

    # Method to choose option in main menu
    def displayButtoms(self):
        # if (self.timeEfect == 10):
        #     self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame1.png").convert_alpha()
        #     self.timeEfect = 0
        # else:
        #     self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame2.png").convert_alpha()
        #     self.timeEfect += 1
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                img = pygame.image.load("resources/image/menu/initial_menu/"+buttom+"1.png").convert_alpha()
            else:
                img = pygame.image.load("resources/image/menu/initial_menu/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)
    def blitingMenu(self):
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

    def newGameDisplay(self):
        if (self.timeEfect == 10):
            self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame1.png").convert_alpha()
            self.timeEfect = 0
        else:
            self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame2.png").convert_alpha()
            self.timeEfect += 1
        self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame0.png").convert_alpha()
        self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame0.png").convert_alpha()
        self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame0.png").convert_alpha()

    def loadGameDisplay(self):
        if (self.timeEfect == 10):
            self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame1.png").convert_alpha()
            self.timeEfect = 0
        else:
            self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame2.png").convert_alpha()
            self.timeEfect += 1 
        self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame0.png").convert_alpha()
        self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame0.png").convert_alpha()
        self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame0.png").convert_alpha()
        
    def settingsDisplay(self):
        if (self.timeEfect == 10):
            self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame1.png").convert_alpha()
            self.timeEfect = 0
        else:
            self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame2.png").convert_alpha()
            self.timeEfect += 1
        self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame0.png").convert_alpha()
        self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame0.png").convert_alpha()
        self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame0.png").convert_alpha()
        
    def quitDisplay(self):
        if (self.timeEfect == 10):
            self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame1.png").convert_alpha()
            self.timeEfect = 0
        else:
            self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame2.png").convert_alpha()
            self.timeEfect += 1
        self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame0.png").convert_alpha()
        self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame0.png").convert_alpha()
        self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame0.png").convert_alpha()
        

    def mainMenuEsc(self):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))

        if (self.menuControl==150):
            # self.newGameDisplay()
            self.currentButtom = self.buttoms[0]
        elif (self.menuControl==200):
            # self.loadGameDisplay()
            self.currentButtom = self.buttoms[1]

        elif (self.menuControl==250):
            # self.settingsDisplay()
            self.currentButtom = self.buttoms[2]

        elif (self.menuControl==300):
            # self.quitDisplay()
            self.currentButtom = self.buttoms[3]
            
        self.displayButtoms()
        self.blitingMenu()

        # self.screen.blit(self.newGame, (145, 150))
        # self.screen.blit(self.loadGame, (150, 200))
        # self.screen.blit(self.settings, (150, 250))
        # self.screen.blit(self.quit, (150, 300))
    # Method to move in the main menu
    def movingInMainMenu(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==300):
                self.menuControl = 150
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl==150):
                self.menuControl = 150
            else:
                self.menuControl -= 50

        if((pressed_keys[K_x])and(self.menuControl==150)):
            return 2
        elif ((pressed_keys[K_x])and(self.menuControl==200)):
            return 3
        elif ((pressed_keys[K_x])and(self.menuControl==250)):
            return 4
        elif ((pressed_keys[K_x])and(self.menuControl==300)):
            return 5
        
        self.mainMenuEsc()  
        self.golemAnimation()
        return 1

    def golemAnimation(self):
        if(self.timeOut==230):
            self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Walking_"+str(int(self.timeOut/10))+".png")
            self.timeOut = 0
        else:
            if ((self.timeOut % 10)==0):
                self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Walking_"+str(int(self.timeOut/10))+".png")
            self.timeOut += 1
        self.screen.blit(self.img, (420, 160))