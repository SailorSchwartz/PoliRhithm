import pygame, math, sys, random, os, time
from threading import Event
from colors import *
from gameClasses import *

levelFile = open("songs/packOne/Bassbook/level.txt")
pygame.mixer.init()
pygame.mixer.music.load("songs/packOne/Bassbook/song.mp3")


gameSpeed = 1
clock = pygame.time.Clock()
delta = 0
fps = 60

interval = 1000
nextTick = pygame.time.get_ticks() + interval

coolcolor = 255,128,128


levelPositions = levelFile.readlines()
levelPositions = [x[:-1] for x in levelPositions]

gameTime = 0
BPM = levelPositions[0]
print (BPM)
print(levelPositions)
displayWidth = 1280
displayHeight = 720


#if bpm = 60
#it needs to go 64 px per second


for i in range(1,len(levelPositions)):
    if levelPositions[i] == "S":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
    if levelPositions[i] == "D":
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
    if levelPositions[i] == "F":
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
    if levelPositions[i] == "G":
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)


    if levelPositions[i] == "SD":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
    if levelPositions[i] == "SF":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
    if levelPositions[i] == "SG":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)
        
    if levelPositions[i] == "DF":
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
    if levelPositions[i] == "DG":
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)
        
    if levelPositions[i] == "FG":
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)


    if levelPositions[i] == "SDF":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
    if levelPositions[i] == "SDG":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)
        
    if levelPositions[i] == "DFG":
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)
        
        
    if levelPositions[i] == "SDFG":
        enemyS = SEnemy(0+(64*i),128,"assets/enemys.png")
        enemySList.add(enemyS)
        enemyD = DEnemy(0+(64*i),256,"assets/enemyd.png")
        enemyDList.add(enemyD)
        enemyF = FEnemy(0+(64*i),384,"assets/enemyf.png")
        enemyFList.add(enemyF)
        enemyG = GEnemy(0+(64*i),512,"assets/enemyg.png")
        enemyGList.add(enemyG)
        


shouldMove = False

songPosition = 0.0
songPosInBeats = 0.0
secPerBeats = 0.0
secSinceStart = 0.0

secPerBeats = int(BPM)/64
#60 bpm = 2px per frame, drifts by 64
#120 bpm = 4px per frame, drifts by 128
howMuchMove = (((secPerBeats*-1)*2))

pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Quizme')

def textScore():
    font = pygame.font.SysFont(None, 24)
    score = font.render("Score: " + str(totalScore*10), True, black)
    gameDisplay.blit(score, (20,20))

    
quadList = pygame.sprite.Group()
spriteList = pygame.sprite.Group()

testQuad = Quad((coolcolor), 64, 64, 1152, 592)
quadList.add(testQuad)
spriteList.add(testQuad)

arrowS = SArrow(128,128,"assets/arrows.png",1)
spriteList.add(arrowS)

arrowD = DArrow(128,256,"assets/arrowd.png",1)
spriteList.add(arrowD)

arrowF = FArrow(128,384,"assets/arrowf.png",1)
spriteList.add(arrowF)

arrowG = GArrow(128,512,"assets/arrowg.png",1)
spriteList.add(arrowG)


#enemyS = SEnemy(1024+(128),128,"assets/enemys.png")
#enemySList.add(enemyS)

#enemyD = DEnemy(1024+(256),256,"assets/enemyd.png")
#enemyDList.add(enemyD)
#
#enemyF = FEnemy(1024+(384),384,"assets/enemyf.png")
#enemyFList.add(enemyF)
#
#enemyG = GEnemy(1024+(512),512,"assets/enemyg.png")
#enemyGList.add(enemyG)






totalScore = (len(enemySList) + len(enemyDList) + len(enemyFList) + len(enemyGList)) *64 

print(totalScore)

