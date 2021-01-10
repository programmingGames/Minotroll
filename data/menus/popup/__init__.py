import pygame 
from pygame import *

class Popup(object):
    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
        self.font = pygame.font.SysFont("Arial", 24)
        self.size = pygame.font.Font.size(self.font, str(self.text))
        self.surf = pygame.Surface((250, 110))
        self.menuControl = 30
        self.timeEfect = 0
        self.buttoms = ["yes", "no"]
        self.currentButtom = self.buttoms[0]
        self.alllButtoms = []
        self.allPosition = [(30, 60), (150, 60)]
        self.displayButtoms()
        self.count = 0

    def movingInPopUp(self, pressed_keys):
        if(pressed_keys[K_RIGHT]):
            pygame.time.delay(100)
            if(self.menuControl==150):
                self.menuControl = 150
            else:
                self.menuControl += 120
        elif(pressed_keys[K_LEFT]):
            pygame.time.delay(100)
            if(self.menuControl==30):
                self.menuControl = 30
            else:
                self.menuControl -= 120


        self.count += 1
        if((pressed_keys[K_RETURN])and(self.menuControl==30)and(self.count >= 5)):
            self.count = 0
            return True
        elif ((pressed_keys[K_RETURN])and(self.menuControl==150)and(self.count >= 5)):
            self.count = 0
            return False
        

    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 10):
                    img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/exit_menu/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)

    def draw(self, pressed_keys):
        self.surf.blit(pygame.image.load("resources/image/menu/user_menu/delete.png").convert_alpha(), (0, 0))
        line = self.font.render(self.text, True, (0, 0,0))
        self.surf.blit(line, ((250/2-self.size[0]/2)-12, 10))
        [self.surf.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]
        self.screen.blit(self.surf, (700/2-250/2, 480/2-110/2))
        self.font.set_bold(True)
        
        # self.screen.blit(line, (170, 200))

        if(self.menuControl == 30):
            self.currentButtom = self.buttoms[0]
        elif(self.menuControl == 150):
            self.currentButtom = self.buttoms[1]
        choice = self.movingInPopUp(pressed_keys)
        self.displayButtoms()

        return choice
        # self.displayButtoms()
        