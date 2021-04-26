import pygame, math, sys, random, os, time
from colors import *


class Quad(pygame.sprite.Sprite):
    def __init__(self,color,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class SArrow(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite,scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()
        self.largerImg = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
    def clicked(self,step):
        self.size = self.image.get_size()

class DArrow(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite,scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()
        self.largerImg = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
    def clicked(self,step):
        self.size = self.image.get_size()

class FArrow(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite,scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()
        self.largerImg = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
    def clicked(self,step):
        self.size = self.image.get_size()

class GArrow(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite,scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()
        self.largerImg = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
    def clicked(self,step):
        self.size = self.image.get_size()




class SEnemy(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def clicked(self,step):
        self.disable()
    def move(self,step):
        self.rect.x += step
    def delete(self):
        kill()

class DEnemy(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def clicked(self,step):
        self.disable()
    def move(self,step):
        self.rect.x += step
    def delete(self):
        kill()

class FEnemy(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def clicked(self,step):
        self.disable()
    def move(self,step):
        self.rect.x += step
    def delete(self):
        kill()

class GEnemy(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def clicked(self,step):
        self.disable()
    def move(self,step):
        self.rect.x += step
    def delete(self):
        kill()
    

enemySList = pygame.sprite.Group()
enemyDList = pygame.sprite.Group()
enemyFList = pygame.sprite.Group()
enemyGList = pygame.sprite.Group()
