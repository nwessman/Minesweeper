import pygame
import constants
from spritesheets_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

    def __init__(self):
        '''Skapar animationen av spelaren när spelet körs'''
        super().__init__()
        
        self.imList = []
        self.c = 0
        self.state = "idle"
        sprite_sheet = SpriteSheet("graphics/player_ss.png")
        for i in range(0,22):
            g = sprite_sheet.get_image(0,i*80,280,80)
            if(i >= 11):
                g = pygame.transform.scale(g,(560,180))
                g.set_colorkey(constants.WHITE)
            self.imList.append(g)
            

        self.image = self.imList[0]
        self.rect = self.image.get_rect()
        
    def update(self):
        if(self.state == "idle"):
            if(self.c == 2):
               self.c = 0
        elif(self.state == "win"):
            if(self.c == 11):
               self.c = 10
        elif(self.state == "die"):
            if(self.c == 22):
                self.c = 21
        self.image = self.imList[self.c]
        self.c+=1
    def die(self):
        self.kill()
