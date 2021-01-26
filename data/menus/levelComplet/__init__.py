import pygame
from pygame.locals import *
from data.music import Sounds


class LevelComplet(object):
    
    def __init__(self, screen):
        self.screen = screen
        self.sounds = Sounds()
        self.buttoms = ['Next Level','Game Menu']
        self.currentButtom = self.buttoms[0]
        self.menuControl = 300
        self.allPosition = []
        self.timeEfect = 0
        self.count = 0 


    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 265
        y = 300
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/levelComplet/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/levelComplet/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 260
            else:
                x = 265
                img = pygame.image.load("resources/image/menu/levelComplet/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50

    def nextLevelMenuEsc(self):
        self.back = pygame.image.load("resources/image/menu/levelComplet/back.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))
        if (self.menuControl==300):
            self.currentButtom = self.buttoms[0]
        elif (self.menuControl==350):
            self.currentButtom = self.buttoms[1]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]


    def drawingLevelCompletPainel(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            self.sounds.upDownMenu()
            if(self.menuControl==350):
                self.menuControl = 300
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            self.sounds.upDownMenu()
            if(self.menuControl==300):
                self.menuControl = 300
            else:
                self.menuControl -= 50
        
        self.nextLevelMenuEsc()
        choice = self.nextLevelChoise(pressed_keys)
        # print(choice)
        return choice, True

    def nextLevelChoise(self, pressed_keys):
        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            self.sounds.selected()
            return 14
        elif ((pressed_keys[K_RETURN])and(self.menuControl==350)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 300
            self.sounds.selected()
            return 3
        return 13