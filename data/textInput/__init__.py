import pygame 
from pygame.locals import *

# class for all the game input by the keyboard
class Textinput:
    def __init__(self):
        pygame.init()
        self.base_font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 20)
        self.text = ''
        self.input_rect = pygame.Rect(206, 190, 140, 32)
        self.color_passive = pygame.Color(128,128,128)
        self.color_active = pygame.Color(255, 255, 255)
        self.color = self.color_passive
        self.active = True
        self.limit = 10
        self.count = 0
    
    # Method to receive the input text from the keyboard
    def settingInputText(self, screen):
        # Pega todos os eventos de escrita do teclado
        key = pygame.key.get_pressed()
        if(key[K_RETURN]and(self.count>=5)):
            self.count = 0
            return self.text
        elif(key[K_BACKSPACE]and(self.count>=5)):
            self.count = 0
            self.text = self.text[:-1]
        elif((self.count>=5)and(len(self.text)<=self.limit)):
            self.count = 0
            self.text += self.keysControl(key)
        self.count += 1

        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        text_surface = self.base_font.render(self.text, True, (255, 255, 255))
        size = pygame.font.Font.size(self.base_font, str(self.text))
        screen.blit(text_surface, (int(700/2-size[0]/2), int(self.input_rect.y+5)))
        self.input_rect.w = max(300, text_surface.get_width() + 10)
        return self.text
    def keysControl(self, key):
        if(key[K_q]):
            return 'q'
        elif(key[K_w]):
            return 'w'
        elif(key[K_e]):
            return 'e'
        elif(key[K_r]):
            return 'r'
        elif(key[K_t]):
            return 't'
        elif(key[K_y]):
            return 'y'
        elif(key[K_u]):
            return 'u'
        elif(key[K_i]):
            return 'i'
        elif(key[K_o]):
            return 'o'
        elif(key[K_p]):
            return 'p'
        elif(key[K_a]):
            return 'a'
        elif(key[K_s]):
            return 's'
        elif(key[K_d]):
            return 'd'
        elif(key[K_f]):
            return 'f'
        elif(key[K_g]):
            return 'g'
        elif(key[K_j]):
            return 'j'
        elif(key[K_k]):
            return 'k'
        elif(key[K_l]):
            return 'l'
        elif(key[K_z]):
            return 'z'
        elif(key[K_x]):
            return 'x'
        elif(key[K_c]):
            return 'c'
        elif(key[K_v]):
            return 'v'
        elif(key[K_b]):
            return 'b'
        elif(key[K_n]):
            return 'n'
        elif(key[K_m]):
            return 'm'
        else:
            return ''