import pygame 
from pygame.locals import *

# class for all the game input by the keyboard
class Textinput:
    def __init__(self):
        pygame.init()
        self.base_font = pygame.font.SysFont(None, 32)
        self.text = ''
        self.input_rect = pygame.Rect(205, 190, 140, 32)
        self.color_active = pygame.Color(128,128,128)
        self.color_passive = pygame.Color(255, 255, 255)
        self.color = self.color_passive
        self.active = False
    
    # Method to receive the input text from the keyboard
    def settingInputText(self, screen, event):
        # Verifica se o mause esta dentro da caixa d texto para permitir a escrita
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if (self.input_rect.collidepoint(event.pos)):
                self.active = True
            else:
                self.active = False

        # Pega todos os eventos de escrita do teclado
        if (event.type == pygame.KEYDOWN):
            pygame.time.delay(100)
            
            # So escreve na caixa do teclado se a active estiver ativo
            if(self.active == True):
                if (event.key == pygame.K_BACKSPACE):
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        text_surface = self.base_font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(300, text_surface.get_width() + 10)
        return self.text