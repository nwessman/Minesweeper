import pygame
import constants
import spriteClass
import buttonClass
import random
import box
import textClass
import Highscore
import player
from spritesheets_functions import SpriteSheet

class Meny(pygame.sprite.Sprite):
    """Den här klassen skapar menyerna/sidorna vi är på i spelet"""
    def __init__(self):
        super().__init__()

        self.meny = ""
        self.graphList =[]
        self.minefieldStartX = 50
        self.minefieldStartY = 150
            
    def addGraph(self,x,sl,bl,rowL,colL,objectList,mine):
        '''Skapar enskild grafik vid behov'''
        if(x == "Restart"):
            b = buttonClass.ButtonClass("Restart")
            b.rect.x = 500
            b.rect.y = 400
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            self.meny = "Restart"
    def changeMeny(self,x,sl,bl,rowL,colL,objectList,mine,tl,mineX,mineY,hsl,pl):
        '''Ändrar skärmen vi är på'''
        for i in range(len(self.graphList)):
            self.graphList[i].kill()
        self.graphList = []
        if(x == "Main" and self.meny != "Main"):
            s = spriteClass.SpriteClass("Main")
            sl.add(s)
            self.graphList.append(s)
            
            s = spriteClass.SpriteClass("Pole")
            s.rect = (640,275)
            sl.add(s)
            self.graphList.append(s)
            
            b = buttonClass.ButtonClass("PlaySign")
            b.rect.x = 575
            b.rect.y = 300
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("Instructions")
            b.rect.x = 575
            b.rect.y = 400
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            

            
            self.meny = "Main"
        elif(x == "Instructions"):
            s = spriteClass.SpriteClass("Background")
            sl.add(s)
            self.graphList.append(s)
            
            s = spriteClass.SpriteClass("Instructions")
            s.rect = (30,30)
            sl.add(s)
            self.graphList.append(s)
            
            b = buttonClass.ButtonClass("Meny")
            b.rect.x = 400
            b.rect.y = 25
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            
            self.meny = "Instructions"
        elif(x == "Setup" and self.meny != "Setup"):
            s = spriteClass.SpriteClass("Background")
            sl.add(s)
            self.graphList.append(s)

            b = buttonClass.ButtonClass("Easy")
            b.rect.x = 40
            b.rect.y = 65
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("Normal")
            b.rect.x = 40
            b.rect.y = 165
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            
            b = buttonClass.ButtonClass("Hard")
            b.rect.x = 40
            b.rect.y = 265
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("Custom")
            b.rect.x = 40
            b.rect.y = 365
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            s = spriteClass.SpriteClass("Height")
            s.rect.x = 40
            s.rect.y = 470
            sl.add(s)
            self.graphList.append(s)

            s = spriteClass.SpriteClass("Width")
            s.rect.x = 300
            s.rect.y = 470
            sl.add(s)
            self.graphList.append(s)

            s = spriteClass.SpriteClass("Mines")
            s.rect.x = 560
            s.rect.y = 470
            sl.add(s)
            self.graphList.append(s)

            b = buttonClass.ButtonClass("lArrow")
            b.rect.x = 50
            b.rect.y = 470
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            
            b = buttonClass.ButtonClass("rArrow")
            b.rect.x = 205
            b.rect.y = 470
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("lArrow")
            b.rect.x = 310
            b.rect.y = 470
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            
            b = buttonClass.ButtonClass("rArrow")
            b.rect.x = 460
            b.rect.y = 470
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("lArrow")
            b.rect.x = 575
            b.rect.y = 470
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)
            
            b = buttonClass.ButtonClass("rArrow")
            b.rect.x = 720
            b.rect.y = 470
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            text = textClass.TextClass()
            tl.append(text)
            self.graphList.append(text)
            sl.add(text)
            text.posX = 100
            text.posY = 510

            text = textClass.TextClass()
            tl.append(text)
            self.graphList.append(text)
            sl.add(text)
            text.posX = 325
            text.posY = 510

            text = textClass.TextClass()
            tl.append(text)
            self.graphList.append(text)
            sl.add(text)
            text.posX = 600
            text.posY = 510

            s = spriteClass.SpriteClass("Name")
            s.rect.x = 500
            s.rect.y = 36
            sl.add(s)
            self.graphList.append(s)

            b = buttonClass.ButtonClass("lArrow")
            b.rect.x = 691
            b.rect.y = 198
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            j = 0
            k = 0
            for i in range(len(constants.abc)):
                b = buttonClass.ButtonClass(constants.abc[i])
                b.rect.x = 475+(k*24)
                b.rect.y = 150+(j*24)
                sl.add(b)
                self.graphList.append(b)
                bl.append(b)
                if(k > 8):
                    k = 0
                if(i > 8):
                    j = 1
                if(i > 17):
                    j = 2
                k+=1

            
            text = textClass.TextClass()
            tl.append(text)
            self.graphList.append(text)
            sl.add(text)
            text.posX = 515
            text.posY = 80
            
            self.meny = "Setup"
        elif(x == "Minesweeper"):
            s = spriteClass.SpriteClass("Background")
            sl.add(s)
            self.graphList.append(s)
            l = 0
            for x in range(0,rowL):
                for y in range(0,colL):
                    box1 = box.Box(0)
                    sl.add(box1)
                    objectList.append(box1)
                    objectList[l].rect.x = mineX+(y*24)
                    objectList[l].rect.y = mineY+(x*24)
                    l+=1
            b = 0
            while(b < mine):
                r = random.randint(0,(rowL*colL)-1)
                if(objectList[r].mine == False):
                    objectList[r].mine = True
                    b+=1

            s = spriteClass.SpriteClass("Box")
            s.rect.x = 300
            s.rect.y = 30
            sl.add(s)
            self.graphList.append(s)

            s = spriteClass.SpriteClass("Box")
            s.rect.x = 560
            s.rect.y = 30
            sl.add(s)
            self.graphList.append(s)

            b = buttonClass.ButtonClass("Restart")
            b.rect.x = 560
            b.rect.y = 500
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("Meny")
            b.rect.x = 40
            b.rect.y = 500
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            b = buttonClass.ButtonClass("Highscore")
            b.rect.x = 300
            b.rect.y = 500
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            text = textClass.TextClass()
            tl.append(text)
            self.graphList.append(text)
            sl.add(text)
            text.posX = 350
            text.posY = 40
            
            text = textClass.TextClass()
            tl.append(text)
            self.graphList.append(text)
            sl.add(text)
            text.posX = 610
            text.posY = 40

            p = player.Player()
            pl.append(p)
            self.graphList.append(p)
            sl.add(p)
            p.rect.x = 20
            p.rect.y = 20
            self.meny = "Minesweeper"
        elif(x == "Highscore"):
            s = spriteClass.SpriteClass("Background")
            sl.add(s)
            self.graphList.append(s)
            for i in range(1,9):
                for j in range(0,3):
                    s = spriteClass.SpriteClass(str(i))
                    s.rect.x = 40+(260*j)
                    s.rect.y = 150+(30*i)
                    sl.add(s)
                    self.graphList.append(s)

            s = spriteClass.SpriteClass("Easy")
            s.rect.x = 40
            s.rect.y = 30
            sl.add(s)
            self.graphList.append(s)
            
            s = spriteClass.SpriteClass("Normal")
            s.rect.x = 300
            s.rect.y = 30
            sl.add(s)
            self.graphList.append(s)
            
            s = spriteClass.SpriteClass("Hard")
            s.rect.x = 560
            s.rect.y = 30
            sl.add(s)
            self.graphList.append(s)

            b = buttonClass.ButtonClass("Meny")
            b.rect.x = 40
            b.rect.y = 500
            sl.add(b)
            self.graphList.append(b)
            bl.append(b)

            j = 0
            for i in range(0,24):
                h = Highscore.HighscoreClass(i)
                hsl.append(h)
                self.graphList.append(h)
                sl.add(h)
                h.posY = 180+(j*30)
                if(i < 8):
                    h.posX = 70
                elif(i >= 8 and i < 16):
                    h.posX = 330
                else:
                    h.posX = 590
                j += 1
                if(j > 7):
                    j = 0
            
            self.meny = "Highscore"
    
