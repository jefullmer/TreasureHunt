##Menu Class

import pygame
from pygame.locals import *

class menu(object):
    
    def __init__(self, surf):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        self.buttonList = []
        self.textList = []        
        
    def makeButton(self, size, image, pos):
        self.buttonList.append(buttons(self.surf, size, image, pos))
    def makeText(self, size, text, pos, color):
        self.textList.append(texts(self.surf, size, text, pos, color))
        
    def displayScreen(self):
        for x in self.buttonList:
            if x.active == True:
                x.displayButton()
        for x in self.textList:
            x.displayText()    
            
class buttons(object):
    
    def __init__(self, surf, size, image, pos):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.size = size
        self.image = image
        self.pos = pos
        
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
        self.active = True
    
    def displayButton(self):
        self.surf.blit(self.image, self.rect)
    
    def clicked(self, mouseXY):
        mouseRect = pygame.Rect(mouseXY[0], mouseXY[1], 5, 5)
        return mouseRect.colliderect(self.rect)
class texts(object):
    
    def __init__(self, surf, size, text, pos, color):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.titleFont = pygame.font.SysFont("Algerian", 120)
        self.text = text
        self.color = color
        self.size = size
        self.textSurf = self.titleFont.render(self.text, True, self.color, None)
        self.textSurf = pygame.transform.scale(self.textSurf, (self.size[0], self.size[1]))
        self.pos = pos        
    
    def displayText(self):
        self.surf.blit(self.textSurf, self.pos)
    
    def changeText(self, newText):
        self.text = newText
        self.textSurf = self.titleFont.render(self.text, True, self.color, None)
        self.textSurf = pygame.transform.scale(self.textSurf, (self.size[0], self.size[1]))
        