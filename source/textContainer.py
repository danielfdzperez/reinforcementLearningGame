import pygame
import common as cm
from text import *
from point import *
class TextContainer:
    def __init__(self, ctx, size = 72):
        self.texts = {}
        self.font = pygame.font.Font(None, size)
        self.ctx = ctx

    def addText(self, text, color=cm.BLACK):
        if text not in self.texts:
            self.texts[text] = Text(text, color, self.font)

    def __getitem__(self, text):
        return self.texts[text]
