from common import *
from point import *
from spriteSheet import *
import pygame
class Tile:
    '''
        Class represents a tile
    '''

    #Constants
    SIZE = 32

    def __init__(self, x, y, type, image=None, walkable=False, invertible = False):
        '''
            Constructor
            x and y -> Position of the tile
            value -> Value used by the AI
            image -> Image to draw the tile
            walkable -> Boolean to specify id the tile is walkable
        '''
        self.position = Point(x,y)
        self.walkable = walkable
        self.image = image
        self.type = type
        self.invertible = invertible
        self.neighbours = []

    
    def draw(self, ctx,x, y):
        '''
            draw the tile

            ctx -> Is the context where the tile is going to draw
            x and y are displacements.
        '''
        ctx.blit(self.image, (x,y))

    def swapWalkable(self):
        if self.invertible:
            self.walkable = not self.walkable

    
    
