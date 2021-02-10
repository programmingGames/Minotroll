import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back
from sys import exit


class ExitMenu:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = "Do you realy wanna exit game?"
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 16)
        self.size = pygame.font.Font.size(self.font, self.createText)
        self.menuControl = 200
        self.timeEfect = 0
        self.buttoms = ["Yes", "No"]
        self.currentButtom = self.buttoms[0]
        self.alllButtoms = []
        self.allPosition = []
        self.displayButtoms()
        self.count = 0
        

    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 270
        y = 200
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 265
            else:
                x = 270
                img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50

    def movingInExitMenu(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==250):
                self.menuControl = 200
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl==200):
                self.menuControl = 200
            else:
                self.menuControl -= 50

        self.count += 1
        if((pressed_keys[K_RETURN]  or pressed_keys[K_KP_ENTER])and(self.menuControl==200)and(self.count >= 5)):
            self.count = 0
            exit()
        elif ((pressed_keys[K_RETURN]  or pressed_keys[K_KP_ENTER])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            return False        
                
        self.exitMenuEsc()  
        return True
    def exitMenuEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (150, 70))
        self.screen.blit(self.title, (275, 90))
        self.font.set_bold(True)
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, ((700/2-self.size[0]/2)-7, 150))

        if(self.menuControl == 200):
            self.currentButtom = self.buttoms[0]
        elif(self.menuControl == 250):
            self.currentButtom = self.buttoms[1]


        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]