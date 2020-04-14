#CannonGameFinal.py
# Co-Op Work by Hasan M,Rob F,Will G, Davon F
#Game That You Shoot Stuff


from math import sqrt, sin, cos, radians, degrees
from arcgraphics import *
from soundfile import*
from random import randrange
import random

class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height ?? and distance (x)."""

    def __init__(self, angle, velocity, height, xpos):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = xpos
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.ymax = height

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
        if self.ypos > self.ymax:
            self.ymax = self.ypos
            return self.ymax

    def getYMax(self):
        return self.ymax
    
    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos


class Launcher:

    def __init__(self, win):
        """Create inital launcher with angle 45 degrees and velocity 40
        win is the GraphWin to draw the launcher in.
        """
        
        # draw the base shot of the launcher
        base = Circle(Point(0,0), 5)
        base.setFill("black")
        base.setOutline("black")
        base.draw(win)

        # save the window and create initial angle and velocity
        self.win = win
        self.angle = radians(45.0)
        self.vel = 55.0
        
        # create inital "dummy" arrow
        self.arrow = Line(Point(0,0), Point(0,0)).draw(win)
        # replace it with the correct arrow
        self.redraw()

        
    def redraw(self):
        """undraw the arrow and draw a new one for the
        current values of angle and velocity.
        """
        
        self.arrow.undraw()
        pt2 = Point(10*cos(self.angle), 10*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(self.win)
        self.arrow.setWidth(20)

        
    def adjAngle(self, amt):
        """ change angle by amt degrees """
        
        self.angle = self.angle+radians(amt)
        self.redraw()


    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)
  

class ShotTracker:

    """ Graphical depiction of a projectile flight using a Circle """

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot, angle, velocity, and
        height are initial projectile parameters.
        """
        
        self.proj = Projectile(angle, velocity, height, 0)
        self.marker = Circle(Point(0,height), 2)
        self.marker.setFill(color_rgb( randrange(0,256), randrange(0,256), randrange(0,256)))
        self.marker.setOutline("red")
        self.marker.draw(win)

        
    def update(self, dt):
        """ Move the shot dt seconds farther along its flight """
        
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

    def getRadius(self):
        """ returns the radius of this ShotTracker """
        return 3
    
    def getX(self):
        """ return the current x coordinate of the shot's center """
        return self.proj.getX()

    def getY(self):
        """ return the current y coordinate of the shot's center """
        return self.proj.getY()

    def undraw(self):
        """ undraw the shot """
        self.marker.undraw()

class smithereen:

    def __init__(self, win, center):

        self.radius = .1 + random.random()
        self.timeToLive = random.randrange(0, 5)
        self.height = center.getY()
        self.starx = center.getX()
        self.velocity = random.randrange(0, 30)
        self.angle = random.randrange(0, 360)
        self.proj = Projectile(self.angle, self.velocity,self.height, self.starx)
        self.marker = Circle(Point(0, self.height), self.radius).draw(win)
        self.marker.setFill(color_rgb( randrange(0,256), randrange(0,256), randrange(0,256)))
        self.marker.setOutline(color_rgb( randrange(0,256), randrange(0,256), randrange(0,256)))

    def update(self, dt):
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

        timeToLive = self.timeToLive - dt
        if timeToLive > 0:
            return True
        else:
            return False

    def undraw(self):
        self.update(.1)
        self.marker.undraw()

class Target:
    def __init__(self, win, center, radius):
        self.center = center
        self.radius = radius
        self.target = Circle(center, radius)
        self.target.setFill(color_rgb( randrange(0,256), randrange(0,256), randrange(0,256)))
        self.target.draw(win)
        self.targetList = []
        self.dx = random.randrange(-10, 10)
        self.dy = random.randrange(-10, 10)

    def update(self, dt):
        self.target.move(self.dx * dt, self.dy * dt)

        if (self.target.getCenter().getX()
            - self.target.getRadius() < -99) and (self.dx < 0):
            self.dx = -self.dx

        if (self.target.getCenter().getX()
            - self.target.getRadius() > 99) and (self.dx > 0):
            self.dx = -self.dx

        if (self.target.getCenter().getY()
            - self.target.getRadius() < 0) and (self.dy < 10):
            self.dy = -self.dy

        if (self.target.getCenter().getY()
            - self.target.getRadius() > 140) and (self.dy > 0):
            self.dy = -self.dy

    def hit(self, shot):
        """Returns True if Target Hit"""
       
        center = self.target.getCenter()
        distance = sqrt((center.getX() - shot.getX())**2 + (center.getY() - shot.getY())**2)
        
        if distance <= shot.getRadius() + self.radius:
            return True
        

    def __distance(self, p, s):
        return sqrt(((p.getX() - s.getX())**2) + (p.getY() - s.getY())**2)

    def destroy(self):
        self.target.undraw()

