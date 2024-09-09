from objs import Obj
# import tkinter as tk
sizeEnd = 15
startSize = 0
growPerSecond = 50

class Food(Obj.Obj):
    def __init__(self, x, y, rot, canvas):
        self.speed = 0
        ball = canvas.create_oval(0, 0, 0, 0,
                                  fill='', outline='yellow', width=4)

        Obj.Obj.__init__(self, x, y, rot, canvas, [ball], 'yellow')
        #canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="red")
    def render(self, canvas, timeStep):
        pass

    def otherThingToDo(self, canvas, timeStep):
        self.sizeX += growPerSecond * timeStep
        if self.sizeX > sizeEnd:
            self.sizeX = sizeEnd
        self.sizeY = self.sizeX
        canvas.coords(self.obj[0],
                      self.x - self.sizeX,
                      self.y - self.sizeY,
                      self.x + self.sizeX,
                      self.y + self.sizeY)
