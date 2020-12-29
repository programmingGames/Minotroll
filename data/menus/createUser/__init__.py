import pygame
from pygame.locals import *
import os
from data.backgrounds import Backgound as Back
from data.textInput import Textinput as textInput

class CreateUserMenu:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = "Enter a user name"
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = textInput()
        self.menuControl = 250
        self.count = 0
        self.timeEfect = 0
        self.buttoms = ['createuser','back']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(250, 250), (250, 300)]
        self.displayButtoms()
        self.limit = True
        self.exist = False

    # Method to render all the components in the screen
    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 30):
                    img = pygame.image.load("resources/image/menu/createUser/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/createUser/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/createUser/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)

    def settingUserName(self, event):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        self.font.set_bold(True)
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, (265, 150))
        self.user = self.text.settingInputText(self.screen, event)

        # Controling menu buttons efects
        if (self.menuControl == 250):
            self.currentButtom = self.buttoms[0]
        else:
            self.currentButtom = self.buttoms[1]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]
        if(not self.limit or self.exist):
            self.deniedUserCreate()

    # Method to move in this menu and return the choose
    def drawUserMenu(self, event):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl == 300):
                self.menuControl = 250
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl == 250):
                self.menuControl = 250
            else:
                self.menuControl -= 50

        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==250)and(self.count >= 5)and(len(self.user) != 0)):
            self.count = 0
            self.viewUserLimit()
            self.viewUserExist()
            if(self.limit and not self.exist):
                self.createUserDirAndButtom()
                self.createUserEvolutionData()
                return 3, self.user
            else:
                return 2, self.user
        elif((pressed_keys[K_RETURN])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            return 1, self.user
        self.settingUserName(event)
        return 2, self.user

    def createUserDirAndButtom(self):
        os.chdir('users')
        os.mkdir(self.user)
        x = 208
        y = 30
        for i in range(3):
            if(i!=0):
                y = 37
            font = pygame.font.SysFont("arial", 24)
            # font.set_bold(True)
            surf = pygame.Surface((x, y))
            os.chdir('..')
            img = pygame.image.load("resources/image/menu/botao"+str(i)+".png")
            name_surf = font.render(self.user, True, (0, 0, 0), img)
            r = name_surf.get_rect()
            surf.fill((66, 33, 11))
            surf.blit(img, (0, 0))
            surf.blit(name_surf, (int((x/2)-(r.width/2)),int((y/2)-(r.height/2))))
            os.chdir('users/'+self.user)
            pygame.image.save(surf, self.user+""+str(i)+".png")
            os.chdir('..')
        os.chdir('..')

    def createUserEvolutionData(self):
        os.chdir('users/'+self.user)
        file = open('data.txt', 'w')
        #          nivel      Position   Initial Life
        file.write(str(0)+' '+str(500)+' '+str(238))
        file.close()
        os.chdir('../..')

    def viewUserLimit(self):
        if(len(os.listdir('users')) > 3):
            self.limit = False
        else:
            self.limit = True

    def viewUserExist(self):
        userList = os.listdir('users')
        for user in userList:
            if(self.user == user):
                self.exist = True

    def deniedUserCreate(self):
        font = pygame.font.SysFont("Arial", 14)
        font.set_bold(True)
        if(not self.limit):
            line = font.render("Passed the number of allowed users!", True, (206, 0,0))
            self.screen.blit(line, (225, 350))
        elif(self.exist):
            line = font.render("User already exist!", True, (206, 0,0))
            self.screen.blit(line, (285, 350))
        else:
            line = font.render("Not possible to create a user!", True, (206, 0,0))
            self.screen.blit(line, (225, 350))