##Coin Class

import pygame
from pygame.locals import *

from vector2 import vect2

class coin(pygame.sprite.Sprite):
    
    def __init__(self, surf, pos):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.image = pygame.image.load('sprites/chest.png')
        self.width, self.height = self.image.get_size()
        
        self.vect = vect2(pos[0], pos[1])
        
        self.rect = Rect(self.vect.vX, self.vect.vY, self.width, self.height)
        
        self.active = True
        
    def display(self):
        if self.active == True:
            self.surf.blit(self.image, self.rect)
    
    def move(self, vector, speed, touchH, touchV):
        if touchH == False:
            self.vect.vX += vector.vX * speed
        if touchV == False:
            self.vect.vY += vector.vY * speed
        self.rect.x = self.vect.vX
        self.rect.y = self.vect.vY        