import pygame
 
from common import *
'''
    Original class from the tutorial of pygame
    http://programarcadegames.com/python_examples/es/sprite_sheets/ 
    Here is used with some changes
'''
class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ 
            Constructor
            file_name -> name of the image
        """
 
        # Load the sprite sheet.
        if type(file_name) is str:
            self.sprite_sheet = pygame.image.load(file_name)
        else:
            self.sprite_sheet = file_name#pygame.image.load(file_name)

        #If has an alpha it uses convert_alpha instead of convert
        if self.sprite_sheet.get_alpha():
            self.sprite_sheet = self.sprite_sheet.convert_alpha()
        else:
            self.sprite_sheet = self.sprite_sheet.convert()
 
 
    def get_image(self, x, y, width, height,alpha=BLACK):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        
        # Create a new blank image with alpha background
        image = pygame.Surface([width,height], pygame.SRCALPHA, 32).convert_alpha()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Return the image
        return image
