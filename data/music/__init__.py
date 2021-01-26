import pygame

class Sounds(object):
    def __init__(self):
        self.start = pygame.mixer.Sound("resources/sounds/menu/login.oga")
        self.menuMove = pygame.mixer.Sound("resources/sounds/menu/updownmove.ogg")
        self.select = pygame.mixer.Sound("resources/sounds/menu/selected.ogg")
        self.switch = pygame.mixer.Sound("resources/sounds/menu/switch.oga")
        self.ambiente = pygame.mixer.Sound("resources/sounds/ambiente/anbiente.ogg")
    def startSounds(self):
        self.start.set_volume(0.0081)
        self.start.play(0)
    def upDownMenu(self):
        self.start.stop()
        self.menuMove.set_volume(0.1991)
        self.menuMove.play()
    def selected(self):
        self.select.set_volume(0.1991)
        self.select.play()
    def skillschange(self):
        self.switch.set_volume(0.1791)
        self.switch.play()
    def envirementOne(self):
        self.ambiente.set_volume(0.1591)
        self.ambiente.play(-1)