import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back
from data.textInput import Textinput as textInput

class CreateUserMenu:
    def __init__(self, screen, nrImage, painelState, nivel):
        pygame.init()
        self.screen = screen
        self.nivel = nivel
        self.painelState = painelState
        self.background = Back(nrImage, painelState, nivel)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = "Enter a user name"
        self.buttonBack = pygame.image.load("resources/image/menu/createUser/back.png").convert_alpha()
        self.buttonBack1 = pygame.image.load("resources/image/menu/createUser/back1.png").convert_alpha()
        self.buttoncreate = pygame.image.load("resources/image/menu/createUser/createuser.png").convert_alpha()
        self.buttoncreate1 = pygame.image.load("resources/image/menu/createUser/createuser1.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 32)
        self.text = textInput()
        self.menuControl = 250
        self.count = 0

    # Method to render all the components in the screen
    def settingUserName(self, event):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, (267, 150))
        self.text.settingInputText(self.screen, event)

        # Controling menu buttons efects
        if (self.menuControl == 250):
            self.screen.blit(self.buttoncreate1, (255, 250))
            self.screen.blit(self.buttonBack, (260, 300))
        else:
            self.screen.blit(self.buttoncreate, (260, 250))
            self.screen.blit(self.buttonBack1, (255, 300))

    # Method to move in this menu and return the choose
    def drawUserMenu(self, event):
        pressed_keys = pygame.key.get_pressed()
        self.settingUserName(event)
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
        if((pressed_keys[K_x])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            return 3
        elif((pressed_keys[K_x])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            return 1
        
        
        return 2