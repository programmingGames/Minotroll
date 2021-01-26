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
        if(key[K_RETURN]and(self.count>=3)):
            self.count = 0
            text = self.text
            self.text = ''
            return text
        elif(key[K_BACKSPACE]and(self.count>=3)):
            self.count = 0
            self.text = self.text[:-1]
        elif((self.count>=3)and(len(self.text)<=self.limit)):
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
        text = ''
        keysDict = {key[K_q]:'q', key[K_w]: 'w',key[K_e]: 'e',key[K_r]:'r',key[K_t]:'t',key[K_y]:'y',
        key[K_u]: 'u',key[K_i]:'i',key[K_o]:'o',key[K_p]:'p',key[K_a]:'a',key[K_s]:'s',key[K_d]:'d',
        key[K_f]:'f',key[K_g]:'g',key[K_j]:'j',key[K_k]:'k',key[K_l]:'l',key[K_z]:'z',key[K_x]: 'x',
        key[K_c]:'c',key[K_v]:'v',key[K_b]:'b',key[K_n]:'n',key[K_m]:'m'}

        text = [value for keys, value in keysDict.items() if keys]
        if len(text):
            return text[0]
        else:
            return ''