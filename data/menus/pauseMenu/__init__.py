import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back

class PauseMenu(object):
    def __init__(self, screen):
        self.screen = screen
        self.background = Back(screen)
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 24)
        self.menuControl = 300
        self.count = 0
        self.timeEfect = 0
        self.buttoms = ['Continue','Game Menu', 'Main Menu']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(250, 200), (250, 250), (250, 300)]
        self.displayButtoms()

    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 265
        y = 300
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/pause_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/pause_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 260
            else:
                x = 265
                img = pygame.image.load("resources/image/menu/pause_menu/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50

    def settingPauseMenu(self):
        # self.background.settingBackgroundMenu(2)
        self.back = pygame.image.load("resources/image/menu/pause_menu/back.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))

        # Controling menu buttons efects
        if (self.menuControl == 300):
            self.currentButtom = self.buttoms[0]
        elif(self.menuControl == 350):
            self.currentButtom = self.buttoms[1]
        else:
            self.currentButtom = self.buttoms[2]
        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

    # Method to move in this menu and return the choose
    def drawUserMenu(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl == 400):
                self.menuControl = 300
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl == 300):
                self.menuControl = 300
            else:
                self.menuControl -= 50

        self.count += 1
        if((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            return 7
        elif((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==350)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 300
            return 3
        elif((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==400)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 300
            return 1

        self.settingPauseMenu()
        return 8