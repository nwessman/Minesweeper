import pygame
import constants

class TextClass(pygame.sprite.Sprite):
    '''Skapar objekt vi fyller med text'''

    def __init__(self):
        super().__init__()
        
        self.font = pygame.font.SysFont("04b19", 50)
        self.image = self.font.render("",True,constants.BLACK)
        self.rect = self.image.get_rect()
        self.posX = 0
        self.posY = 0
    def update(self,t):
        self.image = self.font.render(t,True,constants.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY
    def die(self):
        self.kill()
