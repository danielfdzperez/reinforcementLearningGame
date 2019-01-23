import pygame
from tile import *
from map import *
from maps import *
from common import *
def drawRect(screen, rgb, x, y, width, height):
    rect = pygame.Rect(x,y,width, height)
    pygame.draw.rect(screen, rgb, rect) 

pygame.init()
screen = pygame.display.set_mode((400,400),pygame.RESIZABLE)

done = False
r = 0
#event1 = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_UP})
event1 = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': pygame.K_UP, 'mod': 4096, 'scancode': 111})
event2 = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': pygame.K_DOWN, 'mod': 4096, 'scancode': 111})
pygame.event.post(event1)
map = Map(map1)

print( aStar(Point(1,1),Point(4,2),map), 5 )
print( aStar(Point(5,1),Point(7,1),map), 12)
print( aStar(Point(7,8),Point(2,4),map),10)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    map.draw(screen,0,0)
    
    pygame.display.flip()



