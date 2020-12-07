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
        self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame.png").convert_alpha()
        self.newGame1 = pygame.image.load("resources/image/menu/initial_menu/newGame1.png").convert_alpha()
        self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame.png").convert_alpha()
        self.loadGame1 = pygame.image.load("resources/image/menu/initial_menu/loadGame1.png").convert_alpha()
        self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame.png").convert_alpha()
        self.settings1 = pygame.image.load("resources/image/menu/initial_menu/SettingsGame1.png").convert_alpha()
        self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame.png").convert_alpha()
        self.quit1 = pygame.image.load("resources/image/menu/initial_menu/QuitGame1.png").convert_alpha()
        self.timeOut = 0
        self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Idle Blinking_"+str(self.timeOut)+".png")
        self.menuControl = 150
        

    # Method to choose option in main menu
    def mainMenuEsc(self):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        if (self.menuControl==150):
            self.screen.blit(self.newGame1, (145, 150))
            self.screen.blit(self.loadGame, (150, 200))
            self.screen.blit(self.settings, (150, 250))
            self.screen.blit(self.quit, (150, 300))

        elif (self.menuControl==200):
            self.screen.blit(self.newGame, (150, 150))
            self.screen.blit(self.loadGame1, (145, 200))
            self.screen.blit(self.settings, (150, 250))
            self.screen.blit(self.quit, (150, 300))

        elif (self.menuControl==250):
            self.screen.blit(self.newGame, (150, 150))
            self.screen.blit(self.loadGame, (150, 200))
            self.screen.blit(self.settings1, (145, 250))
            self.screen.blit(self.quit, (150, 300))

        elif (self.menuControl==300):
            self.screen.blit(self.newGame, (150, 150))
            self.screen.blit(self.loadGame, (150, 200))
            self.screen.blit(self.settings, (150, 250))
            self.screen.blit(self.quit1, (145, 300))

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
        if(self.timeOut==850):
            self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Idle Blinking_"+str(int(self.timeOut/50))+".png")
            self.timeOut = 0
        else:
            if ((self.timeOut % 50)==0):
                self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Idle Blinking_"+str(int(self.timeOut/50))+".png")
            self.timeOut += 1
        self.screen.blit(self.img, (420, 160))