import pygame

class Backgound(object):
    def __init__(self, Nrimage):
        self.image = pygame.image.load("resources/image/background/"+str(Nrimage)+".png").convert()

    # Method to blit the background on the screen
    def settingBackground(self, screen):
        screen.blit(self.image, (0,0))

    def movingBackgournd(self):
        pass
    
    def movingComponnets(self):
        pass
    pass 