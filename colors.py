import pygame, math, sys, random, os

TRANSPARENT = (255, 128, 255) #FF80FF

darkRed = 170,0,0 #AA0000
red = 255,85,85 #FF5555
gold = 255,170,0 #FFAA00
yellow = 255,255,85 #FFFF55
darkGreen = 0,170,0 #00AA00
green = 85,255,85 #55FF55
aqua = 85,255,255 #55FFFF
darkAqua = 0,170,170 #00AAAA
darkBlue = 0,0,170 #0000AA
blue = 85,85,255 #5555FF
lightPurple = 255,85,255 #FF55FF
darkPurple = 85,0,85 #AA00AA
white = 255,255,255 #FFFFFF
gray = 170,170,170 #AAAAAA
darkGray = 85,85,85 #555555
black = 0,0,0 #000000

colorList=[darkRed,red,gold,yellow,darkGreen,green,aqua,darkAqua,darkBlue,blue,lightPurple,darkPurple,white,gray,darkGray,black]

#darkRedTest = Quad(darkRed, 64*1, 0, 64, 64)
#redTest = Quad(red, 64*2, 0, 64, 64)
#goldTest = Quad(gold, 64*3, 0, 64, 64)
#yellowTest = Quad(yellow, 64*4, 0, 64, 64)
#darkGreenTest = Quad(darkGreen, 64*5, 0, 64, 64)
#greenTest = Quad(green, 64*6, 0, 64, 64)
#aquaTest = Quad(aqua, 64*7, 0, 64, 64)
#darkAquaTest = Quad(darkAqua, 64*8, 0, 64, 64)
#darkBlueTest = Quad(darkBlue, 64*9, 0, 64, 64)
#blueTest = Quad(blue, 64*10, 0, 64, 64)
#lightPurpleTest = Quad(lightPurple, 64*11, 0, 64, 64)
#darkPurpleTest = Quad(darkPurple, 64*12, 0, 64, 64)
#whiteTest = Quad(white, 64*13, 0, 64, 64)
#grayTest = Quad(gray, 64*14, 0, 64, 64)
#darkGrayTest = Quad(darkGray, 64*15, 0, 64, 64)
#blackTest = Quad(black, 64*16, 0, 64, 64)
#
#quadList.add(darkRedTest)
#quadList.add(redTest)
#quadList.add(goldTest)
#quadList.add(yellowTest)
#quadList.add(darkGreenTest)
#quadList.add(greenTest)
#quadList.add(aquaTest)
#quadList.add(darkAquaTest)
#quadList.add(darkBlueTest)
#quadList.add(blueTest)
#quadList.add(lightPurpleTest)
#quadList.add(darkPurpleTest)
#quadList.add(whiteTest)
#quadList.add(grayTest)
#quadList.add(darkGrayTest)
#quadList.add(blackTest)
