import pygame
from tile import *
from map import *
from maps import *
from common import *
from character import *
from point import *
from target import *
from ai import *
from textContainer import *
from text import *
from player import *


class World:
    '''
        Class that controll all the parts of the game
    '''

    SPECIAL_TIME = 215

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
        
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        #self.ctx = ctx.copy()
        self.ctx = ctx
        self.original_ctx = ctx
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.update_player = 0
        self.update_coins = 0
        self.enemy = []

        self.tick_special = 0
        self.special = False
        self.countdown = True
        
        self.texts = TextContainer(self.ctx)
       # self.initializePygame()
        
        self.loadText()
        
        self.loadLevel()

    def loadText(self):
        loadingDisplay(self.original_ctx)
        loadingDisplay(self.ctx)
        self.texts.addText(GAME_OVER)
        self.texts.addText(WIN)
        self.texts.addText(str(3))
        self.texts.addText(str(2))
        self.texts.addText(str(1))

    def wait(self):
        count = 3

        self.clock.tick_busy_loop(1)
        while count > 0:
            TICK1.play()
            self.draw()
            self.texts[str(count)].displayMiddle(self.ctx)
            #self.original_ctx.blit(pygame.transform.scale(self.ctx, pygame.display.get_surface().get_size()), (0, 0))
            pygame.display.flip()
            count -= 1
            self.clock.tick_busy_loop(1)
        TICK2.play()
        self.countdown = False            


    def loadLevel(self):
        '''
            Initialize the game
        '''

        loadingDisplay(self.ctx)

        self.selectMap(self.level)
        self.player = Player(self.current_map.player_spawn, self, [CHARACTER1_SHEET])
        self.enemy.clear()
        self.enemy.append(AI(self.current_map.enemy_spawn[0],self,[CHARACTER2_SHEET, CHARACTER4_SHEET]))
        self.enemy.append(AI(self.current_map.enemy_spawn[1],self,[CHARACTER2_SHEET, CHARACTER4_SHEET]))

    def nextLevel(self):
        self.level += 1
        if self.level < self.max_level:
            self.loadLevel()
            self.countdown = True
        else:
            self.running = False
            WON.play()
            self.endGame(WIN)

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

            if self.countdown:
                self.wait()

            #self.clock.tick_busy_loop(self.fps)
            self.draw()
            self.events()
            self.update()
             
            #print(self.clock.get_fps())
            self.clock.tick_busy_loop(self.fps)
            #self.clock.tick(self.fps)

        
    def endGame(self, txt):
        stop = True

        w, h = self.texts[txt].dimensions()
        self.texts[txt].display(self.ctx, (self.screen_width-w) // 2, (self.screen_height - h) // 2)
        #self.original_ctx.blit(pygame.transform.scale(self.ctx, pygame.display.get_surface().get_size()), (0, 0))
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
        #self.original_ctx.blit(self.ctx,(0,0))

        #self.original_ctx.blit(pygame.transform.scale(self.ctx, pygame.display.get_surface().get_size()), (0, 0))
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
                SPECIAL_END_SOUND.play()
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
            if event.type == pygame.VIDEORESIZE:
               self.original_ctx = pygame.display.set_mode(
                   event.dict['size'], pygame.RESIZABLE)


    def canMove(self, position):
       '''
            Test if the position is walkable

            position -> The position to test
       '''
       return self.current_map.isWalkable(position)

    def collectCoin(self):

        #print('punto')
        COIN.play()

    def collectSpecial(self):
        SPECIAL_SOUND.play()
        self.special = True
        self.tick_special = 0
        self.changeStateAi(AI.FLEE)

    def playerDead(self):
        for e in self.enemy:
            if e.position == self.player.position:
                self.running = False
                LOSE.play()
                for i in range(10):
                    self.draw()
                    self.clock.tick_busy_loop(self.fps)
                self.endGame(GAME_OVER)
