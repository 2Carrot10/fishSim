from objs.Obj import Obj
import random
import math
size = 4 

class Effect(Obj):
    # A water circle that expands
    # Friction is how much to multiply every second
    def __init__(self, color, x, y, speed, canvas, timeUntilFade, timeLeft, friction, xVel, yVel):
        rot = random.random() * 2 * math.pi
        self.x = x
        self.y = y
        self.velX = speed * math.cos(rot) + xVel
        self.velY = speed * math.sin(rot) + yVel
        self.friction = friction
        self.timeLeft = timeLeft
        self.timeUntilFade = timeUntilFade
        self.timeSoFar = 0

        self.toDestory = False
        self.obj = canvas.create_oval(x, y, x + size * 2, y + size * 2,
                                      fill='', outline=color, width=2)
        canvas.tag_lower(self.obj)

    def move(self, canvas, timeStep):
        self.timeSoFar += timeStep
        if self.timeSoFar > self.timeUntilFade:
            c = (self.timeSoFar - self.timeUntilFade) / (self.timeLeft - self.timeUntilFade)
            a = size * (1 - c)
            canvas.coords(self.obj,
                          self.x - a,
                          self.y - a,
                          self.x + a,
                          self.y + a)
        if self.timeSoFar > self.timeLeft:
            self.toDestroy = True
        self.velY /= (1 + timeStep) * self.friction #TODO: check
        self.velX /= (1 + timeStep) * self.friction
        self.x += self.velX * timeStep
        self.y += self.velY * timeStep
        canvas.moveto(self.obj, self.x, self.y)
