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
        self.font = pygame.font.SysFont("Arial", 24)
        

    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)

    def movingInExitMenu(self, suport):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_RIGHT]):
            pygame.time.delay(100)
            if(self.menuControl==380):
                self.menuControl = 380
            else:
                self.menuControl += 150
        elif(pressed_keys[K_LEFT]):
            pygame.time.delay(100)
            if(self.menuControl==230):
                self.menuControl = 230
            else:
                self.menuControl -= 150


        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==230)and(self.count >= 5)):
            self.count = 0
            exit()
        elif ((pressed_keys[K_RETURN])and(self.menuControl==380)and(self.count >= 5)):
            self.count = 0
            return suport
        
                
        self.exitMenuEsc()  
        return 5
    def exitMenuEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        self.font.set_bold(True)
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, (170, 200))

        if(self.menuControl == 230):
            self.currentButtom = self.buttoms[0]
        elif(self.menuControl == 380):
            self.currentButtom = self.buttoms[1]


        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]