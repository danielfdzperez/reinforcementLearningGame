from point import *
import pygame
from world import *
from common import *
import character

from DDQNs import *
import tensorflow as tf
import numpy as np

class PlayerAI(character.Character):
    '''
        Class used for the characters of the game
    '''

    movements = {0:UP, 1:DOWN, 2:RIGHT, 3:LEFT}
    def __init__(self, position, world,sprite, with_animation=True):
        '''
            Constructor
            x and y -> Position
            world -> Controller
            sprite -> Sprite sheet name
        '''
        super().__init__(position,world,sprite, with_animation)

        tf.reset_default_graph()
        tf.set_random_seed(42)
        np.random.seed(42)

        self.network = DDQNs('online', 15,15,512,100,4)
        self.sess = tf.Session()
        saver = tf.train.Saver()
        saver.restore(self.sess,'../train/saver/posible/93/sampling7BB.ckpt')

        
    def update(self):
        '''
            Update the character position and animation
        '''
        #pos_update = {UP:Point(0,1) ,DOWN:Point(0,-1) ,RIGHT:Point(1,0) ,DOWN:Point(-1,0)}
        #new_position = self.position + pos_update[self.direction]
        #calculate the new position
        if self.moving:
            return

        state = self.world.generateState()
        q_values = self.network.evalActionSess([state],self.sess)
        action = np.argmax(q_values)
        #self.futureDirection()

        #self.world.playerDead()
        self.changeDirection(self.movements[action])
        new_position = self.position + self.direction
        #If the character can move to the new position update the position and animation
        if self.world.canMove(new_position):
            self.move(new_position)
            self.world.testCoin()

            #self.world.testCoin()

        #self.animation_position = self.position

    #def updateAnimation(self):
    #    '''
    #        Update the animation
    #    '''
    #    self.animation = (self.animation + 0.25)%Character.ANIMATIONS
    #    a = 2/Character.SIZE
    #    self.animation_position += self.direction * Point(a, a)
    #    
    #    if (self.direction is UP and self.animation_position.y <= self.position.y) or (self.direction is DOWN and self.animation_position.y >= self.position.y) or (self.direction is RIGHT and self.animation_position.x >= self.position.x) or (self.direction is LEFT and self.animation_position.x <= self.position.x):
    #           self.moving = False
    #           self.animation_position = self.position
    #           #self.world.testCoin()
               
    def futureDirection(self,direction):
        return
        self.future_direction = direction
