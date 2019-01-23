import pygame
from tile import *
from map import *
from maps import *
from common import *
from character import *
from point import *
from target import *
from ai import *
from text import *


class World:
    '''
        Class that controll all the parts of the game
    '''

    SPECIAL_TIME = 100
    def __init__(self, maps, ctx):
        '''
            Constructor
            maps -> List of maps
        '''
        self.maps = maps
        self.player = None
        self.current_map = None
        self.level = 0
        self.max_level = len(maps)
        self.running = False

        self.ctx = None
        self.clock = None
        self.fps = 60

        self.update_player = 0
        self.update_coins = 0
        self.enemy = []

        self.tick_special = 0
        self.special = False
        
       # self.initializePygame()
        self.ctx = ctx
        self.clock = pygame.time.Clock()
        self.loadLevel()

    def initializePygame(self):
        '''
            Initialize the pygame requirements
        '''
        pygame.init()
        width = len(self.maps[self.level]) * Tile.SIZE
        self.ctx = pygame.display.set_mode((width,width))
        self.clock = pygame.time.Clock()

    def loadLevel(self):
        '''
            Initialize the game
        '''
        self.selectMap(self.level)
        self.player = Character(self.current_map.player_spawn, self, CHARACTER1_SHEET)
        self.enemy.clear()
        self.enemy.append(AI(self.current_map.enemy_spawn[0],self,CHARACTER2_SHEET))
        self.enemy.append(AI(self.current_map.enemy_spawn[1],self,CHARACTER2_SHEET))

    def nextLevel(self):
        self.level += 1
        if self.level < self.max_level:
            self.loadLevel()
        else:
            self.running = False
            self.endGame("You win")

    def selectMap(self, level):
        '''
            Change the current map

            level -> level number
        '''
        self.current_map = Map(self.maps[level],self)

    def startGame(self):
        '''
            Starts the game
        '''
        self.running = True
        self.gameLoop()


    def gameLoop(self):
        '''
            The main loop.
            Updates the characters and draw all the entities.
        '''
        while self.running:
            #self.clock.tick_busy_loop(self.fps)
            self.events()
            self.update()
            self.draw()
             
            print(self.clock.get_fps())
            self.clock.tick_busy_loop(self.fps)
            #self.clock.tick(self.fps)

        
    def endGame(self, txt):
        stop = True
        font_preferences = [
            "Sans Serif",
            "Papyrus",
            "Comic Sans MS"]
        texts = Text(font_preferences)
        text = texts.create_text(txt, 72, (0,0,0))
        w, h = pygame.display.get_surface().get_size()
        self.ctx.blit(text,( (w - text.get_width()) // 2,(h  - text.get_height()) // 2))
        pygame.display.flip()
        while stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    stop = False
        #pygame.quit()


    def draw(self):
        '''
            Draw the map and characters.
        '''
        self.current_map.draw(self.ctx,0,0)
        self.player.draw(self.ctx,0,0)
        for enemy in self.enemy:
            enemy.draw(self.ctx,0,0)
        pygame.display.flip()

    def update(self):
        '''
            Update the characters
        '''
        if True:#self.update_player > 16:
            self.player.update()
            self.update_player = 0
            #self.current_map.distanceCoins(self.player.position)
            #self.current_map.collectCoin(self.player.position)
            for enemy in self.enemy:
                enemy.update()

        self.update_player +=1
        if self.update_coins > 8:
            self.current_map.updateAnimations()
            self.update_coins = 0
        self.update_coins +=1
        self.updateState()
        self.playerDead()
        self.current_map.endMap()

    def testCoin(self):
        self.current_map.distanceCoins(self.player.position)
        self.current_map.collectCoin(self.player.position)
        
    def updateState(self):
        if self.special:
            self.tick_special += 1
            if self.tick_special > World.SPECIAL_TIME:
                self.special = False
                self.tick_special = 0
                self.changeStateAi(AI.HUNT)
        

    def changeStateAi(self, state):
        for enemy in self.enemy:
            enemy.state = state


    def events(self):
        '''
            Look for events
        '''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in PLAYER_EVENTS:
                #self.player.changeDirection(PLAYER_EVENTS[event.key])
                self.player.futureDirection(PLAYER_EVENTS[event.key])
            if event.type == pygame.QUIT:
                self.running = False


    def canMove(self, position):
       '''
            Test if the position is walkable

            position -> The position to test
       '''
       return self.current_map.isWalkable(position)

    def collectCoin(self):

        #print('punto')
        1 +1 

    def collectSpecial(self):
        self.special = True
        self.tick_special = 0
        self.changeStateAi(AI.FLEE)

    def playerDead(self):
        for e in self.enemy:
            if e.position == self.player.position:
                self.running = False
                for i in range(10):
                    self.draw()
                    self.clock.tick_busy_loop(self.fps)
                self.endGame('Game over')