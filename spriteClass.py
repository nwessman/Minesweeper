import pygame
import constants
from spritesheets_functions import SpriteSheet

class SpriteClass(pygame.sprite.Sprite):
    '''Hämtar grafik från filer och tillägnar dem objektet'''

    def __init__(self,im):
        super().__init__()
 
        if(im == "Main"):
            g = pygame.image.load("graphics/home.png").convert()
        elif(im == "Background"):
            g = pygame.image.load("graphics/background.png").convert()
        elif(im == "Box"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,980,200,70)
        elif(im == "Easy"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,0,200,70)
        elif(im == "Normal"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,210,200,70)
        elif(im == "Hard"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,1050,200,70)
        elif(im == "1"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(72,0,24,24)
        elif(im == "2"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(96,0,24,24)
        elif(im == "3"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(120,0,24,24)
        elif(im == "4"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(144,0,24,24)
        elif(im == "5"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(168,0,24,24)
        elif(im == "6"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(192,0,24,24)
        elif(im == "7"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(216,0,24,24)
        elif(im == "8"):
            sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
            g = sprite_sheet.get_image(240,0,24,24)
        elif(im == "Width"):
            sprite_sheet = SpriteSheet("graphics/whm_ss.png")
            g = sprite_sheet.get_image(0,0,200,99)
        elif(im == "Height"):
            sprite_sheet = SpriteSheet("graphics/whm_ss.png")
            g = sprite_sheet.get_image(0,100,200,98)
        elif(im == "Mines"):
            sprite_sheet = SpriteSheet("graphics/whm_ss.png")
            g = sprite_sheet.get_image(0,200,200,100)
        elif(im == "Name"):
            sprite_sheet = SpriteSheet("graphics/whm_ss.png")
            g = sprite_sheet.get_image(0,300,200,100)
        elif(im == "Instructions"):
            g = pygame.image.load("graphics/instructionsMeny.png").convert()
        else:
            sprite_sheet = SpriteSheet("graphics/button_spritesheet.png")           
            if(im == "Pole"):
                g = sprite_sheet.get_image(229,10,60,290)
            g.set_colorkey(constants.WHITE)
        self.image = g
        self.rect = self.image.get_rect()
    def die(self):
        self.kill()
