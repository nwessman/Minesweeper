import pygame
import constants
from spritesheets_functions import SpriteSheet

class ButtonClass(pygame.sprite.Sprite):

    def __init__(self,im):
        '''Skapar knappar med två bilder, en när musen är på, en när musen är utanför.'''
        super().__init__()
 
        self.buttonList = []
        self.hoverActive = False
        self.sign = ""
        if(im == "PlaySign"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,1120,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,1190,200,70)
            self.buttonList.append(g)
            self.sign = "PlaySign"
        elif(im == "Instructions"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,1260,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,1330,200,70)
            self.buttonList.append(g)
            self.sign = "Instructions"
        elif(im == "Easy"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,0,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,70,200,70)
            self.buttonList.append(g)
            self.sign = "Easy"
        elif(im == "Normal"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,140,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,210,200,70)
            self.buttonList.append(g)
            self.sign = "Normal"
        elif(im == "Hard"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,280,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,350,200,70)
            self.buttonList.append(g)
            self.sign = "Hard"
        elif(im == "Custom"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,560,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,630,200,70)
            self.buttonList.append(g)
            self.sign = "Custom"
        elif(im == "Restart"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,420,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,490,200,70)
            self.buttonList.append(g)
            self.sign = "Restart"
        elif(im == "Meny"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,700,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,770,200,70)
            self.buttonList.append(g)
            self.sign = "Meny"
        elif(im == "Highscore"):
            sprite_sheet = SpriteSheet("graphics/dif_spritesheet.png")
            g = sprite_sheet.get_image(0,840,200,70)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(0,910,200,70)
            self.buttonList.append(g)
            self.sign = "Highscore"
        elif(im == "rArrow"):
            sprite_sheet = SpriteSheet("graphics/alpha_ss.png")
            g = sprite_sheet.get_image(624,0,24,24)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(624,24,24,24)
            self.buttonList.append(g)
            self.sign = "rArrow"
        elif(im == "lArrow"):
            sprite_sheet = SpriteSheet("graphics/alpha_ss.png")
            g = sprite_sheet.get_image(624,0,24,24)
            g = pygame.transform.rotate(g,180)
            self.buttonList.append(g)
            g = sprite_sheet.get_image(624,24,24,24)
            g = pygame.transform.rotate(g,180)
            self.buttonList.append(g)
            self.sign = "lArrow"

        for i in range(len(constants.abc)):
            if(im == constants.abc[i]):
                sprite_sheet = SpriteSheet("graphics/alpha_ss.png")
                g = sprite_sheet.get_image((0+(i*24)),0,24,24)
                self.buttonList.append(g)
                g = sprite_sheet.get_image((0+(i*24)),24,24,24)
                self.buttonList.append(g)
                self.sign = constants.abc[i]

            
            
        self.image = self.buttonList[0]
        self.rect = self.image.get_rect()
    def hover(self):
        '''Ändrar bild om musen är över bilden'''
        self.hoverActive = True
        self.image = self.buttonList[1]
    def stopHover(self):
        '''Ändrar tillbaka om musen är utanför bilden'''
        self.hoverActive = False
        self.image = self.buttonList[0]
    def die(self):
        self.kill()
