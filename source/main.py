import pygame
import world
from tile import *
from maps import *



pygame.init()
size = len(maps[1]) * Tile.SIZE
ctx = pygame.display.set_mode((size,size))

w = world.World(maps,ctx)
w.startGame()

pygame.quit()
