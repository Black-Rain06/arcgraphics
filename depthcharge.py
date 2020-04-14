# class for depth charges
# phase four will introduce depth charges
from graphics import *

class DepthCharge:
   
   def __init__(self,center,win):
      self.win = win
      self.velocity = 600
      self.tail = Polygon(Point(center + 4,154), Point(center + 14,154), Point(center + 14,141))
      self.tail.setFill("yellow")
      self.tail.setOutline("yellow")
      self.tail.draw(win)
      self.tail1 = Polygon(Point(center - 6,154), Point(center - 16,154), Point(center -16,141))
      self.tail1.setFill("yellow")
      self.tail1.setOutline("yellow")
      self.tail1.draw(win)
      self.bomb = Oval(Point(center - 14,150), Point(center + 14,190))
      self.bomb.setFill("red")
      self.bomb.setOutline("black")
      self.bomb.draw(win)
      self.point = self.bomb.getCenter()
      


      self.bombList= [self.tail, self.tail1, self.bomb, self.point]
      

      
   def getBody (self):
      return self.bomb

      
         

            
   def move(self,timeStep):

      for i in self.bombList:
         i.move(0,timeStep*self.velocity)

      
   def pastBottom(self):
      
      if self.point.getY() > 829:  
         return True
   
   def undraw(self):
      for i in self.bombList:
         i.undraw()
      

if __name__ == "__main__":
   
    from subhuntGUI import GUI
    from subhuntgame import Game
   


    gui = GUI()
    myGame = Game(gui)
    myGame.play()
    




