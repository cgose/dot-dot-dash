"""
@author Cameron Gose
@summary: Creates a sprite object which will be all objects that can interact with the Player class
"""
from Drawable import *
class Sprite(Drawable):
    def __init__(self,imageloc):
        super(Sprite, self).__init__(imageloc)
        self.xVel = 0
        self.yVel = 0
        self.changePhysicality()
        self.name = ""
        
    def setXVel(self,vel):
        self.xVel = vel
    
    def setYVel(self,vel):
        self.yVel = vel
    """
    @summary: Moves Sprite based on its x Velocity and y Velocity
    @precondition: None
    @postcondition: 
    @return: None
    """
    def move(self):
        self.loc[0] = self.loc[0] + self.xVel
        self.loc[1] = self.loc[1] + self.yVel
        
    def reposition(self,newLoc):
        self.setX(newLoc[0])
        self.setY(newLoc[1])    
        
    def updateVel(self, xAccel, yAccel):
        self.xVel = self.xVel + xAccel
        self.yVel = self.yVel + yAccel
        """
        Sprite update itself according to various situations
        ***Note*** might have to pass in Sprite so it reacts to things***
        """
    def update(self):
        """
        Will probably have to be done separate depending on sprite behavior
        Will most likely contain some sort of AI
        """


    """
    Param: Drawable[]
    Check if Sprite has collided with any other object drawn on stage and resolves collision
    
    @note: will remove as I decided to create a Collision Detector Object that will handle all collisions.
    """
    def checkCollision(self,drawableArray):
        for x in drawableArray:
            #if object is physical
            #check for collision
            """currently only checking player collision will have to change if statement later"""
            if(x.getPhysicality() == True and x.name != "player"):

                #check for collision
                if(((self.getXCollision()[1] >= x.getXCollision()[0]) and
                   (self.getXCollision()[0] <= x.getXCollision()[1])) and
                   ((self.getYCollision()[1] >= x.getYCollision()[0]) and
                    (self.getYCollision()[0] <= x.getYCollision()[1]))):
                    """
                    ***Test***
                    """
                
                    #Check if above or below object of object
                    if((self.getYCollision()[0] <= x.getYCollision()[0])):
                        self.reposition((self.getX(),x.getYCollision()[0]-self.getHeight()))
                        self.setYVel(0)
                    elif(self.getYCollision()[0] >= x.getYCollision()[1]):
                        #collision will cause self to stop
                        self.reposition((self.getX(),x.getYCollision()[1]))
                        self.setYVel(0)
                    #Check if on the left or right of object
                    elif(self.getXCollision()[0] <= x.getXCollision()[0]):
                        self.reposition((x.getXCollision()[0] - self.getWidth(),self.getY()))
                    elif(self.getXCollision()[0] >= x.getXCollision()[1]):
                        self.reposition((x.getXCollision()[1],self.getY()))
                    
                
                #check where self is colliding (what side of object)
                
                """
                @todo: Create method onCollision that determines effect of collision based on what type of sprite. Or create classes that inherit from Sprite
                create function for each one. Second option probably best.
                """
                """
                def resolveCollision(self):
                    #Will resolve based on type of object
                    #enemy will probaby move back and forward if they collide into a object
                """
