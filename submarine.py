# submarine class
from graphics import *
from random import random, randrange, choice
from depthcharge import DepthCharge

class Submarine:
    def __init__(self, y, win):
        
        self.rightEdge = win.width
        self.win = win

        self.y = y
        
        subTail = Polygon(Point(-100,y), Point(-102,y-13), Point(-95,y-13), Point(-85,y))
        subTail.setFill("red")
        subTail.setOutline("red")
        subTail.draw(win)
        subTail1 = Polygon(Point(-100,y), Point(-102,y+13), Point(-95,y+13), Point(-85,y))
        subTail1.setFill("red")
        subTail1.setOutline("red")
        subTail1.draw(win)
        subTail2 = Polygon(Point(-98,y), Point(-112,y-7), Point(-112,y+7))
        subTail2.setFill("red")
        subTail2.setOutline("red")
        subTail2.draw(win)
        self.subBody = Oval(Point(-100,y-15), Point(0,y+15))
        self.subBody.setFill("white")
        self.subBody.setOutline("white")
        self.subBody.draw(win)
        subHead = Polygon(Point(-60,y-11), Point(-53,y-23), Point(-47,y-23), Point(-40,y-11))
        subHead.setFill("white")
        subHead.setOutline("white")
        subHead.draw(win)
        subWindow = Circle(Point(-75,y),5)
        subWindow.setFill("black")
        subWindow.draw(win)
        subWindow1 = Circle(Point(-50,y),8)
        subWindow1.setFill("black")
        subWindow1.draw(win)
        subWindow2 = Circle(Point(-25,y),5)
        subWindow2.setFill("black")
        subWindow2.draw(win)

        self.SubHitbox = Rectangle (Point (-112,y+15), Point(0, y-15))

        self.submarine= [self.SubHitbox, self.subBody, subHead, subTail, subTail1, subTail2, subWindow, subWindow1, subWindow2]

        if choice(["left_right", "right_left"]) == "left_right":
            self.vel = 270 + randrange(-50, 50)
        else:
            self.vel = -270 + randrange(-50, 50)
            for piece in self.submarine:
                piece.move(1300,0)


    def submove(self, timeStep):
        for piece in self.submarine:
            piece.move(timeStep*self.vel,0)

    def offScreen(self):
        if self.subBody.getCenter().getX() < 0 and self.vel < 0:
            return True
        elif self.subBody.getCenter().getX() > 1200 and self.vel > 0:
            return True
        else:
            return False



    def undraw(self):
        
        for x in self.submarine:
            x.undraw()
            
    #ERROR MOST LIKELY IN CHECKHITS3
    def checkHits3(self, d):
        #i took the top bottom and side boundaries of the submarine body with
        #most of the extra parts included (tail but not the sharkfin)

        #same for the bomb except i only included the main bomb body
        
        #EITHER IN DEFINING HITBOX
        SubHitboxTop = ST = self.SubHitbox.getP2().getY()
        SubHitboxBot = SB = self.SubHitbox.getP1().getY()
        SubHitboxRight = SR = self.SubHitbox.getP2().getX()
        SubHitboxLeft = SL = self.SubHitbox.getP1().getX()

        Bomb = DepthCharge.getBody(d)

        BombHitboxTop = BT = Bomb.getP2().getY()
        BombHitboxBot = BB = Bomb.getP1().getY()
        BombHitboxRight = BR = Bomb.getP2().getX()
        BombHitboxLeft = BL = Bomb.getP1().getX()

        #set up a likely wrong condition for whether the sub is hit
        #OR IN THE BOOLEAN
        if ((BL >= SL or BR >= SL) and (BL <= SR or BR <= SR)) and ((BB >= ST or BT >= ST) and (BB <= SB or BT <= SB)):
            pts = 100
            return pts

        else:
            pts = 0
            return pts



if __name__ == "__main__":
    from subhuntGUI import GUI
    from subhuntgame import Game


    gui = GUI()
    myGame = Game(gui)
    myGame.play()
