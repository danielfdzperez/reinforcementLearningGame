import pygame
import time
from point import *
from node import *
from text import *

pygame.init()

#COMMON FUNCTIONS

def loadingDisplay(ctx):
    ctx.fill(BLACK)
    LOADING_TEXT.displayMiddle(ctx)
    pygame.display.flip()


def square(y,x,size):
    '''
        Create a squeare in pygame
        y,x -> Coordinates
        size -> Size of the squeare
    '''
    return pygame.Rect(x,y,size,size)
#import time
def aStar(start_position, target, map, dynamic = False ,max_i = 1000):
    #startt = time.time()
    max_iterations = max_i
    '''
        A* algortihm
        start_position -> The point of the start
        target -> The target point
        map -> The Map

        return a touple: first element is the distance and the second where to move to follow the path
    '''
    close = set() #Visited nodes
    open = [] #Nodes to visit
    find = False #Algortihm found a solutions it will be true

    end = Node(None, target, None) #final node
    start = Node(None, start_position, end) #start node

    open.append(start)

    result = [] #Final path
    current_node = None
    i = 0
    while i < max_iterations and  not find and len(open) > 0:
        i += 1
        open.sort(key=lambda node: node.f)#Sort the list with the minimun f value
        current_node = open.pop(0) #Extract the first node
        close.add(current_node) #Save the node as visited

        #If is the target
        if current_node.equals(end):
            find = True
        #else:
            #Get the neighbours
        #startt = time.time()
        neighbours = map.getNeighboursPosition(current_node.position,dynamic)
        nodes = set()
        for n in neighbours:
            #node = Node(current_node, n, end)
            nodes.add(Node(current_node, n, end))
            #If the node hasn't been visited
            #if node not in close:
            #    open.append(node)
        #endt = time.time()
        #print(endt - startt)
        neighbours = list(nodes-close)
        
        for n in neighbours:
            if n in open:
                index = open.index(n)
                if  n.f < open[index].f:
                    open[index] = n
            else:
                open.append(n)

        

        #open = open + neighbours

    #Create a list with the final path
    while current_node != None:
        #result.append(current_node)
        result.insert(0,current_node)
        current_node = current_node.parent
    #result.reverse()


    #dir = NONE_DIRECTION
    #if len(result) > 1:
    #    dir = direction(start_position,result[1].position) 

    #endt = time.time()
    #print(endt - startt)
    #return (len(result),dir,result)

    #print(i)
    dist = max_iterations
    if find:
        dist = len(result)
    return (dist,result)

def distance(point1, point2, map, dynamic = False,max_i = 100):
    #dist, _, _ = aStar(point1, point2, map)
    dist, _ = aStar(point1, point2, map, dynamic,max_i)
    return dist

def direction(origin, neighbour):
    direction = UP
    
    if origin.x < neighbour.x:
        direction = RIGHT
    if origin.x > neighbour.x:
        direction = LEFT
    if origin.y < neighbour.y:
        direction = DOWN
    #if origin.y > neighbour.y:
    #    direction = UP
    return direction


#CONSTANTS

W = 0 #Walls
P = 1 #Paths
S = 2 #Special
R = 3 #Enemy Respawn
O = 4 #Player Respawn

#Colors
BLACK = (0,0,0)#Color black
WHITE = (255,255,255)#Color black

#Game texts
GAME_OVER = "Game over"
WIN       = "You win"
LOADING   = "Loading ..."
PLAYER    = "Human"
MACHINE   = "IA"

font_display_loading = pygame.font.Font(None, 80)
LOADING_TEXT = Text(LOADING,WHITE,font_display_loading) 


#File name
GRAPHICS = "graphics/"
TILE_MAP_SHEET = GRAPHICS + "tile_image_map.png"
CHARACTER1_SHEET = GRAPHICS + "character1.png"
CHARACTER2_SHEET = GRAPHICS + "character2.png"
COINS = GRAPHICS + "coins.png"
PIZZA = GRAPHICS + "pizza.png"

#Directions
UP    = Point(0,-1)#0
DOWN  = Point(0,1)#1
RIGHT = Point(1,0)#2
LEFT  = Point(-1,0)#3
NONE_DIRECTION = Point(0,0)

PLAYER_EVENTS = {pygame.K_UP:UP, pygame.K_DOWN:DOWN, 
        pygame.K_RIGHT:RIGHT, pygame.K_LEFT:LEFT}
