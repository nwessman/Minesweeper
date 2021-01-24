import pygame
import constants
import box
import random
import meny
import textClass
from spritesheets_functions import SpriteSheet
from timeit import default_timer as timer
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")
spriteList = pygame.sprite.Group()
objectList = []
rowL = 16
colL = 30
minesN = 10
minefieldStartX = 50
minefieldStartY = 150
buttons = []
firstPress = True
gameActive = False
openAmount = 0
correctFlagged = 0
flagged = 0
endTime = 0
currentTime = 0
start = 0
stop = 0
textList = []
hsTextList = []
minefieldX = 0
minefieldY = 0
flagAmount = 0
txt = ""
playerName = "Nille"
dif = ""
hsLista = []
newHsLista = []
textInputList = []
customH = 10
customW = 10
customM = 10
playerArray = []
animC = 0
#Loopar tills spelaren trycker på avsluta-knappen.
done = False
#Används för att kontrollera hur snabbt spelet uppdateras
clock = pygame.time.Clock()

scr = meny.Meny()
scr.changeMeny("Main",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)

def win():
    '''Körs om spelaren vinner, sparar highscore, spelar vinst-grafiken. '''

    playerArray[0].state = "win"
    if(dif != "Custom"):
        newHsLista = []
        hsLista = []
        with open("Highscore.txt","r") as f:
            data = f.readlines()

        for line in data:
            words = line.split(',')
            for i in range(len(words)):
                words[i] = words[i].replace('\n','')
            hsLista.append([words[0],words[1]])
     
        if(dif == "Easy"):
            for i in range(0,8):
                if(currentTime < int(hsLista[i][1])):
                    newHsLista.append(playerName+","+str(currentTime))
                    for j in range(i+1,8):
                        newHsLista.append(hsLista[j-1][0]+","+hsLista[j-1][1])
                    break
                else:
                    newHsLista.append(hsLista[i][0]+","+hsLista[i][1])
            for i in range(8,24):
                newHsLista.append(hsLista[i][0]+","+hsLista[i][1])
        elif(dif == "Normal"):
            for i in range(0,8):
                newHsLista.append(hsLista[i][0]+","+hsLista[i][1])
            for i in range(8,16):
                if(currentTime < int(hsLista[i][1])):
                    newHsLista.append(playerName+","+str(currentTime))
                    for j in range(i+1,16):
                        newHsLista.append(hsLista[j-1][0]+","+hsLista[j-1][1])
                    break
                else:
                    newHsLista.append(hsLista[i][0]+","+hsLista[i][1])
            for i in range(16,24):
                newHsLista.append(hsLista[i][0]+","+hsLista[i][1])
        elif(dif == "Hard"):
            for i in range(0,16):
                newHsLista.append(hsLista[i][0]+","+hsLista[i][1])
            for i in range(16,24):
                if(currentTime < int(hsLista[i][1])):
                    newHsLista.append(playerName+","+str(currentTime))
                    for j in range(i+1,24):
                        newHsLista.append(hsLista[j-1][0]+","+hsLista[j-1][1])
                    break
                else:
                    newHsLista.append(hsLista[i][0]+","+hsLista[i][1])

        with open("Highscore.txt","w") as f:
            for i in range(0,24):
                f.write(newHsLista[i]+"\n")
            

