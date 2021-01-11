import pygame
from pygame.locals import *


class GameOver(object):
    def __init__(self, screen):
        self.screen = screen
        self.back = pygame.image.load("resources/image/menu/gamOver/back.png").convert_alpha()
        self.title = pygame.image.load("resources/image/menu/gamOver/3.png").convert_alpha()
        self.buttoms = ['Restart','GameMenu']
        self.currentButtom = self.buttoms[0]
        self.menuControl = 250
        self.allPosition = [(700/2-208/2, 250), (700/2-208/2, 300)]
        self.timeEfect = 0
        self.count = 0 

    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/gamOver/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/gamOver/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/gamOver/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)
    def gameOverMenuEsc(self):
        self.screen.blit(self.back, (0, 0))
        self.screen.blit(self.title, (700/2-350/2, 170))
        if (self.menuControl==250):
            self.currentButtom = self.buttoms[0]
        elif (self.menuControl==300):
            self.currentButtom = self.buttoms[1]

        self.displayButtoms()
        
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

    def showGameOverPainel(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==300):
                self.menuControl = 250
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl==250):
                self.menuControl = 250
            else:
                self.menuControl -= 50
        
        self.gameOverMenuEsc()
        choice = self.gameOverChoise(pressed_keys)
        # print(choice)
        return choice, False

    def gameOverChoise(self, pressed_keys):
        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            return 12
        elif ((pressed_keys[K_RETURN])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 250
            return 3
        return 11
