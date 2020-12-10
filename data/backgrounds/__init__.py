import pygame

class Backgound(object):
    def __init__(self,screen):
        self.screen = screen

    # Method to blit the background on the screen
    def settingBackgroundMenu(self,nrImage):
        image = pygame.image.load("resources/image/background/"+str(nrImage)+".png").convert()
        self.screen.blit(image, (0,0))

    def movingBackgourndGamePlay(self, nivel):
        image = pygame.image.load("resources/image/background/nivel_"+str(nivel)+"/"+str(nivel)+".png").convert()
        self.screen.blit(image, (0,0))
    
    def movingComponnets(self):
        pass
    pass 