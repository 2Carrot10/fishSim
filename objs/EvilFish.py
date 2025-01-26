from objs import Boid
from objs import Fish 
import tkinter as tk
import math
import random
timeToSwitch = .15
timeUntilGoAway = 10
timeUntilDie = timeUntilGoAway + 20
#root = tk.Tk()
"""
fish = ImageTk.PhotoImage(
    Image.open(
        "assets/fishForward.png").convert("RGBA").resize(
        (128, 128),
        Image.Resampling.NEAREST
    )
)
"""

class EvilFish(Boid.Boid):
    timeCount = timeToSwitch * random.random()
    def chooseMove(self, canvas, others, timeStep):
        ave = list((0, 0))
        distInFrontCheck = 100
        posInFront = list((self.x + math.cos(self.rot) * distInFrontCheck, self.y + math.sin(self.rot) * distInFrontCheck))
        # ave[0] -= min((self.x - canvas.winfo_width() - 100) / 100, 0)
        # ave[0] -= min((100 - self.x) / 100, 0)
        distFromEdgeToBeBad = 150
        ave[1] += max(distFromEdgeToBeBad - self.y, 0) * 100
        ave[1] -= max(distFromEdgeToBeBad - (canvas.winfo_height() - self.y), 0) * 100

        ave[0] += max(distFromEdgeToBeBad - self.x, 0) * 20
        ave[0] -= max(distFromEdgeToBeBad - (canvas.winfo_width() - self.x), 0) * 100
        fishInArea = 0
        fishLocation = list((0, 0))
        for val in others:
            if not self == val:
                intDif = list((val.x - self.x, val.y - self.y))
                dist = math.sqrt(intDif[0]**2 + intDif[1]**2)
                intDifFront = (val.x - posInFront[0], val.y - posInFront[1])
                distFront = math.sqrt(intDifFront[0]**2 + intDifFront[1]**2)
                if dist < 5:
                    continue
                dif = list((0, 0))
                dif[0] = intDif[0]/math.hypot(intDif[0], intDif[1])
                dif[1] = intDif[1]/math.hypot(intDif[0], intDif[1])

                if isinstance(val, Fish.Fish):
                    if distFront > 600:
                        continue
                    if dist < 40:
                        val.toDestroy = True
                        val.toExplode = True
                    mult = 3
                    if distFront < 200:
                        mult = 1.4
                    if distFront < 25:
                        mult = 3
                    ave[0] += dif[0] * mult
                    ave[1] += dif[1] * mult
            if fishInArea > 5:
                pass
        if self.goAway:
            return (-(canvas.winfo_width()/2 - self.x),(canvas.winfo_height()/2 - self.y))
        return ave

    def __init__(self, x, y, rot, canvas, window):
        self.timer = 0
        self.goAway = False
        self.size = 45
        self.width = 20
        self.rotSpeed = 1 * random.random() + .5
        self.speed = 400 + random.random() * 100
        Boid.Boid.__init__(self, x, y, rot, "red", canvas)

    def render(self, canvas, timeStep):
        canvas.moveto(self.obj, self.x - self.size / 2, self.y - self.size / 2)
        p1 = (
            self.x + self.width * math.sin(self.rot),
            self.y - self.width * math.cos(self.rot)
        )
        p2 = (
            self.x - self.width * math.sin(self.rot),
            self.y + self.width * math.cos(self.rot)
        )
        p3 = (
            self.x + self.size * math.cos(self.rot),
            self.y + self.size * math.sin(self.rot)
        )
        canvas.coords(self.obj[0], (p1[0],p1[1],p2[0],p2[1]))
        canvas.coords(self.obj[1], (p2[0],p2[1],p3[0],p3[1]))
        canvas.coords(self.obj[2], (p1[0],p1[1],p3[0],p3[1]))
    """
        self.timeCount += timeStep
        if self.timeCount >= timeToSwitch:
            self.timeCount = 0
            self.cycle = (self.cycle + 1) % 4
            if self.cycle == 0:
                n = self.fish
            elif self.cycle == 1:
                n = self.fishRight
            elif self.cycle == 2:
                n = self.fish
            else:
                n = self.fishLeft
            canvas.itemconfig(self.obj, image=n)
        self.move(canvas, stuff, timeStep)
        self.render(canvas, timeStep)
"""
    def otherThingToDo(self, canvas, timeStep):
        self.timer += timeStep
        if self.timer > timeUntilGoAway:
            self.goAway = True
        if self.timer > timeUntilDie:
            self.toDestroy = True
