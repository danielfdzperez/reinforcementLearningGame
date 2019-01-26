from point import *
import pygame
from world import *
from common import *
import character
class Player(character.Character):
    '''
        Class used for the characters of the game
    '''

    def __init__(self, position, world,sprite=None):
        '''
            Constructor
            x and y -> Position
            world -> Controller
            sprite -> Sprite sheet name
        '''
        super().__init__(position,world,sprite)
        
    def update(self):
        '''
            Update the character position and animation
        '''
        #pos_update = {UP:Point(0,1) ,DOWN:Point(0,-1) ,RIGHT:Point(1,0) ,DOWN:Point(-1,0)}
        #new_position = self.position + pos_update[self.direction]
        #calculate the new position
        if self.moving:
            return

        #self.world.playerDead()
        self.changeDirection(self.future_direction)
        new_position = self.position + self.direction
        #If the character can move to the new position update the position and animation
        if self.world.canMove(new_position):
            self.move(new_position)
            #self.world.testCoin()

        #self.animation_position = self.position

    def updateAnimation(self):
        '''
            Update the animation
        '''
        self.animation = (self.animation + 0.25)%Character.ANIMATIONS
        a = 2/Character.SIZE
        self.animation_position += self.direction * Point(a, a)
        
        if (self.direction is UP and self.animation_position.y <= self.position.y) or (self.direction is DOWN and self.animation_position.y >= self.position.y) or (self.direction is RIGHT and self.animation_position.x >= self.position.x) or (self.direction is LEFT and self.animation_position.x <= self.position.x):
               self.moving = False
               self.animation_position = self.position
               self.world.testCoin()
               

