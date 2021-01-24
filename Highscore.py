import pygame
import constants

class HighscoreClass(pygame.sprite.Sprite):

    def __init__(self,t):
        '''Sorterar resultatlistan för visning'''
        super().__init__()
        
        self.font = pygame.font.SysFont("04b19", 25)
        self.image = self.font.render("",True,constants.BLACK)
        self.rect = self.image.get_rect()
        self.posX = 0
        self.posY = 0
        
        self.hsList = []
        with open("Highscore.txt","r") as f:
            data = f.readlines()

        for line in data:
            words = line.split(',')
            for i in range(len(words)):
                words[i] = words[i].replace('\n','')
            self.hsList.append(words[0]+" ("+words[1]+")")

        self.text = self.hsList[t]
            
    def print(self):
        self.image = self.font.render(self.text,True,constants.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY
    def die(self):
        self.kill()
