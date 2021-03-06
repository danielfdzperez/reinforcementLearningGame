import pygame
import time
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
from playerAi import *


class World:
    '''
        Class that controll all the parts of the game
    '''

    SPECIAL_TIME = 215
    SPECIAL_STEPS = 10
    
    TIME_PUNISH = 0
    COIN_REWARD = 1
    DEAD_PUNISH = -1
    WIN_REWARD  = 10000

    def __init__(self, maps, ctx, with_animation = True, artificial_player = False):
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
        self.with_animation = with_animation
        self.update_player = 0
        self.update_coins = 0
        self.enemy = []
        self.reward = 0
        self.artificial_player = artificial_player



        self.tick_special = 0
        self.special = False
        self.max_special_ticks = World.SPECIAL_TIME
        if not with_animation or artificial_player:
            self.max_special_ticks = World.SPECIAL_STEPS
            #self.updateStateIf = {True:self.updateStateStep, False:lambda:None}
        
        if with_animation:
            self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

            #self.ctx = ctx.copy()
            self.ctx = ctx
            self.original_ctx = ctx
            self.clock = pygame.time.Clock()
            self.fps = 60

            
            self.countdown = True
            
            self.texts = TextContainer(self.ctx)
            
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
            if self.with_animation:
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

        if self.with_animation:
            loadingDisplay(self.ctx)

        self.selectMap(self.level)
        if self.artificial_player:
            self.player = PlayerAI(self.current_map.player_spawn, self, [CHARACTER1_SHEET], self.with_animation)
        else:
            self.player = Player(self.current_map.player_spawn, self, [CHARACTER1_SHEET], self.with_animation)
        self.enemy.clear()
        for pos in self.current_map.enemy_spawn:
            self.enemy.append(AI(pos,self,[CHARACTER2_SHEET, CHARACTER4_SHEET],self.with_animation))
        #self.enemy.append(AI(self.current_map.enemy_spawn[1],self,[CHARACTER2_SHEET, CHARACTER4_SHEET]))

    def trainNextLevel(self):
        self.running = False
        self.addReward(World.WIN_REWARD)

    def normalNextLevel(self):
        self.level += 1
        if self.with_animation:
            WON.play()
        if self.level < self.max_level:
            self.loadLevel()
            self.countdown = True
        else:
            self.running = False
            self.endGame(WIN)

    def nextLevel(self):
        if self.with_animation:
            self.normalNextLevel()
        else:
            trainNextLevel()


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

        if self.with_animation:
            stop = True

            w, h = self.texts[txt].dimensions()
            self.texts[txt].display(self.ctx, (self.screen_width-w) // 2, (self.screen_height - h) // 2)
            #self.original_ctx.blit(pygame.transform.scale(self.ctx, pygame.display.get_surface().get_size()), (0, 0))
            pygame.display.flip()
            while stop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                        stop = False



    def draw(self):
        '''
            Draw the map and characters.
        '''
        if self.update_coins > 8:
            self.current_map.updateAnimations()
            self.update_coins = 0
        self.update_coins +=1
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
        if self.artificial_player:
            enemies_can_update = True
            for enemy in self.enemy:
                enemies_can_update = enemies_can_update and enemy.canUpdate()
            if enemies_can_update and self.player.canUpdate():
                self.player.update()
                for enemy in self.enemy:
                    enemy.update()
                #print(self.generateState())
                self.updateState()
                self.playerDead()
                self.current_map.endMap()
        else:
            self.player.update()
            #self.current_map.distanceCoins(self.player.position)
            #self.current_map.collectCoin(self.player.position)
            for enemy in self.enemy:
                enemy.update()

            self.updateState()
            self.playerDead()
            self.current_map.endMap()

    def testCoin(self):
        self.current_map.collectCoin(self.player.position)
        
    def updateState(self):
        if self.special:
            self.tick_special += 1
            if self.tick_special > self.max_special_ticks:
                if self.with_animation:
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

        #self.addReward((World.COIN_REWARD/self.current_map.total_coins)+10)
        #self.addReward(World.COIN_REWARD*self.current_map.current_coins())
        self.addReward(World.COIN_REWARD)
        #print('punto')
        if self.with_animation:
            COIN.play()

    def collectSpecial(self):
        #self.addReward((World.COIN_REWARD/self.current_map.total_coins)*2+10)
        #self.addReward(World.COIN_REWARD*self.current_map.current_coins()*20)
        self.addReward(World.COIN_REWARD)
        if self.with_animation:
            SPECIAL_SOUND.play()
        self.special = True
        self.tick_special = 0
        self.changeStateAi(AI.FLEE)

    def playerDead(self):
        for e in self.enemy:
            if e.position == self.player.position:
                self.running = False
                if self.with_animation:
                    LOSE.play()
                    for i in range(10):
                        self.draw()
                        self.clock.tick_busy_loop(self.fps)

                self.addReward(World.DEAD_PUNISH)
                self.endGame(GAME_OVER)

    def step(self,action):
        self.reward = 0
        self.addReward(World.TIME_PUNISH)
        self.player.futureDirection(action)
        self.update()
        return self.generateState(),self.reward

    #def updateStep(self):
    #    '''
    #        Update the characters
    #    '''
    #    self.player.updateStep()
    #    #self.current_map.distanceCoins(self.player.position)
    #    #self.current_map.collectCoin(self.player.position)
    #    #for enemy in self.enemy:
    #    self.enemy[0].update()
    #    self.enemy[1].update()

    #    #self.updateState()
    #    self.updateStateIf[self.special]()
    #    self.playerDeadStep()
    #    self.current_map.endMap()

    #def updateStateStep(self):
    #    self.tick_special += 1
    #    if self.tick_special > self.max_special_ticks:
    #        self.special = False
    #        self.tick_special = 0
    #        self.changeStateAi(AI.HUNT)
    #def playerDeadStep(self):
    #    if self.enemy[0].position == self.player.position or self.enemy[1].position == self.player.position:
    #        self.running = False
    #        self.addReward(World.DEAD_PUNISH)
    #        self.endGame(GAME_OVER)

    def addReward (self,reward):
        self.reward += reward

    def newEpisode(self):
        self.level = (self.level + 1) % self.max_level
        self.loadLevel()
        self.running = True
        return self.generateState()

    def repeatEpisode(self):
        self.loadLevel()
        self.running = True
        return self.generateState()


    def generateState(self):
        state = self.current_map.getCurrentState()
        state[self.player.position.y][self.player.position.x] = O
        #for enemy in self.enemy:
        #    state[enemy.position.y][enemy.position.x] = E
        state[self.enemy[0].position.y][self.enemy[0].position.x] = E
        state[self.enemy[1].position.y][self.enemy[1].position.x] = E
        return state

    def getLocalState(self):
        s = self.generateState()
        row = [0]*s.shape[1]
        s = np.vstack((row,s,row))
        col = np.array([0]*s.shape[0])
        col = col.reshape(s.shape[0],1)
        s = np.hstack((col,s,col))
        y = self.player.position.y+1
        x = self.player.position.x+1
        return s[y-2:y+3,x-2:x+3]


    def getPartialState(self):
        s = self.generateState()

        #Pone filas y columnas extras con 0
        row = [0]*s.shape[1]
        s = np.vstack((row,s,row))
        col = np.array([0]*s.shape[0])
        col = col.reshape(s.shape[0],1)
        s = np.hstack((col,s,col))

        ne = np.zeros((4,4))
        y = self.player.position.y+1
        x = self.player.position.x +1
        ne[0] = [s[y-1,x],s[y-2,x],s[y-1,x-1],s[y-1,x+1]]
        ne[1] = [s[y+1,x],s[y+2,x],s[y+1,x-1],s[y+1,x+1]]
        ne[2] = [s[y,x+1],s[y,x+2],s[y-1,x+1],s[y+1,x+1]]
        ne[3] = [s[y,x-1],s[y,x-2],s[y-1,x-1],s[y+1,x-1]]
        #ne[ne == 0] = 5

        ne = np.trunc(ne/5)

        ne = ne.sum(axis=1)
        #if not ne.all()==0:
        #    ne = np.trunc(ne/ne.max())
        #print(ne)
        #print("##")

        return ne

    def getWallState(self):
        s = self.generateState()

        ne = np.zeros((4))
        y = self.player.position.y
        x = self.player.position.x
        ne[0] = s[y-1,x]
        ne[1] = s[y+1,x]
        ne[2] = s[y,x+1]
        ne[3] = s[y,x-1]
        ne[ne == 0] = 20

        ne = np.trunc(ne/20)

        return ne
