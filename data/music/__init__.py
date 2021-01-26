import pygame

class Sounds(object):
    def __init__(self):
        self.start = pygame.mixer.Sound("resources/sounds/menu/login.oga")
        self.menuMove = pygame.mixer.Sound("resources/sounds/menu/updownmove.ogg")
        self.select = pygame.mixer.Sound("resources/sounds/menu/selected.ogg")
    def startSounds(self):
        self.start.set_volume(0.0081)
        self.start.play()
    def upDownMenu(self):
        self.menuMove.set_volume(0.0081)
        self.menuMove.play()
    def selected(self):
        self.select.set_volume(0.0081)
        self.select.play()
