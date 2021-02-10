import pygame
from pygame.locals import *

# class of the congrats menu
class Congrats(object):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 16)
        self.font.set_bold(True)
        self.text = ["You finished all the Level's.","The return of brotherhood strength...","joining forces to recover their home village...","see you soon, until the next seasons."]
        self.buttoms = ['Game Menu', 'Main Menu']
        self.currentButtom = self.buttoms[0]
        self.menuControl = 300
        self.allPosition = []
        self.timeEfect = 0
        self.count = 0 
    
    # Method to make the buttoms to be add screen
    def displayButtoms(self):
        self.allButtom = []
        self.allPosition = []
        x = 265
        y = 300
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/congrats/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/congrats/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
                x = 260
            else:
                x = 265
                img = pygame.image.load("resources/image/menu/congrats/"+buttom+"0.png").convert_alpha()

            self.allButtom.append(img)
            self.allPosition.append((x, y))
            y += 50

    # Method to control the menus choice display
    def nextLevelMenuEsc(self):
        self.back = pygame.image.load("resources/image/menu/congrats/back.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))
        if (self.menuControl==300):
            self.currentButtom = self.buttoms[0]
        elif (self.menuControl==350):
            self.currentButtom = self.buttoms[1]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

        # text
        size = pygame.font.Font.size(self.font, "You finished all the Level's.")
        line = self.font.render("You finished all the Level's.", True, (255, 255,255))
        self.screen.blit(line, ((700/2-size[0]/2), 265))

        ty = 400
        for text in self.text:
            size = pygame.font.Font.size(self.font, text)
            line = self.font.render(text, True, (255, 255,255))
            self.screen.blit(line, ((700/2-size[0]/2), ty))
            ty += 20

    # Method to control the menus move
    def drawingcongratsPainel(self):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl==350):
                self.menuControl = 300
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl==300):
                self.menuControl = 300
            else:
                self.menuControl -= 50
        
        self.nextLevelMenuEsc()
        choice = self.nextLevelChoise(pressed_keys)
        # print(choice)
        return choice, True

    # Method to control the choice
    def nextLevelChoise(self, pressed_keys):
        self.count += 1
        if((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            return 3
        elif ((pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER])and(self.menuControl==350)and(self.count >= 5)):
            self.count = 0
            self.menuControl = 300
            return 1
        return 19