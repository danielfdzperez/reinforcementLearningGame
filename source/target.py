from point import *
from common import *
from spriteSheet import *
from tile import *
import pygame
class Target:

    def __init__(self, x, y, animation, n_animations):
        self.position = Point(x,y)
        self.animation = animation
        self.current_animation = 0
        self.n_animations = n_animations

    def draw(self, ctx):
         ctx.blit(self.animation[self.current_animation], 
                 (self.position.x*Tile.SIZE + (Tile.SIZE/4), self.position.y*Tile.SIZE  + (Tile.SIZE/4))) 

    def update(self):
        self.current_animation = (self.current_animation + 1)%self.n_animations


    #Factory functions
    @classmethod
    def coin(cls, x, y):
        sheet = SpriteSheet(COINS)
        animation = []
        for i in range(8):
            animation.append(sheet.get_image(i*16,0,16,16))
        return cls(x,y,animation,8)
    @classmethod
    def special(cls, x, y):
        sheet = SpriteSheet(PIZZA)
        animation = [sheet.get_image(0,0,32,32)]
        return cls(x,y,animation,1)

