##Mechanics

import pygame
from pygame.locals import *

class mech(object):
    
    def __init__(self, surf):
        self.surf = surf
        INFO = pygame.display.Info()
        self.sWidth = INFO.current_w
        self.sHeight = INFO.current_h