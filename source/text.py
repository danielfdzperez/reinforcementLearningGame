import pygame
import common as cm
from point import *

class Text:
    def __init__(self, text, color, font):
        self.text = font.render(text, True, color)

    def dimensions(self):
        return self.text.get_width(), self.text.get_height()
    
    def display(self, ctx , x, y):
        ctx.blit(self.text, (x, y))

    def displayMiddle(self,ctx):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.display(ctx, (screen_width-self.text.get_width()) // 2, (screen_height - self.text.get_height()) // 2)
