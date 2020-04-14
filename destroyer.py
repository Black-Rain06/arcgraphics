from graphics import *

class Destroyer:
      def __init__(self, win):

            self.win = win
        # set up some constants
            self.step = 20  # pixels to move each move
            centerX = self.X = win.getWidth() / 2  # center of window
            centerY = self.Y = win.getHeight()/2

        # draw a destroyer centered in window

            self.destroyer = Polygon(Point(517,150), Point(536,170), Point(692,170), Point(711,150))
            self.destroyer.setFill("black")
            self.destroyer.draw(win)
            self.square_1 = Polygon(Point(547,150), Point(551,146), Point(677,146), Point(681,150))
            self.square_1.setFill("black")
            self.square_1.draw(win)
            self.square_2 = Rectangle(Point(563, 140), Point(665,146))
            self.square_2.setFill("black")
            self.square_2.draw(win)
            self.square_3 = Rectangle(Point(605,140), Point(635,130))
            self.square_3.setFill("black")
            self.square_3.draw(win)
            self.square_4 = Rectangle(Point(623,130), Point(630,123))
            self.square_4.setFill("black")
            self.square_4.draw(win)
          
            self.weapon1 = Rectangle(Point(645,133), Point(655,140))
            self.weapon1.setFill("black")
            self.weapon1.draw(win)
            self.shell_1 = Rectangle(Point(655,133), Point(662,134))
            self.shell_1.setFill("black")
            self.shell_1.draw(win)
          
            self.tower1 = Polygon(Point(605,140), Point(590,140), Point(595,118), Point(600,118))
            self.tower1.setFill("black")
            self.tower1.draw(win)
            self.tower2 = Rectangle(Point(591,120), Point(604,118))
            self.tower2.setFill("black")
            self.tower2.draw(win)
            self.tower3 = Circle(Point(597.5,114), 3.5)
            self.tower3.setFill("black")
            self.tower3.draw(win)
            self.tower4 = Line(Point(600,130), Point(610,118))
            self.tower4.draw(win)
            self.tower5 = Line(Point(595,135), Point(585,120))
            self.tower5.draw(win)
            self.center= Point(614,160)

            self.DestroyerList = [self.center,self.destroyer, self.square_1, self.square_2, self.square_3, self.square_4, self.weapon1, self.shell_1, self.tower1, self.tower2, self.tower3, self.tower4, self.tower5]

        # if it has move than one shape, put them in a list for ease of manipulation

      def moveLeft(self):
        for piece in self.DestroyerList:
              piece.move(-50,0)
            
        

      def moveRight(self):
        for piece in self.DestroyerList:
              piece.move(50,0)

      def getCenter (self):

            center = self.center.getX()

            return center

            

if __name__ == "__main__":
    from subhuntGUI import GUI
    from subhuntgame import Game
    

    gui = GUI()
    myGame = Game(gui)
    myGame.play()
