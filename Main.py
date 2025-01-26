import tkinter as tk
import random
from objs import Food, Fish, EvilFish, Effect
import math
window = tk.Tk()
amountOfFishGood = 40
amountOfFoodGood = 4
amountOfBadThingsGood = 1
timeStep = 30
timeLastInteract = 0
timeUntilAuto = 10

# fish = ImageTk.PhotoImage(
#     Image.open(
#         "assets/fishForward.png").convert("RGBA").resize(
#         (128, 128),
#         Image.Resampling.NEAREST
#     )
# )
# Food.Food(x, y, 0, canvas)
stuff = []
effects = []

canvas = tk.Canvas(window, bg="black")

def dropFood(event):
    stuff.append(Food.Food(event.x, event.y, 0, canvas))
    timeLastInteract = 0


def spawnFish(event):
    timeLastinteract = 0
    stuff.append(EvilFish.EvilFish(event.x, event.y, random.random() * math.pi * 2, canvas, window))


# canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", dropFood)
canvas.bind("<Button-3>", spawnFish)
"""ball = canvas.create_oval(
    10, 10, 70, 70,
    fill='black'
)
canvas.move(ball, 20, 1)
"""
canvas.pack(fill="both", expand=True)


def frame(Ca):
    global timeLastInteract
    timeLastInteract += timeStep / 1000
    distFromEdge = 400
    fishes = 0
    preds = 0
    foods = 0
    for val in effects:
        val.move(canvas, timeStep / 1000)
        if val.toDestroy:
            effects.remove(val)
            canvas.delete(val.obj)

    for val in stuff:
        val.step(canvas, stuff, timeStep / 1000)  # timeStep is in seconds
        if isinstance(val, Fish.Fish):
            fishes += 1
        if isinstance(val, EvilFish.EvilFish):
            preds += 1
        if isinstance(val, Food.Food):
            foods += 1
    if fishes < amountOfFishGood:
        xPos = -distFromEdge
        yPos = -distFromEdge
        if random.random() * 2 > 1:
            if random.random() * 2 > 1:
                xPos = canvas.winfo_width() + distFromEdge
            yPos = random.random() * canvas.winfo_height()
        else:
            if random.random() * 2 > 1:
                yPos = canvas.winfo_height() + distFromEdge
            xPos = random.random() * canvas.winfo_width()

        stuff.append(Fish.Fish(xPos, yPos, 0, canvas, window))
    if timeLastInteract > timeUntilAuto:
        if foods < amountOfFoodGood:
            yPos = 300 + random.random() * (canvas.winfo_height() - 300 * 2)
            xPos = 300 + random.random() * (canvas.winfo_width() - 300 * 2)
            valid = True
            for val in stuff:
                if math.hypot(val.x - xPos, val.y - yPos) < 200:
                    valid = False
                    break
            if valid:
                stuff.append(Food.Food(xPos, yPos, 0, canvas))

        if preds < amountOfBadThingsGood:
            xPos = -distFromEdge
            yPos = -distFromEdge
            if random.random() * 2 > 1:
                if random.random() * 2 > 1:
                    xPos = canvas.winfo_width() + distFromEdge
                yPos = random.random() * canvas.winfo_height()
            else:
                if random.random() * 2 > 1:
                    yPos = canvas.winfo_height() + distFromEdge
                xPos = random.random() * canvas.winfo_width()

            stuff.append(EvilFish.EvilFish(xPos, yPos, 0, canvas, window))
    for val in stuff:
        if val.toDestroy:
            stuff.remove(val)
            for toDel in val.obj:
                canvas.delete(toDel)
            if val.toExplode:
                for x in range(6):
                    effects.append(Effect.Effect(val.color, val.x, val.y, random.random() * 100, canvas, 1, 2, 1.02, math.cos(val.rot)*val.speed, math.sin(val.rot) * val.speed))


def animation(Ca):
    frame(Ca)
    window.after(timeStep, animation, Ca)


animation(canvas)
window.mainloop()
