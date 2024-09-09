from objs import Boid
from objs import Food
from PIL import Image, ImageTk
import tkinter as tk
import math
import random
from objs import Pred
timeToSwitch = .15
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

class Fish(Boid.Boid):
    cycle = 0
    timeCount = timeToSwitch * random.random()
    def chooseMove(self, canvas, others, timeStep):
        ave = list((0, 0))
        distFromEdgeToBeBad = 150
        ave[1] += max(distFromEdgeToBeBad - self.y, 0) * 100
        ave[1] -= max(distFromEdgeToBeBad - (canvas.winfo_height() - self.y), 0) * 100

        ave[0] += max(distFromEdgeToBeBad - self.x, 0) * 20
        ave[0] -= max(distFromEdgeToBeBad - (canvas.winfo_width() - self.x), 0) * 100
        fishInArea = 0
        fishLocation = list((0, 0))
        closestFood = list((0, 0))
        for val in others:
            if not self == val:
                intDif = list((val.x - self.x, val.y - self.y))
                dist = math.sqrt(intDif[0]**2 + intDif[1]**2)
                dif = list((0, 0))
                dif[0] = intDif[0]/math.hypot(intDif[0], intDif[1])
                dif[1] = intDif[1]/math.hypot(intDif[0], intDif[1])

                if isinstance(val, Food.Food):
                    if dist > 600:
                        continue
                    if dist < 40:
                        self.speed += 20
                        val.toDestroy = True
                        val.toExplode = True
                    closestFood[0] = dif[0]
                    closestFood[1] = dif[1]
                elif isinstance(val, Pred.Pred):
                    if dist > 1000:
                        continue
                    mult = 1
                    ave[0] -= dif[0] * mult
                    ave[1] -= dif[1] * mult
                elif isinstance(val, Fish):
                    if dist > 300:
                        continue
                    fishInArea += 1
                    fishLocation[0] += val.x
                    fishLocation[1] += val.y
                    ave[0] += math.cos(val.rot) / 100
                    ave[1] += math.sin(val.rot) / 100
                    mult = (dist - 130) / 16620
                    if mult < 0:
                        mult *= 30
                    ave[0] += dif[0] * mult
                    ave[1] += dif[1] * mult
            if fishInArea > 5:
                pass

        ave[0] += closestFood[0]
        ave[1] += closestFood[1]
        return ave

    def __init__(self, x, y, rot, canvas, window):
        self.size = 25
        self.width = 10
        self.rotSpeed = 1 * random.random() + 1
        self.speed = 200 * random.random() + 100
        color = "white"
        Boid.Boid.__init__(self, x, y, rot, color, canvas)

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
