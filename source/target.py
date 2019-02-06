from point import *
from common import *
from spriteSheet import *
from tile import *
import pygame
class Target:

    def __init__(self, x, y, animation=None, n_animations=0):
        self.position = Point(x,y)
        self.animation = animation
        self.current_animation = 0
        self.n_animations = n_animations

    def draw(self, ctx):
         ctx.blit(self.animation[self.current_animation], 
                 (self.position.x*Tile.SIZE + (Tile.SIZE/4), self.position.y*Tile.SIZE  + (Tile.SIZE/4))) 

    def update(self):
        self.current_animation = (self.current_animation + 1)%self.n_animations

