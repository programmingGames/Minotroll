import pygame 
from data import intro
from data.backgrounds import Backgound as Back
from data import Hysto 
class Intro(object):
    def __init__(self, screen, nrImage):
        self.screen = screen
        self.time = 0
        self.background = Back(nrImage)
        self.painel = pygame.image.load("resources/image/menu/initial_menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 19,1)
        self.font2 = pygame.font.SysFont("Arial",17,1)
        self.font3 = pygame.font.SysFont("Arial",17,1)
        self.font4 = pygame.font.SysFont("Arial",16,5)
        
        history = Hysto()
        self.primeirolinha = history.part1()
        self.segundolinha = history.part2()
        self.terceiraLinha = history.part3()
        self.quartaLinha =  history.part4()
        self.quintaLinha = history.part5()
        self.sextaLinha = history.part6()
        self.setimaLinha = history.part7()

        #SegundoParagrafo

        self.segundo_Paragrafo_Primeira_Linha = history.part8()
        self.segundo_Paragrafo_Segunda_Linha = history.part9()
        self.segundo_Paragrafo_Terceira_Linha = history.part10()
        self.segundo_Paragrafo_Quarta_Linha = history.part11()
        self.segundo_Paragrafo_Quinta_Linha = history.part12()
        self.segundo_Paragrafo_Sexta_Linha = history.part13()
        self.segundo_Paragrafo_Setima_Linha = history.part14()
        self.segundo_Paragrafo_Oitava_Linha = history.part15()
        self.segundo_Paragrafo_Nona_Linha = history.part16() 
        self.segundo_Paragrafo_Decima_Linha = history.part17()
        self.segundo_Paragrafo_11_Linha = history.part18()
        self.segundo_Paragrafo_12_Linha = history.part19()


        #TerceiroParagrafo

        self.TerParagrafo_1L=history.Ter1()
        self.TerParagrafo_2L=history.Ter2()
        self.TerParagrafo_3L=history.Ter3()
        self.TerParagrafo_4L=history.Ter4()
        self.TerParagrafo_5L=history.Ter5()
        self.TerParagrafo_6L=history.Ter6()
        self.TerParagrafo_7L=history.Ter7()
        self.TerParagrafo_8L=history.Ter8()
        self.TerParagrafo_9L=history.Ter9()
        self.TerParagrafo_10L=history.Ter10()
        self.TerParagrafo_11L=history.Ter11()
        self.TerParagrafo_12L=history.Ter12()

        #QuartoParagrafo
        self.QuaParagrafo_1L=history.Quar1()
        self.QuaParagrafo_2L=history.Quar2()
        self.QuaParagrafo_3L=history.Quar3()
        self.QuaParagrafo_4L=history.Quar4()
        self.QuaParagrafo_5L=history.Quar5()
        self.QuaParagrafo_6L=history.Quar6()
        self.QuaParagrafo_7L=history.Quar7()
        self.QuaParagrafo_8L=history.Quar8()
        self.QuaParagrafo_9L=history.Quar9()
        self.QuaParagrafo_10L=history.Quar10()
        self.QuaParagrafo_11L=history.Quar11()
        self.QuaParagrafo_12L=history.Quar12()
        self.QuaParagrafo_13L=history.Quar13()

    '''def wait():
        time_to_wait= 10000
        pygame.time.wait(time_to_wait)
    def shape_wait():
        time_to_wait= 10000
        timeout = pygame.USEREVENT+1
        pygame.time.set_timer(timeout,time_to_wait)'''

    def introDisplay(self):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (210, 10))


        ##  write code 
        #Primeiro paragrafo
        
        
        text_surf1 = self.font.render(self.primeirolinha, True, (97, 104, 130))
        text_surf2 = self.font.render(self.segundolinha, True, (97, 104, 130))
        text_surf3 = self.font.render(self.terceiraLinha, True, (97, 104, 130))
        text_surf4 = self.font.render(self.quartaLinha, True, (97, 104, 130))
        text_surf5 = self.font.render(self.quintaLinha, True, (97, 104, 130))
        text_surf6 = self.font.render(self.sextaLinha, True, (97, 104, 130))
        text_surf7 = self.font.render(self.setimaLinha, True, (97, 104, 130))

        self.screen.blit(text_surf1, (165, 135))
        self.screen.blit(text_surf2, (120, 170))
        self.screen.blit(text_surf3, (150, 205))
        self.screen.blit(text_surf4, (140, 240))
        self.screen.blit(text_surf5, (125, 275))
        self.screen.blit(text_surf6, (170, 310))
        self.screen.blit(text_surf7, (175, 345))
        
        #SegundoParagrafo

        '''text_surf8 = self.font2.render(self.segundo_Paragrafo_Primeira_Linha, True, (97, 104, 130))
        text_surf9 = self.font2.render(self.segundo_Paragrafo_Segunda_Linha, True, (97, 104, 130))
        text_surf10 = self.font2.render(self.segundo_Paragrafo_Terceira_Linha, True, (97, 104, 130))
        text_surf11 = self.font2.render(self.segundo_Paragrafo_Quarta_Linha, True, (97, 104, 130))
        text_surf12 = self.font2.render(self.segundo_Paragrafo_Quinta_Linha, True, (97, 104, 130))
        text_surf13 = self.font2.render(self.segundo_Paragrafo_Sexta_Linha, True, (97, 104, 130))
        text_surf14 = self.font2.render(self.segundo_Paragrafo_Setima_Linha, True, (97, 104, 130))
        text_surf15 = self.font2.render(self.segundo_Paragrafo_Oitava_Linha, True, (97, 104, 130))
        text_surf16 = self.font2.render(self.segundo_Paragrafo_Nona_Linha, True, (97, 104, 130))
        text_surf17 = self.font2.render(self.segundo_Paragrafo_Decima_Linha, True, (97, 104, 130))
        text_surf18 = self.font2.render(self.segundo_Paragrafo_11_Linha, True, (97, 104, 130))
        text_surf19 = self.font2.render(self.segundo_Paragrafo_12_Linha, True, (97, 104, 130))
        self.screen.blit(text_surf8, (148, 123))
        self.screen.blit(text_surf9, (148, 147))
        self.screen.blit(text_surf10, (185, 173))
        self.screen.blit(text_surf11, (158, 197))
        self.screen.blit(text_surf12, (153, 223))
        self.screen.blit(text_surf13, (173, 247))
        self.screen.blit(text_surf14, (180, 273))
        self.screen.blit(text_surf15, (170, 297))
        self.screen.blit(text_surf16, (150, 323))
        self.screen.blit(text_surf17, (185, 347))
        self.screen.blit(text_surf18, (175, 373))
        self.screen.blit(text_surf19, (290, 397))'''

        #TerceiroParagrafo

        '''Terparafo1 = self.font3.render(self.TerParagrafo_1L, True, (97, 104, 130))
        Terparafo2 = self.font3.render(self.TerParagrafo_2L, True, (97, 104, 130))
        Terparafo3 = self.font3.render(self.TerParagrafo_3L, True, (97, 104, 130))
        Terparafo4 = self.font3.render(self.TerParagrafo_4L, True, (97, 104, 130))
        Terparafo5 = self.font3.render(self.TerParagrafo_5L, True, (97, 104, 130))
        Terparafo6 = self.font3.render(self.TerParagrafo_6L, True, (97, 104, 130))
        Terparafo7 = self.font3.render(self.TerParagrafo_7L, True, (97, 104, 130))
        Terparafo8 = self.font3.render(self.TerParagrafo_8L, True, (97, 104, 130))
        Terparafo9 = self.font3.render(self.TerParagrafo_9L, True, (97, 104, 130))
        Terparafo10 = self.font3.render(self.TerParagrafo_10L, True, (97, 104, 130))
        Terparafo11 = self.font3.render(self.TerParagrafo_11L, True, (97, 104, 130))
        Terparafo12 = self.font3.render(self.TerParagrafo_12L, True, (97, 104, 130))
        self.screen.blit(Terparafo1, (145, 123))
        self.screen.blit(Terparafo2, (160, 147))
        self.screen.blit(Terparafo3, (150, 173))
        self.screen.blit(Terparafo4, (165, 197))
        self.screen.blit(Terparafo5, (135, 223))
        self.screen.blit(Terparafo6, (150, 247))
        self.screen.blit(Terparafo7, (138, 273))
        self.screen.blit(Terparafo8, (155, 297))
        self.screen.blit(Terparafo9, (120, 323))
        self.screen.blit(Terparafo10, (195, 347))
        self.screen.blit(Terparafo11, (160, 373))
        self.screen.blit(Terparafo12, (300, 397))'''

        #QuartoParagrafo
        ''' Quaparagrafo1 = self.font4.render(self.QuaParagrafo_1L, True, (97, 104, 130))
        Quaparagrafo2 = self.font4.render(self.QuaParagrafo_2L, True, (97, 104, 130))
        Quaparagrafo3 = self.font4.render(self.QuaParagrafo_3L, True, (97, 104, 130))
        Quaparagrafo4 = self.font4.render(self.QuaParagrafo_4L, True, (97, 104, 130))
        Quaparagrafo5 = self.font4.render(self.QuaParagrafo_5L, True, (97, 104, 130))
        Quaparagrafo6 = self.font4.render(self.QuaParagrafo_6L, True, (97, 104, 130))
        Quaparagrafo7 = self.font4.render(self.QuaParagrafo_7L, True, (97, 104, 130))
        Quaparagrafo8 = self.font4.render(self.QuaParagrafo_8L, True, (97, 104, 130))
        Quaparagrafo9 = self.font4.render(self.QuaParagrafo_9L, True, (97, 104, 130))
        Quaparagrafo10 = self.font4.render(self.QuaParagrafo_10L, True, (97, 104, 130))
        Quaparagrafo11 = self.font4.render(self.QuaParagrafo_11L, True, (97, 104, 130))
        Quaparagrafo12 = self.font4.render(self.QuaParagrafo_12L, True, (97, 104, 130))
        Quaparagrafo13 = self.font4.render(self.QuaParagrafo_13L, True, (97, 104, 130))
       
        self.screen.blit(Quaparagrafo1, (142, 130))
        self.screen.blit(Quaparagrafo2, (155, 150))
        self.screen.blit(Quaparagrafo3, (138, 170))
        self.screen.blit(Quaparagrafo4, (132, 190))
        self.screen.blit(Quaparagrafo5, (145, 210))
        self.screen.blit(Quaparagrafo6, (145, 230))
        self.screen.blit(Quaparagrafo7, (153, 250))
        self.screen.blit(Quaparagrafo8, (165, 270))
        self.screen.blit(Quaparagrafo9, (145, 290))
        self.screen.blit(Quaparagrafo10, (125, 310))
        self.screen.blit(Quaparagrafo11, (125, 330))
        self.screen.blit(Quaparagrafo12, (155, 350))
        self.screen.blit(Quaparagrafo13, (155, 370))'''
      


        return 4
        # pygame.time.set_timer(self.NEW_BASIC_SOUL, 3000)