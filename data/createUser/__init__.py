import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back
from data.textInput import Textinput as textInput

class CreateUser:
    def __init__(self, screen, nrImage, menuEsc, nivel):
        self.screen = screen
        self.menuEsc = menuEsc
        self.nivel = nivel
        self.background = Back(nrImage, menuEsc, nivel)
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = pygame.image.load("resources/image/menu/createUser/create.png").convert_alpha()
        self.buttonBack = pygame.image.load("resources/image/menu/createUser/back.png").convert_alpha()
        self.buttonBack1 = pygame.image.load("resources/image/menu/createUser/back1.png").convert_alpha()
        self.buttoncreate = pygame.image.load("resources/image/menu/createUser/createuser.png").convert_alpha()
        self.buttoncreate1 = pygame.image.load("resources/image/menu/createUser/createuser1.png").convert_alpha()
        self.text = textInput()

    # Method to render all the components in the screen
    def settingUserName(self, event, pos_y):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (210, 10))
        self.screen.blit(self.createText, (267, 150))
        self.text.settingInputText(self.screen, event)

        # Controling menu buttons efects
        if (pos_y == 250):
            self.screen.blit(self.buttoncreate1, (255, 250))
            self.screen.blit(self.buttonBack, (260, 300))
        else:
            self.screen.blit(self.buttoncreate, (260, 250))
            self.screen.blit(self.buttonBack1, (255, 300))

    # Method to move in this menu and return the choose
    def settingUserMenu(self, event, pressed_keys, esc, menuControl):
        self.esc = esc
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(menuControl == 300):
                menuControl = 250
            else:
                menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(menuControl == 250):
                menuControl = 250
            else:
                menuControl -= 50

        if((pressed_keys[K_KP_ENTER])and(menuControl==250)):
            pygame.time.wait(100)
            self.esc = 3
        elif((pressed_keys[K_KP_ENTER])and(menuControl==300)):
            pygame.time.wait(100)
            self.esc = 1
            
        self.settingUserName(event, menuControl)
        return menuControl, self.esc
        
