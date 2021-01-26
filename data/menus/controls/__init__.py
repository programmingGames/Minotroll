import pygame 
from random import randint
from pygame.locals import * 
from data.backgrounds import Backgound as Back
from data.music import Sounds

class Controls:
    def __init__(self, screen):
        self.screen = screen
        self.sounds = Sounds()
        self.background = Back(screen)
        self.painel = pygame.image.load("resources/image/menu/settings/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 12)
        self.font.set_bold(True)
        self.font1 = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
        self.text = 'Controls'
        self.size = pygame.font.Font.size(self.font1, self.text)
        self.font1.set_bold(True)
        self.timeEfect = 0
        self.buttom = 'Back'
        self.count = 0
        self.controls = ['Direction keys ("up", "down") - Move through menu screens.',
                        '"ENTER" key - selects the triggered item in the menu screens.',
                        'Direction keys ("left", "up", "right") - Move through the game screen.',
                        '"M" key - show and hide game map',
                        '"TAB" key - show and hide skills on the game screen.',
                        'Keys "1", "2", ..., "5" - change the skill in use, if in show state.',
                        '"Q" key - activates the attack state, depending on the skill in use.',
                        '"ESC" key - pauses the game.'
                ]
        



    # Method to blit the start game font on the screen
    def settingControls(self):
        pressed_keys = pygame.key.get_pressed()
        
        self.count += 1
        if((pressed_keys[K_RETURN])and(self.count >= 5)):
            self.count = 0
            self.sounds.selected()
            return 20     
                
        self.controlsEsc() 
        return 21

    def controlsEsc(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel, (105, 90))
        self.screen.blit(self.title, (270, 100))
        line = self.font1.render(self.text, True, (255, 255,255))
        self.screen.blit(line, ((700/2-self.size[0]/2)-4, 350))

        ty = 170
        for paragrf in self.controls:
            size = pygame.font.Font.size(self.font, str(paragrf))
            line = self.font.render(paragrf, True, (0, 0,0))
            self.screen.blit(line, ((700/2-size[0]/2)+6, ty))
            ty += 15

        if (self.timeEfect == 10):
            img = pygame.image.load("resources/image/menu/settings/"+self.buttom+"1.png").convert_alpha()
            self.timeEfect = 0
        else:
            img = pygame.image.load("resources/image/menu/settings/"+self.buttom+"2.png").convert_alpha()
            self.timeEfect += 1
        self.screen.blit(img, (265, 300))