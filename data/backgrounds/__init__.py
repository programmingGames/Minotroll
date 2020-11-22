import pygame

class Backgound(object):
    def __init__(self, Nrimage, menuEsc, nivel):
        self.Nrimage = Nrimage
        self.esc = menuEsc
        self.nivel = nivel

    # Method to blit the background on the screen
    def settingBackground(self, screen):
        if(self.esc<4):
            self.image = pygame.image.load("resources/image/background/"+str(self.Nrimage)+".png").convert()
        elif(self.esc>=4):
            self.image = pygame.image.load("resources/image/background/nivel_"+str(self.nivel)+"/"+str(self.nivel)+".png").convert()

        screen.blit(self.image, (0,0))

    def movingBackgournd(self):
        pass
    
    def movingComponnets(self):
        pass
    pass 