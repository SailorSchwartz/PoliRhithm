import pygame, math, sys, random, os, time
from threading import Event
from colors import *
from gameClasses import *


gameSpeed = 1
clock = pygame.time.Clock()
delta = 0
fps = 60


coolcolor = 255,128,128

displayWidth = 1280
displayHeight = 720






class levelPack(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image,name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def clicked(self,step):
        self.disable()
    def move(self,step):
        self.rect.x += step
    def delete(self):
        kill()












    
pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Quizme')

   
quadList = pygame.sprite.Group()
spriteList = pygame.sprite.Group()

testQuad = Quad(white,64,64,(1280-128),(720-128))
quadList.add(testQuad)
spriteList.add(testQuad)

update = True
while update == True:
    gameDisplay.fill(lightPurple)
    
    spriteList.draw(gameDisplay)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pass
    pygame.display.update()
    clock.tick(fps)

