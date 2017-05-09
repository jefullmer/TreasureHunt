##Main

import pygame, sys
from pygame.locals import *
from random import randint

from playerClass import player
from oceanClass import ocean
from coinClass import coin
from bombClass import bomb
from menuClass import menu


pygame.mixer.pre_init(44100, -16, 2, 1024*4)
pygame.init()

clock = pygame.time.Clock()
FPS = 60
sWidth = 800
sHeight = 600
screen = pygame.display.set_mode((sWidth, sHeight))

bgColor = (55, 55, 55)

explosionSound = pygame.mixer.Sound("audio/explosion.wav")
pickupSound = pygame.mixer.Sound("audio/pickup.wav")
blipSound = pygame.mixer.Sound("audio/blip.wav")

hero = player(screen)
backGround = ocean(screen)

coinList = pygame.sprite.Group()
bombList = pygame.sprite.Group()


overLay = menu(screen)
overLay.makeText([200, 50], 'Treasure: 0', [15, 25], (0, 0, 0))
overLay.makeText([200, 50], 'Treasure Left: 3', [550, 25], (0, 0, 0))
overLay.makeText([150, 25], 'Current Level: 1', [300, 75], (0, 0, 0))
overLay.makeText([200, 50], 'Time: 60', [275, 15], (0, 0, 0))

overLay.makeButton([450, 200], pygame.image.load('sprites/gameOverMessage.png'), [175, 400])#0 - game over
overLay.makeButton([450, 200], pygame.image.load('sprites/message1.png'), [175, 400])#1 - message1
overLay.makeButton([450, 200], pygame.image.load('sprites/message2.png'), [175, 400])#2 - message2
overLay.makeButton([450, 200], pygame.image.load('sprites/message3.png'), [175, 400])#3 - message3
overLay.makeButton([450, 200], pygame.image.load('sprites/message4.png'), [175, 400])#4 - message4
overLay.makeButton([450, 200], pygame.image.load('sprites/gamePaused.png'), [175, 400])#5 - pause

for x in overLay.buttonList:
    x.active = False



def setNewItems(maxCoins, maxBombs):
    coinList.empty()
    bombList.empty()
    for x in range(maxCoins):
        coinList.add(coin(screen, [randint(-325, 1100), randint(-225, 650)]))
    for y in range(maxBombs):
        bombList.add(bomb(screen, [randint(-325, 1100), randint(-225, 650)]))

def displayClock(seconds, count, go):
    count += 1
    if count >= FPS:
        seconds -= 1
        count = 0
    overLay.textList[3].changeText('Time: ' + str(seconds))
    if seconds <= 0:
        go = False
    return seconds, count, go

def gameOver():
    go = True
    overLay.buttonList[0].active = True
    while go == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()        
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    blipSound.play()
                    go = False
                    overLay.buttonList[0].active = False
                    
                    
                
        overLay.displayScreen()
        clock.tick(FPS)
        pygame.display.update()        
    
    gameLoop()

def startGame():
    go = True
    message = 1
    overLay.buttonList[message].active = True
    while go == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()        
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    overLay.buttonList[message].active = False
                    message += 1
                    blipSound.play()
                    if message < 5:
                        overLay.buttonList[message].active = True
                    else:
                        go = False
                        overLay.buttonList[4].active = False
                    
                    
                
        overLay.displayScreen()
        clock.tick(FPS)
        pygame.display.update()

def pausedGame():
    go = True
    overLay.buttonList[5].active = True
    while go == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()        
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    blipSound.play()
                    go = False
                    overLay.buttonList[5].active = False
                    
                    
                
        overLay.displayScreen()
        clock.tick(FPS)
        pygame.display.update()    

def gameLoop():
    go = True
    backGround.resetPosition()
    rotateSpeed = 0
    rotateR = 0
    rotateL = 0
    speed = 0
    maxSpeed = 6
    minSpeed = -3
    forward = False
    reverse = False
    score = 0
    maxTreasure = 3
    treasureLeft = maxTreasure
    currentLevel = 1
    
    bombs = 0
    
    setNewItems(maxTreasure, bombs)  
    
    seconds = 60
    count = 0
    
    
    overLay.textList[0].changeText(('Treasure: ' + str(score)))
    overLay.textList[1].changeText(('Treasure Left: ' + str(treasureLeft)))
    overLay.textList[2].changeText(('Current Level: ' + str(currentLevel)))    
    
    while go:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_a:
                    rotateL = 2
                elif event.key == K_d:
                    rotateR = -2
                    
                if event.key == K_w:
                    forward = True                    
                elif event.key == K_s:
                    reverse = True                    
            elif event.type == pygame.KEYUP:
                if event.key == K_a:                    
                    rotateL = 0
                elif event.key == K_d:                    
                    rotateR = 0
                    
                if event.key == K_w:
                    forward = False
                elif event.key == K_s:
                    reverse = False
                
                if event.key == K_SPACE:
                    blipSound.play()
                    pausedGame()
        screen.fill(bgColor)
        backGround.display()
        
        if forward == True:
            speed += .05
            if speed >= maxSpeed:
                speed = maxSpeed
        if reverse == True:
            speed -= .2
            if speed <= minSpeed:
                speed = minSpeed            
        
        rotateSpeed += rotateR + rotateL
        hero.rotatePlayer(rotateSpeed)
        
        collisionList = pygame.sprite.spritecollide(hero, coinList, True)
        for col in collisionList:
            pickupSound.play()
            score += 1
            treasureLeft -= 1
            seconds += 2
            overLay.textList[0].changeText(('Treasure: ' + str(score)))
            overLay.textList[1].changeText(('Treasure Left: ' + str(treasureLeft)))
            if treasureLeft == 0:
                score = 0
                maxTreasure += 2
                treasureLeft = maxTreasure
                bombs += 1
                currentLevel += 1
                rotateSpeed = 0
                speed = 0
                backGround.resetPosition()
                setNewItems(maxTreasure, bombs)
                overLay.textList[0].changeText(('Treasure: ' + str(score)))
                overLay.textList[1].changeText(('Treasure Left: ' + str(treasureLeft)))
                overLay.textList[2].changeText(('Current Level: ' + str(currentLevel)))
        explodeList = pygame.sprite.spritecollide(hero, bombList, True)
        for exp in explodeList:
            explosionSound.play()
            seconds -= 10
        
        
        for x in coinList:
            x.display()
            x.move(hero.vector2, speed, backGround.touchingHorz, backGround.touchingVert)
        for y in bombList:
            y.display()
            y.move(hero.vector2, speed, backGround.touchingHorz, backGround.touchingVert)
        
        hero.displayPlayer()
        backGround.moveBG(hero.vector2, speed)
        
        seconds, count, go = displayClock(seconds, count, go)
        
        overLay.displayScreen()
        clock.tick(FPS)
        pygame.display.update()
    gameOver()
startGame()
gameLoop()