
from tile import *
from target import *
#Tiles dictionary factories
#tile_types = { W:Tile.wall, P:Tile.path, S:Tile.path, R:Tile.enemyRespawn, O:Tile.path, D:Tile.dockPath}
targets_types    = {P:Target.coin, S:Target.special}


#Factory functions
def wall(x,y):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_MAP_SHEET)
    image = sheet.get_image(128,96,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.WALL,image)
def enemyRespawn(x,y):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_MAP_SHEET)
    image = sheet.get_image(Tile.SIZE*5,Tile.SIZE*1,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.WALL,image)
def doorEnemyRespawn(x,y):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_MAP_SHEET)
    image = sheet.get_image(Tile.SIZE*18,Tile.SIZE*9,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.WALL,image)

def path(x,y ):
    '''
        Create a path
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_MAP_SHEET)
    image = sheet.get_image(32,64,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.PATH,image,walkable=True, invertible = True)

def dockPath(x,y):
    '''
        Create a wood path
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_MAP_SHEET)
    image = sheet.get_image(80,544,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.PATH,image,walkable=True, invertible = True)

def water(x,y):
    '''
        Create a wood path
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_MAP_SHEET)
    image = sheet.get_image(96,672,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.WALL,image)

