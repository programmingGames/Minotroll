import pygame
from pygame.locals import *
from sys import exit
from data.backgrounds import Backgound as Back

#  Class for controling all the menu on the game
class MainMenu(object):
    def __init__(self, screen, backgroundImage):
        self.screen = screen
        self.background = Back(backgroundImage)
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.newGame = pygame.image.load("resources/image/menu/initial_menu/newGame.png").convert_alpha()
        self.newGame1 = pygame.image.load("resources/image/menu/initial_menu/newGame1.png").convert_alpha()
        self.loadGame = pygame.image.load("resources/image/menu/initial_menu/loadGame.png").convert_alpha()
        self.loadGame1 = pygame.image.load("resources/image/menu/initial_menu/loadGame1.png").convert_alpha()
        self.settings = pygame.image.load("resources/image/menu/initial_menu/SettingsGame.png").convert_alpha()
        self.settings1 = pygame.image.load("resources/image/menu/initial_menu/SettingsGame1.png").convert_alpha()
        self.quit = pygame.image.load("resources/image/menu/initial_menu/QuitGame.png").convert_alpha()
        self.quit1 = pygame.image.load("resources/image/menu/initial_menu/QuitGame1.png").convert_alpha()
        pass
    # Method for rendering items on the screen
    def startingMenu(self, screen):
        self.background.settingBackground(self.screen)
        screen.blit(self.painel, (100, 60))
        pass

    # Method to choose option in main menu
    def mainMenuEsc(self, screen, menuControl):
        if (menuControl==150):
            screen.blit(self.newGame1, (145, 150))
            screen.blit(self.loadGame, (150, 200))
            screen.blit(self.settings, (150, 250))
            screen.blit(self.quit, (150, 300))

        elif (menuControl==200):
            screen.blit(self.newGame, (150, 150))
            screen.blit(self.loadGame1, (145, 200))
            screen.blit(self.settings, (150, 250))
            screen.blit(self.quit, (150, 300))

        elif (menuControl==250):
            screen.blit(self.newGame, (150, 150))
            screen.blit(self.loadGame, (150, 200))
            screen.blit(self.settings1, (145, 250))
            screen.blit(self.quit, (150, 300))

        elif (menuControl==300):
            screen.blit(self.newGame, (150, 150))
            screen.blit(self.loadGame, (150, 200))
            screen.blit(self.settings, (150, 250))
            screen.blit(self.quit1, (145, 300))

    # Method to move in the main menu
    def movingInMainMenu(self, screen, pressed_keys, menuControl):
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(menuControl==300):
                menuControl = 150
            else:
                menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(menuControl==150):
                menuControl = 150
            else:
                menuControl -= 50
        elif pressed_keys[K_ESCAPE]:
            exit()
        self.mainMenuEsc(screen, menuControl)       
        return menuControl
        pass
    pass