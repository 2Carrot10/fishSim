from objs import Obj
import math
import random


class Boid(Obj.Obj):

    def chooseMove(self, canvas, others, timeStep):
        pass

    def move(self, canvas, others, timeStep):
        rotAllowed = self.rotSpeed * timeStep
        dir = self.chooseMove(canvas, others, timeStep)
        if math.hypot(dir[1], dir[0]) > .01:
            idealRot = math.atan2(dir[1], dir[0])
            delta_rot = (((idealRot - self.rot) + math.pi) % (math.pi * 2)) - math.pi
            clamped_delta_rot = max(min(
                delta_rot, rotAllowed), -rotAllowed)
            self.rot += clamped_delta_rot

        self.x += math.cos(self.rot) * self.speed * timeStep
        self.y += math.sin(self.rot) * self.speed * timeStep
        #canvas.moveto(self.obj, self.x, self.y)

    def __init__(self, x, y, rot, color, canvas):
        width = 5
        ball = canvas.create_line(
            x - self.size/2, y - self.size/2, x + self.size, y + self.size, fill=color, width=width
        )

        ball2 = canvas.create_line(
            x - self.size/2, y - self.size/2, x + self.size, y + self.size, fill=color, width=width
        )
        ball3 = canvas.create_line(
            x - self.size/2, y - self.size/2, x + self.size, y + self.size, fill=color, width=width
        )
        # fish = canvas.create_image(32, 32, image=image)
        # ob = canvas.create_image(32, 32, image=image)
        Obj.Obj.__init__(self, x, y, rot, canvas, (ball, ball2, ball3), color)
