
from arcgraphics import*

x, y = 400, 300 #window size
d, t = 13, 13 #Mouse size
win = GraphWin("Window", x, y)
rect = Rectangle(Point(x/d,x/d), Point(y/t,y/t)) #Mouse size relative to window size
win.mouse(win, rect)
