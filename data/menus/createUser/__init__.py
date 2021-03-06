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
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 16)
        self.size = pygame.font.Font.size(self.font, self.createText)
        self.text = textInput()
        self.menuControl = 250
        self.count = 0
        self.timeEfect = 0
        self.buttoms = ['Create','Back']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(250, 250), (250, 300)]
        self.displayButtoms()
        self.limit = True
        self.exist = False

    # Method to render all the components in the screen
    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 265
        y = 250
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/createUser/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/createUser/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 260
            else:
                x = 265
                img = pygame.image.load("resources/image/menu/createUser/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50

    def settingUserName(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (150, 70))
        self.screen.blit(self.title, (270, 90))
        self.font.set_bold(True)
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, ((700/2-self.size[0]/2)-7, 150))
        self.user = self.text.settingInputText(self.screen)

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
    def drawUserMenu(self):
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
        if((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==250)and(self.count >= 5)and(len(self.user) != 0)):
            self.count = 0
            self.viewUserLimit()
            self.viewUserExist()
            if(self.limit and not self.exist):
                self.createUserDirAndButtom()
                self.createUserEvolutionData()
                self.menuControl = 250
                return 3, self.user
            else:
                return 2, ""
            
        elif((pressed_keys[K_RETURN]  or pressed_keys[K_KP_ENTER])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 250
            return 1, ''
        self.settingUserName()
        return 2, self.user

    def createUserDirAndButtom(self):
        font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
        os.chdir('users')
        os.mkdir(self.user)
        x = 171
        y = 30
        for i in range(3):
            if(i!=0):
                y = 37
            if(i!=0):
                x = 182
            font.set_bold(True)
            surf = pygame.Surface((x, y))
            os.chdir('..')
            img = pygame.image.load("resources/image/menu/botao"+str(i)+".png")
            name_surf = font.render(self.user, True,(0, 0, 0))
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
        #           nivel  | Position_x| Position_y |Initial Life|enimy Killed|green fire|Blue Fire
        file.write(str(0)+' '+str(500)+' '+str(120)+' '+str(218)+' '+str(0)+' '+str(0)+' '+str(0))
        file.close()
        os.chdir('../..')

    def viewUserLimit(self):
        if(len(os.listdir('users')) > 3):
            self.limit = False
        else:
            self.limit = True

    def viewUserExist(self):
        userList = os.listdir('users')
        verify = False
        for user in userList:
            if(self.user.upper() == user.upper()):
                self.exist = True
                verify = True
        if not verify:
            self.exist = False

    def deniedUserCreate(self):
        font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
        font.set_bold(True)
        if(not self.limit):
            size = pygame.font.Font.size(self.font,"Passed the number of allowed users!")
            line = font.render("Passed the number of allowed users!", True, (206, 0,0))
            self.screen.blit(line, (700/2-size[0]/2+20, 350))
        elif(self.exist):
            size = pygame.font.Font.size(self.font,"User already exist!")
            line = font.render("User already exist!", True, (206, 0,0))
            self.screen.blit(line, (700/2-size[0]/2+15, 350))
        else:
            size = pygame.font.Font.size(self.font,"Not possible to create a user!")
            line = font.render("Not possible to create a user!", True, (206, 0,0))
            self.screen.blit(line, (700/2-size[0]/2+20, 350))