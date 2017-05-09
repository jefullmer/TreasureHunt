##PlayerClass

import pygame
from pygame.locals import *

from vector2 import vect2

class player(pygame.sprite.Sprite):
    
    def __init__(self, surf):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h
        
        self.image = pygame.image.load('sprites/basicBoat.png')
        self.playerWidth, self.playerHeight = self.image.get_size()
        
        self.vect = vect2((self.sWidth//2) - (self.playerWidth//2), (self.sHeight//2) - (self.playerHeight//2))
        
        self.x = (self.sWidth//2) - (self.playerWidth//2)
        self.y = (self.sHeight//2) - (self.playerHeight//2)
        
        self.rect = Rect(self.vect.vX, self.vect.vY, self.playerWidth, self.playerHeight)
        
        self.rotImg = pygame.transform.rotate(self.image, 0)
        
        self.vector1 = vect2.fromPoints((self.vect.vX, self.vect.vY), (self.vect.vX + 0, self.vect.vX - 10))
        self.vector1 = self.vector1.normalizeV2()
    
    
    def displayPlayer(self):
        self.surf.blit(self.rotImg, self.rect)
    
    def rotatePlayer(self, rotateSpeed):
        self.rotImg = pygame.transform.rotate(self.image, rotateSpeed)
        self.playerWidth, self.playerHeight = self.rotImg.get_size()
        self.vect = vect2((self.sWidth//2) - (self.playerWidth//2), (self.sHeight//2) - (self.playerHeight//2))
        self.rect = Rect(self.vect.vX, self.vect.vY, self.playerWidth, self.playerHeight)
        
        self.vector2 = self.vector1.rotateV2(-rotateSpeed)
        #self.vector1 = self.vector1.normalizeV2