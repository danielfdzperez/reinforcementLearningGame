from tile import *
from target import *
#Tiles dictionary factories
#tile_types = { W:Tile.wall, P:Tile.path, S:Tile.path, R:Tile.enemyRespawn, O:Tile.path, D:Tile.dockPath}


#Factory functions
def wall(x,y, image_x, image_y, animation=True):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    image = None
    if animation:
        sheet = SpriteSheet(TILE_SHEET)
        image = sheet.get_image(image_x,image_y,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,W,image)

def greenWall(x,y,animation):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    return wall(x,y,128,96,animation)

def water(x,y,animation):
    '''
        Create a wood path
        x and y -> Coordinates
    '''
    return wall(x,y,96,672,animation)

def enemyRespawn(x,y,image_x, image_y,animation):
    '''
        Create a wall
        x and y -> Coordinates
    '''
    image = None
    if animation:
        sheet = SpriteSheet(TILE_SHEET)
        image = sheet.get_image(image_x,image_y,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,W,image)

def archEnemyRespawn(x,y, animation):
    return enemyRespawn(x,y,Tile.SIZE*5,Tile.SIZE*1,animation)


def doorEnemyRespawn(x,y,animation):
    return enemyRespawn(x,y,Tile.SIZE*18,Tile.SIZE*9,animation)

def path(x,y,image_x, image_y,animation):
    '''
        Create a path
        x and y -> Coordinates
    '''
    image = None
    if animation:
        sheet = SpriteSheet(TILE_SHEET)
        image = sheet.get_image(image_x,image_y,Tile.SIZE,Tile.SIZE)
    return Tile(x,y,P,image,walkable=True, invertible = True)

def grassPath(x,y,animation):
    return path(x,y,32,64,animation)


def dockPath(x,y,animation):
    return path(x,y,80,544,animation)

#Targer factory
def coin(x, y,graphics):
    if not graphics:
        return Target(x,y)
    sheet = SpriteSheet(COINS)
    animation = []
    for i in range(8):
        animation.append(sheet.get_image(i*16,0,16,16))
    return Target(x,y,animation,8)
def special(x, y,graphics):
    if not graphics:
        return Target(x,y)
    sheet = SpriteSheet(SPECIAL)
    animation = [sheet.get_image(0,0,32,32)]
    return Target(x,y,animation,1)

targets_types    = {P:coin, S:special}
