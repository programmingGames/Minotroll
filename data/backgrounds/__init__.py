import pygame

class Backgound(object):
    def __init__(self, Nrimage):
        self.Nrimage = Nrimage

    # Method to blit the background on the screen
    def settingBackground(self, screen):
        self.image = pygame.image.load("resources/image/background/"+str(self.Nrimage)+".png").convert()

        screen.blit(self.image, (0,0))

    def movingBackgournd(self):
        pass
    
    def movingComponnets(self):
        pass
    pass 