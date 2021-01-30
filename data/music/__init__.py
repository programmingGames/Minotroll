import pygame

class Sounds(object):
    pygame.mixer.init()
    def __init__(self):
        self.start = pygame.mixer.Sound("resources/sounds/menu/login.oga")
        self.menuMove = pygame.mixer.Sound("resources/sounds/menu/updownmove.ogg")
        self.select = pygame.mixer.Sound("resources/sounds/menu/selected.ogg")
        self.switch = pygame.mixer.Sound("resources/sounds/menu/switch.oga")
        self.ambiente = pygame.mixer.Sound("resources/sounds/ambiente/anbiente.ogg")
        self.menuBack = pygame.mixer.Sound("resources/sounds/ambiente/menusongs.ogg")
        self.golemSongs = [pygame.mixer.Sound("resources/sounds/golem/"+str(i)+".ogg") for i in range(8)]

    def startSounds(self):
        self.start.set_volume(0.0081)
        self.start.play(0)

    def upDownMenu(self):
        self.start.stop()
        self.menuBackSongStop()
        self.menuMove.set_volume(0.1991)
        self.menuMove.play()

    def selected(self):
        self.menuBackSongStop()
        self.select.set_volume(0.1991)
        self.select.play()

    def skillschange(self):
        self.menuBackSongStop()
        self.switch.set_volume(0.1791)
        self.switch.play()

    def envirementOne(self):
        self.menuBackSongStop()
        self.ambiente.set_volume(0.1591)
        self.ambiente.play()

    def envirementOneStop(self):
        self.ambiente.stop()

    def menubackSong(self):
        self.menuBack.set_volume(0.0291)
        self.menuBack.play(0)

    def menuBackSongStop(self):
        self.menuBack.stop()
    
    def golemTiredOut(self):
        self.envirementOneStop()
        self.golemSongs[0].set_volume(0.1592)
        self.golemSongs[0].play()
    def golemstartFire(self):
        self.envirementOneStop()
        self.golemSongs[2].set_volume(1.1591)
        self.golemSongs[2].play()
    def golemGoFire(self):
        self.envirementOneStop()
        self.golemSongs[3].set_volume(0.195)
        self.golemSongs[3].play()
    def golemEndFire(self):
        self.envirementOneStop()
        self.golemSongs[1].set_volume(0.1943)
        self.golemSongs[1].play()
    def golemHurt(self):
        self.envirementOneStop()
        self.golemSongs[4].set_volume(0.19883)    
        self.golemSongs[4].play()    
    def golemSliding(self):
        self.envirementOneStop()
        self.golemSongs[6].set_volume(10.1934)
        self.golemSongs[6].play()
    def golemSlach(self):
        self.envirementOneStop()
        self.golemSongs[7].set_volume(0.1953)
        self.golemSongs[7].play()
    def golemKicking(self):
        self.envirementOneStop()
        self.golemSongs[5].set_volume(0.19838)
        self.golemSongs[5].play()
