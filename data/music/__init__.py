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
        self.start.set_volume(0.3881)
        self.start.play(0)

    def upDownMenu(self):
        self.start.stop()
        self.menuBackSongStop()
        self.menuMove.set_volume(0.9991)
        self.menuMove.play()

    def selected(self):
        self.menuBackSongStop()
        self.select.set_volume(0.9991)
        self.select.play()

    def skillschange(self):
        self.menuBackSongStop()
        self.switch.set_volume(0.3791)
        self.switch.play()

    def envirementOne(self):
        self.menuBackSongStop()
        self.ambiente.set_volume(0.3591)
        self.ambiente.play()

    def envirementOneStop(self):
        self.ambiente.stop()

    def menubackSong(self):
        self.menuBack.set_volume(0.3291)
        self.menuBack.play(0)

    def menuBackSongStop(self):
        self.menuBack.stop()
    
    def golemTiredOut(self):
        self.envirementOneStop()
        self.golemSongs[0].set_volume(0.3592)
        self.golemSongs[0].play()
    def golemstartFire(self):
        self.envirementOneStop()
        self.golemSongs[2].set_volume(1.9591)
        self.golemSongs[2].play()
    def golemGoFire(self):
        self.envirementOneStop()
        self.golemSongs[3].set_volume(0.395)
        self.golemSongs[3].play()
    def golemEndFire(self):
        self.envirementOneStop()
        self.golemSongs[1].set_volume(0.3943)
        self.golemSongs[1].play()
    def golemHurt(self):
        self.envirementOneStop()
        self.golemSongs[4].set_volume(0.39883)    
        self.golemSongs[4].play()    
    def golemSliding(self):
        self.envirementOneStop()
        self.golemSongs[6].set_volume(10.3934)
        self.golemSongs[6].play()
    def golemSlach(self):
        self.envirementOneStop()
        self.golemSongs[7].set_volume(0.3953)
        self.golemSongs[7].play()
    def golemKicking(self):
        self.envirementOneStop()
        self.golemSongs[5].set_volume(0.39838)
        self.golemSongs[5].play()
