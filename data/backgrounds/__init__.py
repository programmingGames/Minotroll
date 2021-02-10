import pygame
# Class to control all the game backgournds
class Backgound(object):
    def __init__(self,screen):
        self.screen = screen

    # Method to blit the menus background on the screen
    def settingBackgroundMenu(self,nrImage):
        image = pygame.image.load("resources/image/background/"+str(nrImage)+".png").convert()
        self.screen.blit(image, (0,0))

    # Method to blit the game envirement backgournd on the screen
    def movingBackgourndGamePlay(self, nivel):
        image = None
        if((nivel == 0)or(nivel == 3)):
            image = pygame.image.load("resources/image/background/nivel_1/1.png").convert()
        elif(nivel == 1):
            image = pygame.image.load("resources/image/background/nivel_3/1.png").convert()
        elif(nivel == 2):
            image = pygame.image.load("resources/image/background/nivel_2/1.png").convert()

        self.screen.blit(image, (0,0))
    