class cannonGame:

    def __init__(self):
        self.win = GraphWin("Projectile Animation", 1024, 768,autoflush=False)
        self.win.setCoords(-100, -10, 100, 140)
        self.launcher = Launcher(self.win)

        self.count = randrange(20,101)
        self.fired = 0
        self.shots = []
        self.targets = []
        self.smithereenList = []
        countText1 = Text(Point(50,135),"Reinforcements: ").draw(self.win)
        shotText1 = Text(Point(-5,135),"Shots Fired: ").draw(self.win)
        hitcount1 = Text(Point(-70,135),"Targets Hit: ").draw(self.win)
        self.hitText = Text(Point(-55,135),"0").draw(self.win)
        
        self.countText = Text(Point(65,135),self.count).draw(self.win)
        self.shotText = Text(Point(10,135),"0").draw(self.win)
        self.hitcount = 0

        
    def UpdateSmithereens(self, dt):

        alive = list(self.smithereenList)
        for s in self.smithereenList:
            if not s.update(dt):
                s.undraw()
                alive.remove(s)
        smithereenList = alive

    def GenerateTargets(self):
        
        for target in range(10):
            target = Target(self.win, Point(randrange(-0,90), randrange(10,139)), randrange(3,9))                                                                
            self.targets.append(target)
        return self.targets

    def handleCollisions(self):
       

        live = []
        
        for i in self.targets:
            hit = None 
            for s in self.shots:
                if i.hit(s):
                    hit = s
                    break
                  
            if hit is not None:
                self.shots.remove(hit)
                hit.undraw()
                i.destroy()
                self.count = self.count - 1
                self.hitcount = self.hitcount + 1
                self.hitText.setText(" ")
                self.hitText.setText(self.hitcount)        
                self.win.setBackground(color_rgb( randrange(0,256), randrange(0,256), randrange(0,256)))
                
                if self.count > 0:
                    self.countText.setText(" ")
                    self.countText.setText(self.count)
                    
                    for target in range(1):
                        target = Target(self.win, Point(randrange(-0,90), randrange(10,139)), randrange(3,9))
                        self.targets.append(target)
                elif self.count == 0:
                    self.countText.setText("0")
                    
                for j in range(i.target.getRadius()*5):
                    sm = smithereen(self.win, i.target.getCenter())
                    self.smithereenList.append(sm)
            else:
                live.append(i)
            self.targets = live

    def updateTargets(self, dt):
        
        for i in self.targets:
            i.update(dt)

    def updateShots(self, dt):
        
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and shot.getX() < 210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive

    def run(self):
        j = Joystick()
        j.set_button('SQUARE', 'a')
        j.set_button('X', 'b')
        j.set_button('CIRCLE', 'c')
        j.set_button('TRIANGLE', 'd')
        self.GenerateTargets()
        sound = playSound("jazz.wav", "explosion.wav")
        sound.rewind(0)
        while self.win.isClosed() == False:
            self.updateShots(1/30)
            self.updateTargets(1/5)
            self.handleCollisions()
            self.UpdateSmithereens(1/30)
            key = self.win.checkKey()
            if key in ["d"]:
                sound.fade(1080)
                break
            if key == "a": self.launcher.adjAngle(5)
            elif key == "c": self.launcher.adjAngle(-5)
            elif key == "b":
                sound.play(1)
                self.fired = self.fired + 1
                self.shots.append(self.launcher.fire())
                self.shotText.setText(self.fired)
            update(30)
        self.win.close()

if __name__ == "__main__":
    cannonGame().run()


