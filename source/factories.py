from tile import *
from target import *
#Tiles dictionary factories
#tile_types = { W:Tile.wall, P:Tile.path, S:Tile.path, R:Tile.enemyRespawn, O:Tile.path, D:Tile.dockPath}
targets_types    = {P:Target.coin, S:Target.special}


#Factory functions
def wall(x,y, image_x, image_y):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_SHEET)
    image = sheet.get_image(image_x,image_y,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.WALL,image)

def greenWall(x,y):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    return wall(x,y,128,96)

def water(x,y):
    '''
        Create a wood path
        x and y -> Coordinates
    '''
    return wall(x,y,96,672)

def enemyRespawn(x,y,image_x, image_y):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_SHEET)
    image = sheet.get_image(image_x,image_y,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.WALL,image)

def archEnemyRespawn(x,y):
    return enemyRespawn(x,y,Tile.SIZE*5,Tile.SIZE*1)


def doorEnemyRespawn(x,y):
    return enemyRespawn(x,y,Tile.SIZE*18,Tile.SIZE*9)

def path(x,y,image_x, image_y ):
    '''
        Create a path
        x and y -> Coordinates
    '''
    sheet = SpriteSheet(TILE_SHEET)
    image = sheet.get_image(image_x,image_y,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,Tile.PATH,image,walkable=True, invertible = True)

def grassPath(x,y):
    return path(x,y,32,64)


def dockPath(x,y):
    return path(x,y,80,544)

