##Ocean Class

import pygame
from pygame.locals import *

from vector2 import vect2

class ocean(object):
    
    def __init__(self, surf):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h        
        
        self.image = pygame.image.load('sprites/basicOcean.png')
        self.width, self.height = self.image.get_size()
        
        self.vect = vect2(-((self.width//2)//2), -((self.height//2)//2))
        
        self.rect = Rect(self.vect.vX, self.vect.vY, self.width, self.height)
        
        self.touchingHorz = False
        self.touchingVert = False
    
    def display(self):
        self.surf.blit(self.image, self.rect)
        
    def moveBG(self, vector, speed):
        self.touchingHorz = False
        self.touchingVert = False        
        self.vect.vX += vector.vX * speed
        self.vect.vY += vector.vY * speed
        
        if self.vect.vX >= 300 or self.vect.vX <= -1100:
            self.vect.vX -= vector.vX * speed
            self.touchingHorz = True
        if self.vect.vY >= 200 or self.vect.vY <= -600:
            self.vect.vY -= vector.vY * speed
            self.touchingVert = True
        self.rect.x = self.vect.vX
        self.rect.y = self.vect.vY
    def resetPosition(self):
        self.vect = vect2(-((self.width//2)//2), -((self.height//2)//2))
        self.rect = Rect(self.vect.vX, self.vect.vY, self.width, self.height)