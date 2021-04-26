import pygame, math, sys, random, os, time
from threading import Event
from colors import *
from gameClasses import *
import json

gameSpeed = 1
clock = pygame.time.Clock()
delta = 0
fps = 60

fObj = open('data.json',)

ogdata = json.load(fObj)

print(ogdata)

speedx = 0
speedy = 0
fObj.close()

print(ogdata["Packs"][0]["creator"])
print(ogdata["Packs"][0]["bgColor"])
bgColor = ogdata["Packs"][0]["bgColor"]

textColor = ogdata["Packs"][0]["textColor"]
textBhColor = ogdata["Packs"][0]["textBhColor"]
topColor = ogdata["Packs"][0]["topColor"]
outlineColor = ogdata["Packs"][0]["outlineColor"]
    


class Cursor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/cursor2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.posx = x
        self.posy = y
    def move(self, speedx, speedy):
        self.rect.x += speedx
        self.rect.y += speedy
        speedx = 0
        speedy = 0
        self.posx = self.rect.x
        self.posy = self.rect.y


coolcolor = 255,128,128

#bgColor = (47,120,173)
#textColor = (255,255,255)
#textBhColor = (0,0,0)
#topColor = (116,31,36)
#outlineColor = (255,255,255)

displayWidth = 1280
displayHeight = 720
pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Quizme')
font1 = pygame.font.SysFont(None, 30)
spriteList = pygame.sprite.Group()

menuCursor = Cursor(51,232)
cursor = pygame.sprite.Group()
cursor.add(menuCursor)

def LevelPack(bgColor,textColor,textBhColor,topColor,outlineColor,x,y,image, name, score, difficulty, creator):
    testButton = Quad((bgColor), x,y, 256, 256)

    testImage = Image(image,testButton.rect.x + 10,testButton.rect.y + 35)
    testButton3 = Quad(outlineColor, testButton.rect.x + 5, testButton.rect.y + 30, 138,138)
    testButton2 = Quad(topColor, testButton.rect.x, testButton.rect.y, 256,25)

    testText = Text(textColor, (testButton.rect.x + 5),(testButton.rect.y + 3),font1,name)
    testTextBh = Text(textBhColor, (testButton.rect.x + 4),(testButton.rect.y + 2),font1,name)

    testText2 = Text(textColor,(testButton.rect.x + 5),(testButton.rect.y + 173),font1,"Max Score: " + score)
    testText2Bh = Text(textBhColor,(testButton.rect.x + 4),(testButton.rect.y + 172),font1,"Max Score: " + score)

    testText3 = Text(textColor,(testButton.rect.x + 5),(testButton.rect.y + 193),font1,"Difficulty: " + difficulty)
    testText3Bh = Text(textBhColor,(testButton.rect.x + 4),(testButton.rect.y + 192),font1,"Difficulty: " + difficulty)

    testText4 = Text(textColor,(testButton.rect.x + 5),(testButton.rect.y + 213),font1,"Creator: " + creator)
    testText4Bh = Text(textBhColor,(testButton.rect.x + 4),(testButton.rect.y + 212),font1,"Creator: " + creator)


    spriteList.add(testButton)

    spriteList.add(testButton2)
    spriteList.add(testButton3)
    spriteList.add(testImage)

    spriteList.add(testText)
    spriteList.add(testText2)
    spriteList.add(testText3)
    spriteList.add(testText4)
    spriteList.add(testTextBh)
    spriteList.add(testText2Bh)
    spriteList.add(testText3Bh)
    spriteList.add(testText4Bh)



levelPackPos = [51,358,665,972]
LevelPack((47,120,173),(0,0,0),(255,255,255),(116,31,36),(0,0,0), levelPackPos[0],232,"assets/tempAlbumArt.jpg", "Boa - Twilight", "30000", "*****", "Sailor_Schwartz")

LevelPack((47,255,173),(255,120,173),(47,120,255),(255,120,255),(255,255,173), levelPackPos[1],232,"assets/cursor.png", "Hardcore", "2352", "****", "agadsg")

LevelPack((47,255,173),(255,120,173),(47,120,255),(255,120,255),(255,255,173), levelPackPos[2],232,"assets/cursor.png", "MCR - Bullets", "30000", "***", "tjrrtj")    

LevelPack((47,120,123),(123,120,173),(123,120,123),(47,123,123),(47,120,173), levelPackPos[3],232,"assets/tempAlbumArt.jpg", "Bibimbam", "30000", "*******", "erwy")
print(levelPackPos)




update = True
while update == True:
    gameDisplay.fill(lightPurple)
    
    spriteList.draw(gameDisplay)
    cursor.draw(gameDisplay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if menuCursor.rect.x == levelPackPos[0]:
                    pass
                if menuCursor.rect.x == levelPackPos[1]:
                    menuCursor.rect.x = levelPackPos[0]
                if menuCursor.rect.x == levelPackPos[2]:
                    menuCursor.rect.x = levelPackPos[1]
                if menuCursor.rect.x == levelPackPos[3]:
                    menuCursor.rect.x = levelPackPos[2]
            if event.key == pygame.K_RIGHT:
                if menuCursor.rect.x == levelPackPos[3]:
                    pass
                if menuCursor.rect.x == levelPackPos[2]:
                    menuCursor.rect.x = levelPackPos[3]
                if menuCursor.rect.x == levelPackPos[1]:
                    menuCursor.rect.x = levelPackPos[2]
                if menuCursor.rect.x == levelPackPos[0]:
                    menuCursor.rect.x = levelPackPos[1]
                    

    pygame.display.update()
    clock.tick(fps)

