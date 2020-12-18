import pygame
from pygame import *
from data.backgrounds import Backgound as Back

class UserMenu(object):
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/user_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.timeOut = 0
        self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Walking_"+str(self.timeOut)+".png")
        self.menuControl = 150
        self.timeEfect = 0
        self.buttoms = ['gamePlay','gameMap', 'gameSkills','gameHistory', 'mainMenu']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(100, 150), (100, 200), (100, 250), (100, 300), (100, 350)]
        self.displayButtoms()
        self.count = 0
        self.user = ''
        

    # Method to choose option in main menu
    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)

    def drawUserLevel(self):
        pass
    def mainMenuEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (52, 50))
        self.screen.blit(self.title, (270, 60))

        if (self.menuControl==150):
            self.currentButtom = self.buttoms[0]
        elif (self.menuControl==200):
            self.currentButtom = self.buttoms[1]
        elif (self.menuControl==250):
            self.currentButtom = self.buttoms[2]
        elif (self.menuControl==300):
            self.currentButtom = self.buttoms[3]
        elif(self.menuControl == 350):
            self.currentButtom = self.buttoms[4]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

    # Method to move in the main menu
    def movingInUserMenu(self, user):
        self.user = user
        nivel, skills, lastPassPoint = self.loadUserData(user)
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==350):
                self.menuControl = 150
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl==150):
                self.menuControl = 150
            else:
                self.menuControl -= 50
        choice = self.userChoise(pressed_keys)
        
        self.mainMenuEsc()  
        self.drawUserInfor(user)
        self.golemAnimation()
        return choice, int(nivel), int(skills), int(lastPassPoint)

    def userChoise(self, pressed_keys):
        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==150)and(self.count >= 5)):
            self.count = 0
            return 7
        elif ((pressed_keys[K_RETURN])and(self.menuControl==200)and(self.count >= 5)):
            self.count = 0
            return 3
        elif ((pressed_keys[K_RETURN])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            return 9
        elif ((pressed_keys[K_RETURN])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            return 6
        elif ((pressed_keys[K_RETURN])and(self.menuControl==350)and(self.count >= 5)):
            self.count = 0
            return 1
        return 3

    def golemAnimation(self):
        if(self.timeOut==230):
            self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Walking_"+str(int(self.timeOut/10))+".png")
            self.timeOut = 0
        else:
            if ((self.timeOut % 10)==0):
                self.img = pygame.image.load("resources/image/menu/initial_menu/animation/0_Goblin_Walking_"+str(int(self.timeOut/10))+".png")
            self.timeOut += 1
        self.screen.blit(self.img, (420, 160))
    
    def loadUserData(self, user):
        file = open('users/'+user+'/data.txt', 'r')
        data = file.read()
        file.close()
        allUserData = data.split(' ')
        nivel = allUserData[0]    # The current level of the player 
        skills = allUserData[1]     # the skilss that the user had
        lastPassPoint = allUserData[2]   # the last point in the game tha the user pass to
        return nivel, skills, lastPassPoint

    def drawUserInfor(self, user):
        playerIcon = pygame.image.load("resources/image/user/Head1.png")
        progressBox = pygame.image.load("resources/image/user/progress.png")
        selo = pygame.image.load("resources/image/user/nivel-sel2.png")
        font = pygame.font.SysFont("Arial", 18)
        font.set_bold(True)
        line = font.render(user, True, (255, 255,255))
        
        self.screen.blit(playerIcon, (160, 100))
        self.screen.blit(progressBox, (465, 105))
        self.screen.blit(selo, (440, 95))
        self.screen.blit(line, (195, 110))