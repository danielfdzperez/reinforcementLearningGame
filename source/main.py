import pygame
import world
from tile import *
from maps import *
from textContainer import *
from text import *


MENU_BACKGROUND = (102, 153, 255)
SELECTED_COLOR  = (204, 102, 0)

def main():
    pygame.init()
    size = len(maps[1]) * Tile.SIZE
    
    ctx = pygame.display.set_mode((size,size))
    
    loadingDisplay(ctx)
    
    menu_texts = TextContainer(ctx, 50)
    menu_texts.addText(PLAYER)
    menu_texts.addText(MACHINE)
    
    exit = False

    selected = 0
    
    while not exit:
        ctx.fill(MENU_BACKGROUND)

        if selected == 0:
            pygame.draw.rect(ctx, SELECTED_COLOR, [150, 100, 200, 100])
        else:
            pygame.draw.rect(ctx, SELECTED_COLOR, [150, 200, 200, 100])

        menu_texts[PLAYER].display(ctx, 190, 135)
        menu_texts[MACHINE].display(ctx, 230, 235)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected + 1)%2
                if event.key == pygame.K_DOWN:
                    selected = (selected - 1)%2
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        w = world.World(maps,ctx)
                        w.startGame()
                    else:
                        print("Under construction")
    
    pygame.quit()

if __name__ == "__main__":
    main()
