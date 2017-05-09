##Vector2

from math import *

class vect2(object):

    def __init__(self, vXf = 0.0, vYf = 0.0):

        self.vX = vXf
        self.vY = vYf
        self.vector = [self.vX, self.vY]
        
    @staticmethod
    def fromPoints(P1, P2):

        return vect2(P2[0] - P1[0], P2[1] - P1[1])

    def normalizeV2(self):
        
        mag = self.lengthV2()
        X = self.vX / mag
        Y = self.vY / mag

        return vect2(X, Y)
        
    def lengthV2(self):

        LV2 = sqrt((self.vector[0] * self.vector[0])+
                   (self.vector[1] * self.vector[1]))
        return LV2

    def dotProductV2(self, rightV2):

        scalerV2 = ((self.vector[0] * rightV2.vector[0]) + (self.vector[1] * rightV2.vector[1]))

        return scalerV2
        
    def crossProductV2(self, rightV2):

        return (self.vector[0] * rightV2.vector[1] - self.vector[1] * rightV2.vector[0])

    def rotateV2(self, theta):
        rad = radians(theta)
        X = round((self.vX * cos(rad)) - (self.vY * sin(rad)), 3)
        Y = round((self.vX * sin(rad)) + (self.vY * cos(rad)), 3)

        return vect2(X, Y)    