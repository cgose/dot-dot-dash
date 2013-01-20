import pygame, Sprite
from Sprite import *
from pygame.locals import *
class Player(Sprite):
    def __init__(self, imageLoc):
        super(Player, self).__init__(imageLoc)
        #player states
        self.jumping = False
        self.walking = False
        self.running = False
        self.crouching = False
        self.sliding = False
        self.attacking = False
        self.name = "player"

    """
    Updates Player according to key events
    pass in pygame.event
    return void
    """
    def update(self,input):
        if input.type == KEYDOWN:
            #print(input.key)
            if input.key == K_DOWN:
                """duck"""
            if input.key == K_RIGHT:
                """move right"""
                self.xVel = 5
                self.walking = True
            if input.key == K_LEFT:
                """move left"""
                self.xVel = -5
                self.walking = True
            if input.key == K_UP:
                """look up"""
            if input.key == K_a and self.walking == True:
                """run"""
                if(self.xVel < 0):
                    self.xVel -= 5
                    self.running = True
                elif (self.xVel > 0):
                    self.xVel += 5
                    self.running = True
            if input.key == K_s:
                """attack"""
            if (input.key == K_SPACE) and (self.yVel == 1) and (self.jumping == False):
                """jump"""
                self.jumping = True
                self.yVel = -10
                self.loc[1] -= 1
            else:
                """Will have to put something else for later"""
        elif input.type == KEYUP:
            if input.key == K_DOWN:
                """stand"""
            if input.key == K_RIGHT:
                """move right"""
                self.xVel = 0
                self.walking = False
            if input.key == K_LEFT:
                """move left"""
                self.xVel = 0
                self.walking = False
            if input.key == K_UP:
                """look up"""
            if input.key == K_a and self.running == True:
                """walk"""
                if(self.xVel < 0):
                    self.xVel += 5
                elif(self.xVel > -5):
                    self.xVel -= 5
                self.running = False
                self.walking = True

            if input.key == K_s:
                """stop attack"""
            else:
                """Will have to put something else for later"""
       
    def move(self):
        if self.loc[1] >= 200:
            self.yVel = 0
            self.jumping = False
            self.loc[1] = 200
        super(Player, self).move()
