# final project phase 1
#subhunt.py

from arcgraphics import*
class GUI:
   def __init__(self):
      # the window
      self.win = win = GraphWin("SUBMARINE HUNT",1200,800,autoflush=False)
      win.setBackground(color_rgb(253, 94, 83))
      self.getWidth = 1200
      # instructions, score, time Texts
      self.message = Text(Point(600,80),"Click to begin game")
      self.message2 = Text(Point(600, 103), "This is a subhunt game, click to play this amazing game")
      self.message3 = Text(Point(600, 80), "Click to restart game")

      self.scoreText = Text(Point(200,30),"Score: 0")
      self.timeText = Text(Point(1000,30),"Time Remaining: 0")

      j = Joystick()
      j.set_button('SQUARE', 'a')
      j.set_button('X', 'b')
      j.set_button('CIRCLE', 'c')

      j.set_button('SHARE', 'a')
      j.set_button('PAD', 'b')
      j.set_button('OPTIONS', 'c')
      
      for x in [self.message,self.scoreText,self.timeText]:
         x.setFill("white")
         x.setSize(24)
         x.draw(win)
         
      keys1 = Text(Point(1000,60),"Click P to pause the game")
      keys1.setFill("black")
      keys1.setSize(13)
      keys1.draw(win)
      keys2 = Text(Point(1000,80),"Click Q to quit the game")
      keys2.setFill("black")
      keys2.setSize(13)
      keys2.draw(win)
      keys3 = Text(Point(200,60),"Click left or right arrow key to move the battleship")
      keys3.setFill("black")
      keys3.setSize(13)
      keys3.draw(win)
      keys4 = Text(Point(200,80),"Click the space bar to drop the bomb")
      keys4.setFill("black")
      keys4.setSize(13)
      keys4.draw(win)
      

      self.message2.setFill("white")
      self.message2.setSize(15)
      self.message2.draw(win)

      # lanes
      rect_1 = Rectangle(Point(0,800), Point(1200, 730))
      rect_1.setFill(color_rgb(25,25,112))
      rect_1.setOutline(color_rgb(25,25,112))
      rect_1.draw(win)

      rect_2 = Rectangle(Point(0,730), Point(1200, 660))
      rect_2.setFill(color_rgb(0, 0, 139))
      rect_2.setOutline(color_rgb(0, 0, 139))
      rect_2.draw(win)
      
      rect_3 = Rectangle(Point(0,660), Point(1200, 590))
      rect_3.setFill(color_rgb(0, 0, 205))
      rect_3.setOutline(color_rgb(0, 0, 205))
      rect_3.draw(win)

      rect_4 = Rectangle(Point(0,590), Point(1200, 520))
      rect_4.setFill(color_rgb(0, 0, 255))
      rect_4.setOutline(color_rgb(0, 0, 255))
      rect_4.draw(win)

      rect_5 = Rectangle(Point(0,520), Point(1200, 450))
      rect_5.setFill(color_rgb(30,144,255))
      rect_5.setOutline(color_rgb(30,144,255))
      rect_5.draw(win)

      rect_6 = Rectangle(Point(0,450), Point(1200, 380))
      rect_6.setFill(color_rgb(0,191,255))
      rect_6.setOutline(color_rgb(0,191,255))
      rect_6.draw(win)

      rect_7 = Rectangle(Point(0,380), Point(1200, 310))
      rect_7.setFill(color_rgb(135,206,250))
      rect_7.setOutline(color_rgb(135,206,250))
      rect_7.draw(win)

      rect_8 = Rectangle(Point(0,310), Point(1200, 240))
      rect_8.setFill(color_rgb(135,206,235))
      rect_8.setOutline(color_rgb(135,206,235))
      rect_8.draw(win)

      rect_9 = Rectangle(Point(0,240), Point(1200, 170))
      rect_9.setFill(color_rgb(176,224,230))
      rect_9.setOutline(color_rgb(176,224,230))
      rect_9.draw(win)

      tri_1 = Polygon(Point(0,170), Point(15,160), Point(30,170))
      tri_1.setFill(color_rgb(176,224,230))
      tri_1.setOutline(color_rgb(176,224,230))
      tri_1.draw(win)

      tri_2 = Polygon(Point(30,170), Point(45,160), Point(60,170))
      tri_2.setFill(color_rgb(176,224,230))
      tri_2.setOutline(color_rgb(176,224,230))
      tri_2.draw(win)

      tri_3 = Polygon(Point(60,170), Point(75,160), Point(90,170))
      tri_3.setFill(color_rgb(176,224,230))
      tri_3.setOutline(color_rgb(176,224,230))
      tri_3.draw(win)

      tri_4 = Polygon(Point(90,170), Point(105,160), Point(120,170))
      tri_4.setFill(color_rgb(176,224,230))
      tri_4.setOutline(color_rgb(176,224,230))
      tri_4.draw(win)

      tri_5 = Polygon(Point(120,170), Point(135,160), Point(150,170))
      tri_5.setFill(color_rgb(176,224,230))
      tri_5.setOutline(color_rgb(176,224,230))
      tri_5.draw(win)
      
      tri_6 = Polygon(Point(150,170), Point(165,160), Point(180,170))
      tri_6.setFill(color_rgb(176,224,230))
      tri_6.setOutline(color_rgb(176,224,230))
      tri_6.draw(win)

      tri_7 = Polygon(Point(180,170), Point(195,160), Point(210,170))
      tri_7.setFill(color_rgb(176,224,230))
      tri_7.setOutline(color_rgb(176,224,230))
      tri_7.draw(win)

      tri_8 = Polygon(Point(210,170), Point(225,160), Point(240,170))
      tri_8.setFill(color_rgb(176,224,230))
      tri_8.setOutline(color_rgb(176,224,230))
      tri_8.draw(win)

      tri_9 = Polygon(Point(240,170), Point(255,160), Point(270,170))
      tri_9.setFill(color_rgb(176,224,230))
      tri_9.setOutline(color_rgb(176,224,230))
      tri_9.draw(win)

      tri_10 = Polygon(Point(270,170), Point(285,160), Point(300,170))
      tri_10.setFill(color_rgb(176,224,230))
      tri_10.setOutline(color_rgb(176,224,230))
      tri_10.draw(win)

      tri_11 = Polygon(Point(300,170), Point(315,160), Point(330,170))
      tri_11.setFill(color_rgb(176,224,230))
      tri_11.setOutline(color_rgb(176,224,230))
      tri_11.draw(win)

      tri_12 = Polygon(Point(330,170), Point(345,160), Point(360,170))
      tri_12.setFill(color_rgb(176,224,230))
      tri_12.setOutline(color_rgb(176,224,230))
      tri_12.draw(win)

      tri_13 = Polygon(Point(360,170), Point(375,160), Point(390,170))
      tri_13.setFill(color_rgb(176,224,230))
      tri_13.setOutline(color_rgb(176,224,230))
      tri_13.draw(win)

      tri_14 = Polygon(Point(390,170), Point(405,160), Point(420,170))
      tri_14.setFill(color_rgb(176,224,230))
      tri_14.setOutline(color_rgb(176,224,230))
      tri_14.draw(win)

      tri_15 = Polygon(Point(420,170), Point(435,160), Point(450,170))
      tri_15.setFill(color_rgb(176,224,230))
      tri_15.setOutline(color_rgb(176,224,230))
      tri_15.draw(win)

      tri_16 = Polygon(Point(450,170), Point(465,160), Point(480,170))
      tri_16.setFill(color_rgb(176,224,230))
      tri_16.setOutline(color_rgb(176,224,230))
      tri_16.draw(win)

      tri_17 = Polygon(Point(480,170), Point(495,160), Point(510,170))
      tri_17.setFill(color_rgb(176,224,230))
      tri_17.setOutline(color_rgb(176,224,230))
      tri_17.draw(win)

      tri_18 = Polygon(Point(510,170), Point(525,160), Point(540,170))
      tri_18.setFill(color_rgb(176,224,230))
      tri_18.setOutline(color_rgb(176,224,230))
      tri_18.draw(win)

      tri_19 = Polygon(Point(540,170), Point(555,160), Point(570,170))
      tri_19.setFill(color_rgb(176,224,230))
      tri_19.setOutline(color_rgb(176,224,230))
      tri_19.draw(win)

      tri_20 = Polygon(Point(570,170), Point(585,160), Point(600,170))
      tri_20.setFill(color_rgb(176,224,230))
      tri_20.setOutline(color_rgb(176,224,230))
      tri_20.draw(win)

      tri_21 = Polygon(Point(600,170), Point(615,160), Point(630,170))
      tri_21.setFill(color_rgb(176,224,230))
      tri_21.setOutline(color_rgb(176,224,230))
      tri_21.draw(win)

      tri_22 = Polygon(Point(630,170), Point(645,160), Point(660,170))
      tri_22.setFill(color_rgb(176,224,230))
      tri_22.setOutline(color_rgb(176,224,230))
      tri_22.draw(win)

      tri_23 = Polygon(Point(660,170), Point(675,160), Point(690,170))
      tri_23.setFill(color_rgb(176,224,230))
      tri_23.setOutline(color_rgb(176,224,230))
      tri_23.draw(win)

      tri_24 = Polygon(Point(690,170), Point(705,160), Point(720,170))
      tri_24.setFill(color_rgb(176,224,230))
      tri_24.setOutline(color_rgb(176,224,230))
      tri_24.draw(win)

      tri_25 = Polygon(Point(720,170), Point(735,160), Point(750,170))
      tri_25.setFill(color_rgb(176,224,230))
      tri_25.setOutline(color_rgb(176,224,230))
      tri_25.draw(win)

      tri_26 = Polygon(Point(750,170), Point(765,160), Point(780,170))
      tri_26.setFill(color_rgb(176,224,230))
      tri_26.setOutline(color_rgb(176,224,230))
      tri_26.draw(win)

      tri_27 = Polygon(Point(780,170), Point(795,160), Point(810,170))
      tri_27.setFill(color_rgb(176,224,230))
      tri_27.setOutline(color_rgb(176,224,230))
      tri_27.draw(win)

      tri_28 = Polygon(Point(810,170), Point(825,160), Point(840,170))
      tri_28.setFill(color_rgb(176,224,230))
      tri_28.setOutline(color_rgb(176,224,230))
      tri_28.draw(win)

      tri_29 = Polygon(Point(840,170), Point(855,160), Point(870,170))
      tri_29.setFill(color_rgb(176,224,230))
      tri_29.setOutline(color_rgb(176,224,230))
      tri_29.draw(win)

      tri_30 = Polygon(Point(870,170), Point(885,160), Point(900,170))
      tri_30.setFill(color_rgb(176,224,230))
      tri_30.setOutline(color_rgb(176,224,230))
      tri_30.draw(win)

      tri_31 = Polygon(Point(900,170), Point(915,160), Point(930,170))
      tri_31.setFill(color_rgb(176,224,230))
      tri_31.setOutline(color_rgb(176,224,230))
      tri_31.draw(win)

      tri_32 = Polygon(Point(930,170), Point(945,160), Point(960,170))
      tri_32.setFill(color_rgb(176,224,230))
      tri_32.setOutline(color_rgb(176,224,230))
      tri_32.draw(win)

      tri_33 = Polygon(Point(960,170), Point(975,160), Point(990,170))
      tri_33.setFill(color_rgb(176,224,230))
      tri_33.setOutline(color_rgb(176,224,230))
      tri_33.draw(win)

      tri_34 = Polygon(Point(990,170), Point(1005,160), Point(1020,170))
      tri_34.setFill(color_rgb(176,224,230))
      tri_34.setOutline(color_rgb(176,224,230))
      tri_34.draw(win)

      tri_35 = Polygon(Point(1020,170), Point(1035,160), Point(1050,170))
      tri_35.setFill(color_rgb(176,224,230))
      tri_35.setOutline(color_rgb(176,224,230))
      tri_35.draw(win)

      tri_36 = Polygon(Point(1050,170), Point(1065,160), Point(1080,170))
      tri_36.setFill(color_rgb(176,224,230))
      tri_36.setOutline(color_rgb(176,224,230))
      tri_36.draw(win)

      tri_36 = Polygon(Point(1080,170), Point(1095,160), Point(1110,170))
      tri_36.setFill(color_rgb(176,224,230))
      tri_36.setOutline(color_rgb(176,224,230))
      tri_36.draw(win)

      tri_37 = Polygon(Point(1110,170), Point(1125,160), Point(1140,170))
      tri_37.setFill(color_rgb(176,224,230))
      tri_37.setOutline(color_rgb(176,224,230))
      tri_37.draw(win)

      tri_38 = Polygon(Point(1140,170), Point(1155,160), Point(1170,170))
      tri_38.setFill(color_rgb(176,224,230))
      tri_38.setOutline(color_rgb(176,224,230))
      tri_38.draw(win)

      tri_39 = Polygon(Point(1170,170), Point(1185,160), Point(1200,170))
      tri_39.setFill(color_rgb(176,224,230))
      tri_39.setOutline(color_rgb(176,224,230))
      tri_39.draw(win)


      # horizon

      update()
      win.getMouse()
      self.message.setText("KEEP GOING TILL TIMER RUNS OUT")
      # The game's explanation will disappear after one click
      self.message2.undraw()


   def close(self):
      self.message.setText("Game over\nClick to close")
      self.win.getMouse()
      self.win.close()

   def updateScore(self,score):
      self.scoreText.setText("Score: "+str(score))

   def updateTimer(self,time):
      self.timeText.setText("Time Remaining: {0:0.2f}".format(time))

   

 

if __name__=="__main__":
   from subhuntgame import Game

   gui = GUI()
   myGame = Game(gui)
   myGame.play()
