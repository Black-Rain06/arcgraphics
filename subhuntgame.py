# subhunt game
from arcgraphics import *
from destroyer import *
from submanager import *
from submarine import *

class Game:
    def __init__(self, gui):
        self.gui = gui
        self.destroyer = Destroyer(self.gui.win)
        self.done=False
        self.manager = SubManager(gui.win)
        self.depthcharge = []
        self.maxdepth = 5
        
        
        

    def play(self):

        fps = 100  
        self.timeRemaining = 20  
        self.score = 0  
        #  MAIN EVENT LOOP, everything happens from herex
        while self.timeRemaining > 0:
            
            self.manager.moveSubs(1/ fps)
            self.checkKeybord()
            for d in self.depthcharge:
                timestep = 1/fps
                d.move(timestep)
                if d.pastBottom():
                    d.undraw()
                    self.depthcharge.remove(d)
        

                #CANT GET POINTS TO ADD UP
                #if pts > 0:
                    #self.score = self.score + int(pts)
                    #self.gui.updateScore(self.score)
                    
            if self.done:
                break
            # temporary scoring to test GUI scoring update
            # move submarines
            self.manager.moveSubs(1/ fps)
            self.checkHits()
            # update the time remaining  (this can stay)
            self.timeRemaining -= 1 / fps
            self.gui.updateTimer(self.timeRemaining)

            # update screen and control loop speed
            update(fps)
            


        self.gui.close()



    def checkKeybord(self):
        ch = self.gui.win.checkKey()
        if ch == "a":
            self.destroyer.moveLeft()
        elif ch == "c":
            self.destroyer.moveRight()
        elif ch == "p":
            self.gui.message.setText("<Pause> Click to restart")
            self.gui.win.getMouse()
            self.gui.message.setText("Don't give up")
        elif ch == "q":
            self.gui.message.setText("Click to quit")
            self.done =True
        elif ch == "b":
            if len(self.depthcharge) < self.maxdepth:
                center = self.destroyer.getCenter()
                self.depthcharge.append(DepthCharge(center, self.gui.win))
                
    def checkHits(self):
        for d in self.depthcharge:
            pts = self.manager.checkHits2(d)

            if pts > 0:
                self.score = self.score + int(pts)
                self.gui.updateScore(self.score)
                d.undraw()
                self.depthcharge.remove(d)
    

if __name__ == "__main__":  
    from subhuntGUI import GUI
    from destroyer import Destroyer
    from submanager import SubManager
    from depthcharge import DepthCharge


    gui = GUI()
    myGame = Game(gui)
    myGame.play()
    
