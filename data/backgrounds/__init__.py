import pygame

class Backgound(object):
    def __init__(self,screen):
        self.screen = screen

    # Method to blit the background on the screen
    def settingBackgroundMenu(self,nrImage):
        image = pygame.image.load("resources/image/background/"+str(nrImage)+".png").convert()
        self.screen.blit(image, (0,0))

    def movingBackgourndGamePlay(self, nivel):
        if((nivel == 0)or(nivel == 3)):
            image = pygame.image.load("resources/image/background/nivel_1/1.png").convert()
        elif(nivel == 1):
            image = pygame.image.load("resources/image/background/nivel_3/1.png").convert()
        elif(nivel == 2):
            image = pygame.image.load("resources/image/background/nivel_2/1.png").convert()

        self.screen.blit(image, (0,0))
    
    def movingComponnets(self):
        pass
    pass 