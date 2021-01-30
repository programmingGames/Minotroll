import pygame
from pygame.locals import *
# from sys import exit
from data.backgrounds import Backgound as Back

#  Class for controling all the menu on the game
class Settings(object):
    def __init__(self, screen, soundSate, musicState):
        self.screen = screen
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.timeOut = 0
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
        self.text = 'Settings'
        self.size = pygame.font.Font.size(self.font, self.text)
        self.font.set_bold(True)
        self.menuControl = 150
        self.timeEfect = 0
        self.musicOn = soundSate
        self.soundOn = musicState
        self.musicButton = ''
        self.soundButton = ''
        self.buttoms = []
        self.allButtom = []
        self.allPosition = []
        self.checkingSounds()
        self.currentButtom = self.buttoms[0]
        self.displayButtoms()
        self.count = 0
        

    # Method to choose option in main menu
    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 270
        y = 150
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/settings/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/settings/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 265
            else:
                x = 270
                img = pygame.image.load("resources/image/menu/settings/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50
    def checkingSounds(self):
        # checking music
        if self.musicOn:
            self.musicButton = 'MusicOn'
        else:
            self.musicButton = 'MusicOff'
        # checing sound
        if self.soundOn:
            self.soundButton = 'SoundOn'
        else:
            self.soundButton = 'SoundOff'

        self.buttoms = [self.musicButton,self.soundButton, 'Controls', 'Back']
        self.saveSoundsState()
        
    def settingsEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (150, 70))
        self.screen.blit(self.title, (275, 90))

        line = self.font.render(self.text, True, (255, 255,255))
        self.screen.blit(line, ((700/2-self.size[0]/2)-4, 350))

        if (self.menuControl==150):
            self.currentButtom = self.buttoms[0]
        elif (self.menuControl==200):
            self.currentButtom = self.buttoms[1]
        elif (self.menuControl==250):
            self.currentButtom = self.buttoms[2]
        elif (self.menuControl==300):
            self.currentButtom = self.buttoms[3]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

    # Method to move in the main menu
    def movingInSettingsMenu(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==300):
                self.menuControl = 150
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl==150):
                self.menuControl = 150
            else:
                self.menuControl -= 50

        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==150)and(self.count >= 5)):
            self.count = 0
            self.musicOn = not self.musicOn
        elif ((pressed_keys[K_RETURN])and(self.menuControl==200)and(self.count >= 5)):
            self.count = 0
            self.soundOn = not self.soundOn
        elif ((pressed_keys[K_RETURN])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 150
            return 21, self.soundOn, self.musicOn
        elif ((pressed_keys[K_RETURN])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 150
            return 1, self.soundOn, self.musicOn
        self.checkingSounds()
        self.settingsEsc()  
        return 20, self.soundOn, self.musicOn

    def saveSoundsState(self):
        file = open("data/menus/mainMenu/soundState.txt", 'w')
        #          nivel      Position   Initial Life
        file.write(str(int(self.soundOn))+' '+str(int(self.musicOn)))
        file.close()