class Obj:
    x = 0
    y = 0
    rot = 0
    obj = None
    size = 30
    toDestroy = False
    toExplode = False

    def __init__(self, x, y, rot, canvas, obj, color):
        self.color = color
        self.sizeX = 0
        self.sizeY = 0
        self.x = x
        self.y = y
        self.rot = rot
        self.obj = obj
        self.render(canvas, 0)

    def move(self, canvas, stuff, timeStep):
        pass

    def render(self, canvas, timeStep):
        canvas.moveto(self.obj, self.x - self.sizeX, self.y - self.sizeY)

    def otherThingToDo(self, canvas, timeStep):
        pass

    def step(self, canvas, stuff, timeStep):
        self.otherThingToDo(canvas, timeStep)
        self.move(canvas, stuff, timeStep)
        self.render(canvas, timeStep)
