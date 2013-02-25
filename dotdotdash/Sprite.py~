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
        Will probably have to be done separate depending on sprite behaviour
        Will most likely contain some sort of AI
        """
        """
        Check if Sprite has collided with any other object drawn on stage
        """
    def checkCollision(self,drawableArray):
        for x in drawableArray:
            #if object is physical
            #check for collision
            if(x.getPhysicality() == True and x.name != "player"):
                #check for collision
                #print(self.loc)
                if(((self.getXCollision()[1] >= x.getXCollision()[0]) and
                   (self.getXCollision()[0] <= x.getXCollision()[1])) and
                   ((self.getYCollision()[1] >= x.getYCollision()[0]) and
                    (self.getYCollision()[0] <= x.getYCollision()[1]))):
                    """
                    ***Test***
                    """
                    # print("There was a successful collision YAY! or NAY!")
                    #Check if on the left or right of object
                    if(self.getXCollision()[0] <= x.getXCollision()[0]):
                        self.reposition((x.getXCollision()[0] - self.getWidth(),self.getY()))
                    elif(self.getXCollision()[0] >= x.getXCollision()[1]):
                        self.reposition((x.getXCollision()[1],self.getY()))
                    
                    #Check if above or below object of object
                    elif((self.getYCollision()[0] <= x.getYCollision()[0])):
                        self.reposition((self.getX(),x.getYCollision()[0]-self.getHeight()))
                        self.setYVel(0)
                    elif(self.getYCollision()[0] >= x.getYCollision()[1]):
                        #collision will cause self to stop
                        self.reposition((self.getX(),x.getYCollision()[1]))
                        self.setYVel(0)
                #check where self is colliding (what side of object)
                
                
            