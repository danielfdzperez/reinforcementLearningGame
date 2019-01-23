
from tile import *
from target import *
#Tiles dictionary factories
tile_types = { W:Tile.wall, P:Tile.path, S:Tile.path, R:Tile.enemyRespawn, O:Tile.path}
targets_types    = {P:Target.coin, S:Target.special}
