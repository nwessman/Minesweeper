#This class created by Paul Graven
import pygame
import constants

class SpriteSheet(object):
    """Class to get images from a sprite sheet"""
    
    def __init__(self,file_name):
        """Pass the file name for the sprite sheet"""
        
        #Load the graphic
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    def get_image(self,x,y,width,height):
        """Grab a single image out of a larger spritesheet
        pass in the x, y location of the sprite
        and the width and height of the sprite."""
        
        #Create a new blank image
        image = pygame.Surface([width,height]).convert()
        
        #Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        
        #Assuming black works as the transparent color
        #image.set_colorkey(constants.BLACK)
        
        #return the image
        return image
        
