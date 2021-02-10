import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back

class UserMenu(object):
    def __init__(self, screen):
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/user_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.timeOut = 0
        self.font1 = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
        self.text = 'Game Menu'
        self.size = pygame.font.Font.size(self.font1, self.text)
        self.font1.set_bold(True)
        self.img = pygame.image.load("resources/image/menu/user_menu/animation/0_Goblin_Walking_"+str(self.timeOut)+".png")
        self.avalableSkills = None
        self.nivel = None
        self.lastPassPoint_x = 0
        self.lastPassPoint_y = 0
        self.life = 0
        self.greenFire = 0
        self.blueFire = 0
        self.enimysKilled = 0
        self.menuControl = 150
        self.timeEfect = 0
        self.buttoms = ['Play','Skills','History', 'Main Menu','Delete']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = []
        self.displayButtoms()
        self.count = 0
        self.user = ''
        

    # Method to choose option in main menu
    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 155
        y = 150
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 150
            else:
                x = 155
                img = pygame.image.load("resources/image/menu/user_menu/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50

    def mainMenuEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (105, 60))
        self.screen.blit(self.title, (270, 70))

        line = self.font1.render(self.text, True, (255, 255,255))
        self.screen.blit(line, ((700/2-self.size[0]/2)-4, 400))
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
        if self.user != user:
            self.loadUserData(user)
            self.skillsOfThePlayer()
            self.user = user
        choice = 3
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN] and self.count>=5):
            self.count = 0
            if(self.menuControl==350):
                self.menuControl = 150
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP] and self.count>=5):
            self.count = 0
            if(self.menuControl==150):
                self.menuControl = 150
            else:
                self.menuControl -= 50
        choice = self.userChoise(pressed_keys)
        self.mainMenuEsc()  
        self.drawUserInfor()
        self.golemAnimation()
        return choice

    def userChoise(self, pressed_keys):
        if((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==150)and(self.count >= 5)):
            self.count = 0
            # self.sounds.selected()
            return 7
        elif ((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==200)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 150
            # self.sounds.selected()
            return 9
        elif ((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 150
            # self.sounds.selected()
            return 6
        elif ((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 150
            # self.sounds.selected()
            return 1
        elif ((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==350)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 150
            return 17
        self.count += 1
        return 3

    def golemAnimation(self):
        if(self.timeOut==46):
            self.img = pygame.image.load("resources/image/menu/user_menu/animation/0_Goblin_Walking_"+str(int(self.timeOut/2))+".png")
            self.timeOut = 0
        else:
            if ((self.timeOut % 2)==0):
                self.img = pygame.image.load("resources/image/menu/user_menu/animation/0_Goblin_Walking_"+str(int(self.timeOut/2))+".png")
            self.timeOut += 1
        self.screen.blit(self.img, (450, 180))
    
    def loadUserData(self, user):
        file = open('users/'+user+'/data.txt', 'r')
        data = file.read()
        file.close()
        allUserData = data.split(' ')
        self.nivel = int(allUserData[0])    # The current level of the player 
        self.lastPassPoint_x = int(allUserData[1])  # the last point in the game tha the user pass to in x
        self.lastPassPoint_y = int(allUserData[2])   # the last point in the game tha the user pass to in y
        self.life = int(allUserData[3])  # the last quantity of life save by the user
        self.enimysKilled = int(allUserData[4]) ## the total of enimys killed by the user
        self.greenFire = int(allUserData[5]) # the total of green fire availabe
        self.blueFire = int(allUserData[6]) # the total of blue fire availabe

    def drawUserInfor(self):
        playerIcon = pygame.image.load("resources/image/menu/user_menu/faceIcon.png")
        currentNivel = "Level: "+str(int(self.nivel)+1)

        # calcum of the level percentage completed
        currentProgressPerc = 0
        if ((self.nivel == 0)or(self.nivel == 1)):
            currentProgressPerc = int(((self.lastPassPoint_x - 500)*100)/(5460-500))
        elif(self.nivel == 2):
            currentProgressPerc = int(((self.lastPassPoint_x - 500)*100)/(6760-500))
        elif(self.nivel == 3):
            currentProgressPerc = int(((self.lastPassPoint_x - 500)*100)/(4200-500))
        currentProgress = "Level Status: "+str(currentProgressPerc)+'%'

        currentLifePerc = int((self.life*100)/218)
        currentLife = 'Life Status: '+str(currentLifePerc)+'%'

        ## bliting statistic info
        font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
        font.set_bold(True)
        line = font.render(self.user.capitalize(), True, (255, 255,255))
        self.screen.blit(line, (386, 188))
        font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 12)
        font.set_bold(True)
        line = font.render(currentNivel, True, (255, 255,255))
        self.screen.blit(line, (350, 245))
        line = font.render(currentProgress, True, (255, 255,255))
        self.screen.blit(line, (350, 265))
        line = font.render(currentLife, True, (255, 255,255))
        self.screen.blit(line, (350, 285))

        line = font.render('Skills: ', True, (255, 255,255))
        self.screen.blit(line, (350, 305))
        
        ## bliting the skills of the player
        x = 390
        for card in self.avalableSkills:
            self.screen.blit(card, (x, 302))
            x += 16

        line = font.render('Enimy killed: '+str(self.enimysKilled), True, (255, 255,255))
        self.screen.blit(line, (350, 325))
        self.screen.blit(playerIcon, (350, 180))

    def skillsOfThePlayer(self):
        skills = 0
        if (self.nivel == 0):
            skills = 2

        elif(self.nivel == 1):
            skills = 4

        elif(self.nivel >= 2):
            skills = 5
        self.avalableSkills = [pygame.image.load("resources/image/menu/user_menu/skills/"+str(i)+"-True.png")for i in range(skills)]
        