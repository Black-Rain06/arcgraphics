# sub manager
# the submanager is the liaison between the various subs and the game engine
from submarine import Submarine
from random import random
from random import choice


class SubManager():
    def __init__(self, win):
        # remember the window for later
        self.win = win
        self.makeProb = .0080
        self.subs = [None, None, None, None, None, None, None,None,None]
        self.pts = 0




    def moveSubs(self, timeStep):
       
        listy = [205, 275, 345, 415, 485,555,625,690,765]
        for i in range(9):
            if self.subs[i] == None:
                if random() < self.makeProb:
                    y = listy[i]
                    self.subs[i] = Submarine(y, self.win)
            else:
                self.subs[i].submove(timeStep)
                if self.subs[i].offScreen():
                    self.subs[i].undraw()
                    self.subs[i] = None


    def checkHits2(self, d):
        for i in range (9):
            if self.subs[i] != None:
                pts = self.subs[i].checkHits3(d)
                
                if pts > 0:
                    self.subs[i].undraw()
                    i = None
                    return pts
        return 0
    

     

   




if __name__ == "__main__":
    from subhuntGUI import GUI
    from subhuntgame import Game
    from submarine import Submarine


    gui = GUI()
    myGame = Game(gui)
    myGame.play()
