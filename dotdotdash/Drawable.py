import pygame
from pygame.locals import *

class Drawable(object):
    def __init__(self, imageloc):
        self.loc = [5,50]
        self.height = 10
        self.width = 10
        self.physical = False
        self.picLoc = imageloc
        self.image = pygame.image.load(self.picLoc)
    
    def draw(self,surface):
        surface.blit(self.image, self.loc)
    
    def setPicLoc(self, path):
        self.picLoc = path
    
    def changePhysicality(self):
        if self.physical == False:
            self.physical = True
        else:
            self.physical = False
    
    def move(self,newLoc):
        self.loc[0] = newLoc[0]
        self.loc[1] = newLoc[1]
    
    def getXCollision(self):
        return (self.loc[0],self.loc[0]+self.height)
    
    def getYCollision(self):
        return (self.loc[1],self.loc[1]+self.width)
    def getPhysicality(self):
        return self.physical
    def setX(self,loc):
        self.loc[0] = loc
    def setY(self,loc):
        self.loc[1] = loc
    def getX(self):
        return self.loc[0]
    def getY(self):
        return self.loc[1]
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
