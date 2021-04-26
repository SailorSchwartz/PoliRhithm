import pygame, math, sys, random, os, time
from colors import *
from gameClasses import *

displayWidth = 1280
displayHeight = 720

speedx = 0
speedy = 0


clock = pygame.time.Clock()


      
class Cursor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/cursor.png")
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

usernames = ["bob","janet","carl","jeff"]
passwords = ["bob","password","gamer","gamer"]


#login = False
#while login == False:
#    usernameBox = input("username?")
#    passwordBox = input("password?")
#    if usernameBox != "" and passwordBox != "":
#        for i in range(0,len(usernames)):
#            if usernameBox == usernames[i]:
#                if passwordBox == passwords[i]:
#                    print("logged in")
#                    login = True
#                    break
#                else:
#                    print("username or password incorrect")
#    else:
#        print("username or password incorrect")
		
		


def startGameButtonClicked(x,y,x2,y2):
    if x == x2 and y == y2:
        exec(open('levelSelect.py').read())
def loginGameButtonClicked(x,y,x2,y2):
    if x == x2 and y == y2:
        print("login clicked")
def settingsGameButtonClicked(x,y,x2,y2):
    if x == x2 and y == y2:
        print("settings clicked")
def quitGameButtonClicked(x,y,x2,y2):
    if x == x2 and y == y2:
        print("quit clicked")
        quit()


pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Quizme')

quadList = pygame.sprite.Group()
spriteList = pygame.sprite.Group()
buttonList = pygame.sprite.Group()

testQuad = Quad((255,128,128), 50, 50, 1180, 620)
quadList.add(testQuad)
spriteList.add(testQuad)





for i in range(0,(int(1280/32)),2):
    for j in range(0,(int(720/32/2)),2):
        measureQuad = Quad((128,255,255),int(i*64),(j*64),64,64)
        quadList.add(measureQuad)
        spriteList.add(measureQuad)
        measureQuad = Quad((128,255,255),int((i*64)+64),((j*64)+64),64,64)
        quadList.add(measureQuad)
        spriteList.add(measureQuad)

startGameButton = Button((8*64), (4*64), "assets/startGameButton.png")
buttonList.add(startGameButton)
spriteList.add(startGameButton)
loginButton = Button((8*64), (5*64), "assets/loginButton.png")
buttonList.add(loginButton)
spriteList.add(loginButton)
settingsButton = Button((8*64), (6*64), "assets/settingsButton.png")
buttonList.add(settingsButton)
spriteList.add(settingsButton)
quitButton = Button((8*64), (7*64), "assets/quitButton.png")
buttonList.add(quitButton)
spriteList.add(quitButton)

menuCursor = Cursor((640-128),(360+24))
spriteList.add(menuCursor)



update = True


while update == True:
    gameDisplay.fill(lightPurple)







    spriteList.draw(gameDisplay)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if menuCursor.rect.y >= 300:
                    menuCursor.move(speedx,-64)
                    speedx = 0
            if event.key == pygame.K_DOWN:
                if menuCursor.rect.y <= 400:
                    menuCursor.move(speedx,+64)
                    speedx = 0
            if event.key == pygame.K_SPACE:
                startGameButtonClicked(menuCursor.rect.x,menuCursor.rect.y,startGameButton.rect.x,startGameButton.rect.y)
                loginGameButtonClicked(menuCursor.rect.x,menuCursor.rect.y,loginButton.rect.x,loginButton.rect.y)
                settingsGameButtonClicked(menuCursor.rect.x,menuCursor.rect.y,settingsButton.rect.x,settingsButton.rect.y)
                quitGameButtonClicked(menuCursor.rect.x,menuCursor.rect.y,quitButton.rect.x,quitButton.rect.y)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speedy = 0
                speedx = 0
            if event.key == pygame.K_DOWN:
                speedy = 0
                speedx = 0



    spriteList.draw(gameDisplay)
    pygame.display.update()
    clock.tick(60)
