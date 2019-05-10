import numpy as np
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
        self.tiles_value = [ [ None for i in range(self.width) ] for j in range(self.height)]
        self.coins_matrix = np.empty((self.width,self.height),dtype=object)
        self.coins = []
        self.special_coins = []
        self.player_spawn = None
        self.enemy_spawn = []
        self.builMap(tile_map[0])
        self.buildNeighborhood()
        self.total_coins = len(self.coins) + len(self.special_coins)
        self.max_coins = len(self.coins) + len(self.special_coins)

    def current_coins(self):
        return self.max_coins - self.total_coins

    def builMap(self, tile_map):
        '''
            Create the map using tiles

            tile_map -> Map without tiles
        '''
        for y in range(self.height):
            for x in range(self.width):
                tile  = tile_map[y][x]
                self.tiles[y][x] = self.tile_types[tile](x,y,self.world.with_animation)
                self.tiles_value[y][x] = self.tiles[y][x].type
                if tile is P:
                    coin = targets_types[tile](x,y,self.world.with_animation)
                    self.coins_matrix[y,x] = coin
                    self.coins.append(coin)
                if tile is S:
                    special = targets_types[tile](x,y,self.world.with_animation)
                    self.coins_matrix[y,x] = special
                    self.special_coins.append(special)
                if tile is R:
                    self.enemy_spawn.append(Point(x,y))
                if tile is O:
                    self.player_spawn = Point(x,y)
        self.tiles_value = np.array(self.tiles_value)

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

    def collectCoin(self,position):
        element = self.coins_matrix[position.y,position.x]
        if element is None:
            return

        if element in self.coins:
            i = self.coins.index(element)
            self.coins.pop(i)
            self.world.collectCoin()
            self.total_coins -= 1
        if element in self.special_coins:
            i = self.special_coins.index(element)
            self.special_coins.pop(i)
            self.world.collectSpecial()
            self.total_coins -= 1
        self.coins_matrix[position.y,position.x] = None

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

    def getCurrentState(self):
        state = self.tiles_value.copy()
        for coin in self.coins:
            state[coin.position.y][coin.position.x] = C
        for special in self.special_coins:
            state[special.position.y][special.position.x] = S

        return state
