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

    def __init__(self, x, y, value, image=None, walkable=False, invertible = False):
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
        self.value = value
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

    #Factory functions
    @classmethod
    def wall(cls,x,y):
        '''
            Create a wall
            x and y -> Coordinates
        '''
        sheet = SpriteSheet(TILE_MAP_SHEET)
        image = sheet.get_image(128,96,Tile.SIZE,Tile.SIZE)
        return cls(x,y,W,image)
    @classmethod
    def enemyRespawn(cls,x,y):
        '''
            Create a wall
            x and y -> Coordinates
        '''
        sheet = SpriteSheet(TILE_MAP_SHEET)
        image = sheet.get_image(Tile.SIZE*5,Tile.SIZE*1,Tile.SIZE,Tile.SIZE)
        return cls(x,y,W,image)
    @classmethod
    def path(cls,x,y ):
        '''
            Create a path
            x and y -> Coordinates
        '''
        sheet = SpriteSheet(TILE_MAP_SHEET)
        image = sheet.get_image(32,64,Tile.SIZE,Tile.SIZE)
        return cls(x,y,P,image,walkable=True, invertible = True)
    