update = True
while update == True:
    gameDisplay.fill(lightPurple)
    
    quadList.draw(gameDisplay)
    spriteList.draw(gameDisplay)
    enemySList.draw(gameDisplay)
    enemyDList.draw(gameDisplay)
    enemyFList.draw(gameDisplay)
    enemyGList.draw(gameDisplay)
    textScore()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                for enemyS in enemySList:
                 #   print(str(testArrow.rect.x) + " " + str(testEnemy.rect.x))
                    if enemyS.rect.x <= arrowS.rect.x+64: #or
                        if enemyS.rect.x > arrowS.rect.x-64: 
                #            print(str(testEnemy.rect.x - testArrow.rect.x))
                            if (arrowS.rect.x - enemyS.rect.x) + (arrowS.rect.x - enemyS.rect.x) >= 0:
                                totalScore += ((arrowS.rect.x - enemyS.rect.x) * -1)
                            else:
                                totalScore += arrowS.rect.x - enemyS.rect.x
                            enemySList.remove(enemyS)
                            enemyS.move(10000000)
               # print(totalScore)
            if event.key == pygame.K_d:
                for enemyD in enemyDList:
                 #   print(str(testArrow.rect.x) + " " + str(testEnemy.rect.x))
                    if enemyD.rect.x <= arrowD.rect.x+64: #or
                        if enemyD.rect.x > arrowD.rect.x-64: 
                #            print(str(testEnemy.rect.x - testArrow.rect.x))
                            if (arrowD.rect.x - enemyD.rect.x) + (arrowD.rect.x - enemyD.rect.x) >= 0:
                                totalScore += ((arrowD.rect.x - enemyD.rect.x) * -1)
                            else:
                                totalScore += arrowD.rect.x - enemyD.rect.x
                            enemyDList.remove(enemyD)
                            enemyD.move(10000000)
               # print(totalScore)
            if event.key == pygame.K_f:
                for enemyF in enemyFList:
                 #   print(str(testArrow.rect.x) + " " + str(testEnemy.rect.x))
                    if enemyF.rect.x <= arrowF.rect.x+64: #or
                        if enemyF.rect.x > arrowF.rect.x-64: 
                #            print(str(testEnemy.rect.x - testArrow.rect.x))
                            if (arrowF.rect.x - enemyF.rect.x) + (arrowF.rect.x - enemyF.rect.x) >= 0:
                                totalScore += ((arrowF.rect.x - enemyF.rect.x) * -1)
                            else:
                                totalScore += arrowF.rect.x - enemyF.rect.x
                            enemyFList.remove(enemyF)
                            enemyF.move(10000000)
               # print(totalScore)
            if event.key == pygame.K_g:
                for enemyG in enemyGList:
                 #   print(str(testArrow.rect.x) + " " + str(testEnemy.rect.x))
                    if enemyG.rect.x <= arrowG.rect.x+64: #or
                        if enemyG.rect.x > arrowG.rect.x-64: 
                #            print(str(testEnemy.rect.x - testArrow.rect.x))
                            if (arrowG.rect.x - enemyG.rect.x) + (arrowG.rect.x - enemyG.rect.x) >= 0:
                                totalScore += ((arrowG.rect.x - enemyG.rect.x) * -1)
                            else:
                                totalScore += arrowG.rect.x - enemyG.rect.x
                            enemyGList.remove(enemyG)
                            enemyG.move(10000000)
               # print(totalScore)
            elif event.key == pygame.K_w:
                print(str(totalScore))
            elif event.key == pygame.K_q:
                shouldMove = True
                songPosInBeats = 0.0
                pygame.mixer.music.play()
                
    
    for enemyS in enemySList:
        if enemyS.rect.x < arrowS.rect.x-129:
            totalScore -= 64
            enemySList.remove(enemyS)
            enemyS.move(10000000)
    for enemyS in enemySList:
        if shouldMove == True:
            enemyS.move(howMuchMove)
        
    for enemyD in enemyDList:
        if enemyD.rect.x < arrowD.rect.x-129:
            totalScore -= 64
            enemyDList.remove(enemyD)
            enemyD.move(10000000)
    for enemyD in enemyDList:
        if shouldMove == True:
            enemyD.move(howMuchMove)
        
    for enemyF in enemyFList:
        if enemyF.rect.x < arrowF.rect.x-129:
            totalScore -= 64
            enemyFList.remove(enemyF)
            enemyF.move(10000000)
    for enemyF in enemyFList:
        if shouldMove == True:
            enemyF.move(howMuchMove)

    for enemyG in enemyGList:
        if enemyG.rect.x < arrowG.rect.x-129:
            totalScore -= 64
            enemyGList.remove(enemyG)
            enemyG.move(10000000)
    for enemyG in enemyGList:
        if shouldMove == True:
            enemyG.move(howMuchMove)
    pygame.display.update()
    gameTime += 1
    #print(math.ceil(gameTime/60))
    if shouldMove == True:
        songPosInBeats += secPerBeats
        #print(songPosInBeats/int(BPM))
        print((songPosInBeats/int(BPM))/4)
    if songPosInBeats/int(BPM) >= 2.0:
        BestQuad = Quad((126,235,21), 64, 64, 1152, 592)
        quadList.add(testQuad)
        spriteList.add(testQuad)
    ticks = pygame.time.get_ticks()
    if ticks > nextTick:
        nextTick += interval
        gameSpeed += 0.1
    delta = clock.tick(fps) * 0.001
    deltaSpeed = delta * gameSpeed
