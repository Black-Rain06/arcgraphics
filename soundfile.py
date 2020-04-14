
try:
    from pygame import mixer
    mixer.init()
except:
    raise "Pygame mixer not initiated"


class playSound():

    def __init__(self, *argv):
        self.filename = argv

    def play(self, num):
        return mixer.Sound(self.filename[num]).play()

    def rewind(self, num):
        return mixer.Sound(self.filename[num]).play(-1)

    def pause(self):
        return mixer.pause()

    def stop(self):
        return mixer.stop()

    def fade(self, num):
        return mixer.fadeout(num)

from arcgraphics import*
def main():

    win = GraphWin("", 200, 200)

    wav = playSound("jazz.wav", "explosion.wav")
    wav.play(0)

    while win.isClosed() == False:
        key = win.checkKey()
        if key == 'SQUARE':
            wav.play(1)
        elif key == 'X': wav.rewind(1)
        elif key == 'TRIANGLE': wav.pause()
        elif key == 'CIRCLE': wav.stop()
        elif key == 'L1': wav.fade(1000)
        elif key == 'R1': wav.play(0)
    print('closed')


main()






