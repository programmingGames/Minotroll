import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back

class PauseMenu(object):
    def __init__(self, screen):
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/painel1.png").convert_alpha()
        self.pauseText = "Game Pause"
        self.font = pygame.font.SysFont("Arial", 24)
        self.menuControl = 200
        self.count = 0
        self.timeEfect = 0
        self.buttoms = ['Continue','GameMenu', 'MainMenu']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(250, 200), (250, 250), (250, 300)]
        self.displayButtoms()

    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 30):
                    img = pygame.image.load("resources/image/menu/pause_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/pause_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/pause_menu/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)

    def settingPauseMenu(self):
        # self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (105, 100))
        self.font.set_bold(True)
        line = self.font.render(self.pauseText, True, (0, 0,0))
        self.screen.blit(line, (265, 150))

        # Controling menu buttons efects
        if (self.menuControl == 200):
            self.currentButtom = self.buttoms[0]
        elif(self.menuControl == 250):
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
            if(self.menuControl == 300):
                self.menuControl = 200
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl == 200):
                self.menuControl = 200
            else:
                self.menuControl -= 50

        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==200)and(self.count >= 5)):
            self.count = 0
            return 7
        elif((pressed_keys[K_RETURN])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 200
            return 3
        elif((pressed_keys[K_RETURN])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 200
            return 1

        self.settingPauseMenu()
        return 8