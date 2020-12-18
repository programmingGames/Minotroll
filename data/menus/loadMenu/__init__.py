import pygame 
import os
from pygame.locals import *
from data.backgrounds import Backgound as Back


class LoadUser(object):
    def __init__(self, screen):
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = "Chose your user name"
        self.font = pygame.font.SysFont("Arial", 24)
        self.currentButtom = ''
        self.users = []
        self.allUser()
        self.menuControl = 200
        self.timeEfect = 0
        self.count = 0
        self.allButtom = []
        self.allPosition = [(250, 200), (250, 250), (250, 300), (250, 350)]
        self.displayButtoms()
        self.nrUser = len(self.users)
        self.maxScroll = self.menuControl+(self.nrUser * 50)

    def displayButtoms(self):
        self.allButtom = []
        for user in self.users:
            if(self.currentButtom == user):
                if (self.timeEfect == 10):
                    img = pygame.image.load("users/"+user+"/"+user+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("users/"+user+"/"+user+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("users/"+user+"/"+user+"0.png").convert_alpha()
            self.allButtom.append(img)

    def loadMenuEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        self.font.set_bold(True)
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, (215, 150))

        for i in range(len(self.users)):
            if(self.menuControl == ((i*50)+200)):
                self.currentButtom = self.users[i]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]


# there is a problem here then you shoud see it 
    def movingInLoadMenu(self):
        self.allUser()
        self.allUser()
        pressed_keys = pygame.key.get_pressed()
        
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==self.maxScroll):
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
        for i in range(len(self.users)):
            if((pressed_keys[K_RETURN])and(self.count >= 5)and(self.menuControl == ((i*50)+200))):
                self.count = 0
                return 3, self.users[i]
                
        self.loadMenuEsc()
        return 4, ''
    
    def allUser(self):
        if(len(os.listdir('users')) == 0):
            pass
        else:
            self.users = os.listdir('users')
            self.currentButtom = self.users[0]
