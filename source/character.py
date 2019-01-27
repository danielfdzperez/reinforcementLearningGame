from point import *
import pygame
from world import *
from common import *
class Character:
    
    '''
        Class used for the characters of the game
    '''

    ID = 0
    #Constants

    #Number of animations
    ANIMATIONS = 3
    #Size of the image
    SIZE = 32

    def __init__(self, position, world,sprites):
        '''
            Constructor
            x and y -> Position
            world -> Controller
            sprite -> Sprite sheet name
        '''
        self.id = Character.ID
        Character.ID += 1
        self.position = position
        
        self.direction = RIGHT #The current direction
        self.future_direction = RIGHT
        self.world = world
        self.state = 0

        self.sprite_up    =[]
        self.sprite_down  =[]
        self.sprite_right =[]
        self.sprite_left  =[]
        #Loads the sprites of each direction
        for sprite in sprites:
            sheet = SpriteSheet(sprite)
            self.sprite_up.append(self.loadSprite(sheet,Character.SIZE*3))
            self.sprite_down.append(self.loadSprite(sheet,Character.SIZE*0))
            self.sprite_right.append(self.loadSprite(sheet,Character.SIZE*2))
            self.sprite_left.append(self.loadSprite(sheet,Character.SIZE*1)) 
        self.current_sprite = self.sprite_right
        self.animation = 0 #Current animation frame

        self.animation_position = self.position
        self.moving = False
        
    def loadSprite(self,sheet,raw):
        '''
            Load an sprite and return a list with all the images
            sheet -> sprite sheet
            raw -> Raw to load
        '''
        return [sheet.get_image(0,raw,Character.SIZE,Character.SIZE),
                sheet.get_image(Character.SIZE,raw,Character.SIZE,Character.SIZE),
                sheet.get_image(Character.SIZE*2,raw,Character.SIZE,Character.SIZE)]

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
            self.world.testCoin()

        #self.animation_position = self.position

    def move(self,new_position):
        self.animation_position = self.position
        self.position = new_position
        #self.position = self.future_position

        self.moving = True
        #self.updateAnimation()

    def moveTo(self, new_position):
        self.future_position = new_position
        self.moving = True

    def updateAnimation(self):
        '''
            Update the animation
        '''
        self.animation = (self.animation + 0.25)%Character.ANIMATIONS
        a = 2/Character.SIZE
        self.animation_position += self.direction * Point(a, a)
        
        if (self.direction is UP and self.animation_position.y <= self.position.y) or (self.direction is DOWN and self.animation_position.y >= self.position.y) or (self.direction is RIGHT and self.animation_position.x >= self.position.x) or (self.direction is LEFT and self.animation_position.x <= self.position.x):
               self.moving = False
               #self.move()
               self.animation_position = self.position
               #print('entra')
               #self.world.testCoin()
        #future_pos = (self.position + self.direction) * Character.SIZE
        #if self.animation_position >= 
    
    def draw(self, ctx, x, y):
        '''
            Draw the character

            ctx -> screen where thw image is going to be drawed.
        '''
        #pygame.draw.rect(ctx, (0,255,0), square(self.position.y*Tile.SIZE, self.position.x*Tile.SIZE,Tile.SIZE))
        #ctx.blit(self.current_sprite[self.animation], (self.position.x*Character.SIZE,self.position.y*Character.SIZE))
        ctx.blit(self.current_sprite[self.state][int(self.animation)], (self.animation_position.x * Character.SIZE,self.animation_position.y * Character.SIZE))
        if self.moving:
            self.updateAnimation()
        #print(self.animation_position)


    def futureDirection(self,direction):
        if direction is UP:
            self.future_direction = UP
        if direction is DOWN:
            self.future_direction = DOWN
        if direction is RIGHT:
            self.future_direction = RIGHT
        if direction is LEFT:
            self.future_direction = LEFT


    def changeDirection(self, direction):
        '''
            Change the direction of the character and its sprite

            direction -> new direction
        '''
        #if self.moving:
        #    return

        if direction is UP:
            self.direction = UP
            self.current_sprite = self.sprite_up
            #change animation
        if direction is DOWN:
            self.direction = DOWN
            self.current_sprite = self.sprite_down
        if direction is RIGHT:
            self.direction = RIGHT
            self.current_sprite = self.sprite_right
        if direction is LEFT:
            self.direction = LEFT
            self.current_sprite = self.sprite_left

        




        
