
from tile import *
from target import *
from common import *
from factories import *
from point import *

class Map:
    '''
        Class is the responsible to manage the map
    '''

    def __init__(self, tile_map,world):
        '''
            Constructor
            tile_map -> Map without tiles
        '''
        self.world = world
        self.tile_types = tile_map[1]
        self.width = len(tile_map[0][0])
        self.height = len(tile_map[0])
        self.tiles = [ [ None for i in range(self.width) ] for j in range(self.height)]
        self.coins = []
        self.special_coins = []
        self.player_spawn = None
        self.enemy_spawn = []
        self.builMap(tile_map[0])
        self.buildNeighborhood()
        self.total_coins = len(self.coins) + len(self.special_coins)

    def builMap(self, tile_map):
        '''
            Create the map using tiles

            tile_map -> Map without tiles
        '''
        for y in range(self.height):
            for x in range(self.width):
                tile  = tile_map[y][x]
                self.tiles[y][x] = self.tile_types[tile](x,y)
                if tile is P:
                    self.coins.append(targets_types[tile](x,y))
                if tile is S:
                    self.special_coins.append(targets_types[tile](x,y))
                if tile is R:
                    self.enemy_spawn.append(Point(x,y))
                if tile is O:
                    self.player_spawn = Point(x,y)

    def buildNeighborhood(self):
        for y in range(self.height):
            for x in range(self.width):
                tile = self.tiles[y][x]
                if tile.walkable:
                    tile.neighbours = self.getNeighbours(tile.position)



    def draw(self,ctx, x_start, y_start):
        '''
            Draw all the map
            ctx -> Pygame screen to draw
            x_start -> Displacement in x
            y_start -> Displacement in y
        '''
        for y in range(self.height):
            for x in range(self.width):
                self.tiles[y][x].draw(ctx, (x+x_start)*Tile.SIZE,(y+y_start)*Tile.SIZE)
        for coin in self.coins:
            coin.draw(ctx)
        for special in self.special_coins:
            special.draw(ctx)

    def updateAnimations(self):
        for coin in self.coins:
            coin.update()
        for special in self.special_coins:
            special.update()

    def endMap(self):
        if self.total_coins < 1:
            self.world.nextLevel()

    def distanceCoins(self, position):
        self.coins.sort(key=lambda coin:  distance(coin.position, position, self))
        self.special_coins.sort(key=lambda coin:  distance(coin.position, position, self))

    def collectCoin(self,position):
        if self.coins and self.coins[0].position == position:
            self.coins.pop(0)
            self.world.collectCoin()
            self.total_coins -= 1
        if self.special_coins and self.special_coins[0].position == position:
            self.special_coins.pop(0)
            self.world.collectSpecial()
            self.total_coins -= 1

    def isWalkable(self, position):
        '''
            Check if a tile is walkable
            position -> Point of the tile
        '''
        return self.tiles[position.y][position.x].walkable

    def getNeighboursPosition(self,pos,dynamic = False):

        if dynamic:
            return self.getNeighbours(pos)

        return self.tiles[pos.y][pos.x].neighbours

    def getNeighbours(self, pos):
        '''
            Return the positions of the walkable neighbours
            pos -> Point that is the origin
        '''
        neighbours = []

        # West
        w = Point(pos.x-1,pos.y)
        if w.x > -1 and self.isWalkable(w):
            neighbours.append(w) 
	

	# East
        e = Point(pos.x+1,pos.y)
        if e.x < self.width and self.isWalkable(e):
            neighbours.append(e) 
	

	# South
        s = Point(pos.x,pos.y+1)
        if s.y < self.height and self.isWalkable(s):
            neighbours.append(s) 
	

	# North
        n = Point(pos.x,pos.y-1)
        if n.y > -1 and self.isWalkable(n) :
            neighbours.append(n)
        
        return neighbours

    def swapWalkable(self, position):
        self.tiles[position.y][position.x].swapWalkable()

        



        

