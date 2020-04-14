from arcgraphics import*
from soundfile import*

sound = playSound("jazz.wav", "explosion.wav")
sound.play(0)

x, y = 400, 300
win = GraphWin("Window", x, y)

mimg = Polygon(Point(-2,0), Point(3, 4), Point(3, 2),\
                   Point(8, 2), Point(8, -2), Point(3, -2), Point(3, -4)
               )
mimg.move(x/2, y/2)
mimg.setFill('black')
mimg.setOutline('black')

img = 'cursor.png'
curso = Image(Point(x/2, y/2), img)

try:
    win.mouse(win, cursor)
except:
    win.mouse(win, mimg)

