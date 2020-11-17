import pygame 
from pygame.locals import *

class Textinput:
    def __init__(self):
        self.base_font = pygame.font.Font(None, 32)
        self.text = ''
        self.input_rect = pygame.Rect(200, 200, 140, 32)
        self.color_active = pygame.Color('lightkyblue')
        self.color_passive = pygame.Color('gray15')
        self.color = self.color_passive
        self.active = False
    
    def settingInputText(self, screen, event):
        # Verifica se o mause esta dentro da caixa d texto para permitir a escrita
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if (self.input_rect.collidepoint(event.pos)):
                self.active = True
            else:
                self.active = False

        # Pega todos os eventos de escrita do teclado
        if (event.type == pygame.KEYDOWN):

            # So escreve na caixa do teclado se a active estiver ativo
            if(self.active == True):
                if (event.key == pygame.K_BACKSPACE):
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        if active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        text_surface = self.base_font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)