#Main program loop
while not done:
    #Tar emot användarinput och hanterar den.
    events = pygame.event.get()
    for event in events:
        pos = pygame.mouse.get_pos()
        for b in range(len(buttons)):
            if(pos[0] >= buttons[b].rect.x and pos[0] < (buttons[b].rect.x+buttons[b].rect.width) and pos[1] >= buttons[b].rect.y and pos[1] < (buttons[b].rect.y+buttons[b].rect.height)):
                if(buttons[b].hoverActive == False):
                    buttons[b].hover()
            else:
                if(buttons[b].hoverActive == True):
                    buttons[b].stopHover()
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(gameActive == True):
                for z in range(0,len(objectList)):
                    if(pos[0] >= objectList[z].rect.x and pos[0] < (objectList[z].rect.x+24) and pos[1] >= objectList[z].rect.y and pos[1] < (objectList[z].rect.y+24)):
                        if(event.button == 1):
                            if(firstPress == True):
                                objectList[z].firstPress(objectList,rowL,colL,z)
                                firstPress = False
                                start = timer()
                            gameActive = objectList[z].press(objectList,z,rowL,colL)
                            if(gameActive == False):
                                #Spelet förloras
                                playerArray[0].state = "die"
                                playerArray[0].c = 11
                                playerArray[0].rect.y = -80
                                playerArray[0].rect.x -= 50
                        elif(event.button == 3):
                            flagAmount += objectList[z].plantFlag()
                        openAmount = 0
                        correctFlagged = 0
                        flagged = 0
                        for f in range(len(objectList)):
                            if(objectList[f].over == 1 and objectList[f].mine == False):
                                openAmount += 1
                            if(objectList[f].over == 2):
                                flagged +=1
                                if(objectList[f].mine == True):
                                    correctFlagged +=1
                        if((openAmount == ((rowL*colL)-minesN)) or (correctFlagged == minesN and correctFlagged == flagged)):
                            #Vinst
                            win()
                            gameActive = False
                            for f in range(len(objectList)):
                                if(objectList[f].mine == True):
                                    objectList[f].change(1)
                            stop = timer()
                            endTime = stop - start
            #Hanterar knapptryck
            for b in range(len(buttons)):
                if(buttons[b].hoverActive == True):
                    if(buttons[b].sign == "PlaySign"):
                        buttons = []
                        textList = []
                        playerArray = []
                        scr.changeMeny("Setup",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        break
                    elif(buttons[b].sign == "Easy"):
                        buttons = []
                        textList = []
                        playerArray = []
                        rowL = 9
                        colL = 9
                        minesN = 10
                        
                        minefieldX = (constants.SCREEN_WIDTH/2)-((colL*24)/2)
                        minefieldY = (constants.SCREEN_HEIGHT/2)-((rowL*24)/2)
                        scr.changeMeny("Minesweeper",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        gameActive = True
                        firstPress = True
                        dif = "Easy"
                        break
                    elif(buttons[b].sign == "Normal"):
                        buttons = []
                        playerArray = []
                        textList = []
                        rowL = 16
                        colL = 16
                        minesN = 40
                        minefieldX = (constants.SCREEN_WIDTH/2)-((colL*24)/2)
                        minefieldY = (constants.SCREEN_HEIGHT/2)-((rowL*24)/2)
                        scr.changeMeny("Minesweeper",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        gameActive = True
                        firstPress = True
                        dif = "Normal"
                        break
                    elif(buttons[b].sign == "Hard"):
                        buttons = []
                        textList = []
                        playerArray = []
                        rowL = 16
                        colL = 30
                        minesN = 99
                        minefieldX = (constants.SCREEN_WIDTH/2)-((colL*24)/2)
                        minefieldY = (constants.SCREEN_HEIGHT/2)-((rowL*24)/2)
                        scr.changeMeny("Minesweeper",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        gameActive = True
                        firstPress = True
                        dif = "Hard"
                        break
                    elif(buttons[b].sign == "Custom"):
                        buttons = []
                        playerArray = []
                        textList = []
                        rowL = customH
                        colL = customW
                        minesN = customM
                        minefieldX = (constants.SCREEN_WIDTH/2)-((colL*24)/2)
                        minefieldY = (constants.SCREEN_HEIGHT/2)-((rowL*24)/2)
                        scr.changeMeny("Minesweeper",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        gameActive = True
                        firstPress = True
                        dif = "Custom"
                        break
                    elif(buttons[b].sign == "Restart" and (firstPress == False or flagAmount > 0)):
                        for a in range(len(objectList)):
                            objectList[a].die()
                        playerArray = []
                        objectList = []
                        buttons = []
                        textList = []
                        hsTextList = []
                        flagAmount = 0
                        scr.changeMeny("Minesweeper",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        gameActive = True
                        firstPress = True
                        currentTime = 0
                        break
                    elif(buttons[b].sign == "Meny"):
                        for a in range(len(objectList)):
                            objectList[a].die()
                        objectList = []
                        buttons = []
                        textList = []
                        hsTextList = []
                        playerArray = []
                        flagAmount = 0
                        currentTime = 0
                        gameActive = False
                        scr.changeMeny("Main",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        break
                    elif(buttons[b].sign == "Highscore"):
                        for a in range(len(objectList)):
                            objectList[a].die()
                        objectList = []
                        buttons = []
                        textList = []
                        playerArray = []
                        hsTextList = []
                        flagAmount = 0
                        currentTime = 0
                        gameActive = False
                        scr.changeMeny("Highscore",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        break
                    elif(buttons[b].sign == "Instructions"):
                        buttons = []
                        textList = []
                        playerArray = []
                        scr.changeMeny("Instructions",spriteList,buttons,rowL,colL,objectList,minesN,textList,minefieldX,minefieldY,hsTextList,playerArray)
                        break
                    elif(b == 4 and buttons[b].sign == "lArrow"):
                        customH -= 1
                    elif(b == 5 and buttons[b].sign == "rArrow"):
                        customH += 1
                    elif(b == 6 and buttons[b].sign == "lArrow"):
                        customW -= 1
                    elif(b == 7 and buttons[b].sign == "rArrow"):
                        customW += 1
                    elif(b == 8 and buttons[b].sign == "lArrow"):
                        customM -= 1
                    elif(b == 9 and buttons[b].sign == "rArrow"):
                        customM += 1
                    elif(b == 10 and buttons[b].sign == "lArrow"):
                        if(len(playerName) > 0):
                            playerName = playerName[:-1] 
                    if(len(playerName) < 4):
                        for a in range(len(constants.abc)):
                            if(buttons[b].sign == constants.abc[a]):
                                playerName += constants.abc[a]
                            
    #Spellogik
    if(customW < 4):
        customW = 4
    elif(customW > 30):
        customW = 30
    if(customH < 4):
        customH = 4
    elif(customH > 16):
        customH = 16
    if(customM > ((customH*customW)-9)):
        customM = ((customH*customW)-9)
    if(customM < 1):
        customM = 1
    if(gameActive == True and firstPress == False):
        end = timer()
        currentTime = int(end - start)
        if(currentTime >= 999):
            currentTime = 999
    for t in range(len(textList)):
        if(scr.meny == "Minesweeper"):
            if(t == 0):
                txt = str(minesN-flagAmount)
            elif(t == 1):
                txt = str(currentTime)
        if(scr.meny == "Setup"):
            if(t == 0):
                txt = str(customH)
            elif(t == 1):
                txt = str(customW)
            elif(t == 2):
                txt = str(customM)
            elif(t == 3):
                txt = playerName
        textList[t].update(txt)
    for h in range(len(hsTextList)):
        hsTextList[h].print()

    if(len(playerArray) > 0):
        if(animC == 10):
            playerArray[0].update()
            animC = 0
        animC+=1
    #Ritkod
    screen.fill((constants.WHITE))
    spriteList.draw(screen)      
    pygame.display.update()

    
    clock.tick(60)
    
pygame.quit()
