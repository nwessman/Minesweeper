import pygame
import constants
import random
from spritesheets_functions import SpriteSheet

class Box(pygame.sprite.Sprite):
    """Den här klassen representar lådorna du letar efter minor i"""
    def __init__(self,u):
        super().__init__()
        
        self.boxImage = []
        sprite_sheet = SpriteSheet("graphics/slots_spritesheets.png")
        for x in range(0,13):
            image = sprite_sheet.get_image((x*24),0,24,24)
            self.boxImage.append(image)
        
        self.image = self.boxImage[0]
        self.rect = self.image.get_rect()

        self.over = 0
        self.under = u
        self.mine = 0 #0 = false, 1 = True
        self.nr = 0
        
        self.leftUp = False
        self.up = False
        self.rightUp = False
        self.left = False
        self.right = False
        self.leftDown = False
        self.down = False
        self.rightDown = False
    
    def firstPress(self,obj,row,col,i):
        '''Funktion som körs när första lådan per spel öppnas.'''
        m = 0
        if((i-col-1) >= 0 and ((i-col)%col)!=0 and obj[(i-col-1)].mine == 1):
            obj[(i-col-1)].mine = 0
            m += 1
        if((i-col) >= 0) and obj[(i-col)].mine == 1:
            obj[(i-col)].mine = 0
            m += 1
        if((i-col+1) >= 0 and ((i-col+1)%col)!=0 and obj[(i-col+1)].mine == 1):
            obj[(i-col+1)].mine = 0
            m+=1
        if((i-1) >= 0 and ((i)%col)!=0 and obj[(i-1)].mine == 1):
            obj[(i-1)].mine = 0
            m+=1
        if((i+1) < (row*col) and ((i+1)%col)!=0 and obj[(i+1)].mine == 1):
            obj[(i+1)].mine = 0
            m+=1
        if((i+col-1) < (row*col) and ((i+col)%col)!=0 and obj[(i+col-1)].mine == 1):
            obj[(i+col-1)].mine = 0
            m+=1
        if((i+col) < (row*col) and obj[(i+col)].mine == 1):
            obj[(i+col)].mine = 0
            m+=1
        if((i+col+1) < (row*col) and ((i+col+1)%col)!=0 and obj[(i+col+1)].mine == 1):
            obj[(i+col+1)].mine = 0
            m+=1
        if(self.mine == 1):
            self.mine = 0
            m+=1
        if(m > 0):
            while(m > 0):
                r = random.randint(0,(row*col)-1)
                if(obj[r].mine == False and r != i and r != (i-col-1) and r != (i-col) and r != (i-col+1) and r != (i-1) and r != (i+1) and r != (i+col-1) and r != (i+col+1) and r != (i+col)):
                    obj[r].mine = 1
                    m -= 1    
    def change(self,x):
        self.image = self.boxImage[x]
    def plantFlag(self):
        '''Planterar flagga'''
        if(self.over == 0):
            self.change(1)
            self.over=2
            return 1
        elif(self.over == 2):
            self.change(0)
            self.over=0
            return (-1)
        else:
            return 0
    def press(self,obj,i,row,col):
        '''Körs när spelaren trycker på den här lådan'''
        if(self.over == 0):
            if(self.mine == 0):
                self.check(obj,i,row,col)
            else:
                self.openBox(obj)
                return False
        return True
    def openBox(self,obj,nr=0):
        ''''Öppnar lådan för att se vad som döljer sig bakom'''
        self.over = 1
        if(self.mine == 1):
            for k in range(len(obj)):
                if(obj[k].mine == True):
                    obj[k].change(12)
            self.change(11)
        elif(nr > 0):
            self.change(nr+2)
        else:
            self.change(2)
        
    def check(self,obj,i,row,col,dir=""):
        '''Kontrollerar närstående lådor för att se om de innehåller minor'''
        if(self.over == 0):
            self.nr = 0
            self.leftUp = False
            self.up = False
            self.rightUp = False
            self.left = False
            self.right = False
            self.leftDown = False
            self.down = False
            self.rightDown = False
            
            if((i-col-1) >= 0 and ((i-col)%col)!=0):
                self.nr += obj[(i-col-1)].mine
                self.leftUp = True
            if((i-col) >= 0):
                self.nr += obj[(i-col)].mine
                self.up = True
            if((i-col+1) >= 0 and ((i-col+1)%col)!=0):
                self.nr += obj[(i-col+1)].mine
                self.rightUp = True
            if((i-1) >= 0 and ((i)%col)!=0):
                self.nr += obj[(i-1)].mine
                self.left = True
            if((i+1) < (row*col) and ((i+1)%col)!=0):
                self.nr += obj[(i+1)].mine
                self.right = True
            if((i+col-1) < (row*col) and ((i+col)%col)!=0):
                self.nr += obj[(i+col-1)].mine
                self.leftDown = True
            if((i+col) < (row*col)):
                self.nr += obj[(i+col)].mine
                self.down = True
            if((i+col+1) < (row*col) and ((i+col+1)%col)!=0):
                self.nr += obj[(i+col+1)].mine
                self.rightDown = True
            if(self.nr > 0):
                self.openBox(obj,self.nr) 
            else:
                self.openBox(obj)
                if(self.leftUp == True):
                    obj[(i-col-1)].check(obj,(i-col-1),row,col)
                if(self.up == True):
                    obj[(i-col)].check(obj,(i-col),row,col)
                if(self.rightUp == True):
                    obj[(i-col+1)].check(obj,(i-col+1),row,col)
                if(self.left == True):
                    obj[(i-1)].check(obj,(i-1),row,col)
                if(self.right == True):
                    obj[(i+1)].check(obj,(i+1),row,col)
                if(self.leftDown == True):
                    obj[(i+col-1)].check(obj,(i+col-1),row,col)
                if(self.down == True):
                    obj[(i+col)].check(obj,(i+col),row,col)
                if(self.rightDown == True):
                    obj[(i+col+1)].check(obj,(i+col+1),row,col)

                    
    def die(self):
        self.kill()
