import random
import math


class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)


class cell:

    def __init__(self, NW, NE, SW, SE):

        self.NW = NW
        self.NE = NE
        self.SW = SW
        self.SE = SE
        #self.index = index
        self.r = random.uniform(0.0, 1.0)
        self.g = random.uniform(0.0, 1.0)
        self.b = random.uniform(0.0, 1.0)

        self.center = point(
            ((self.NW.x + self.NE.x + self.SW.x + self.SE.x) / 4.0),
            ((self.NW.y + self.NE.y + self.SW.y + self.SE.y) / 4.0))

    def __str__(self):
        return str(self.center)

    def draw(self, cr, dotxsep, dotysep):

        if self.r > 0.5:
            cr.set_source_rgb(0, 1, 0)
        else:
            cr.set_source_rgb(0, 0, 1)
        cr.move_to(self.NW.x*dotxsep, self.NW.y*dotysep)
        cr.line_to(self.NE.x*dotxsep, self.NE.y*dotysep)
        cr.line_to(self.SE.x*dotxsep, self.SE.y*dotysep)
        cr.line_to(self.SW.x*dotxsep, self.SW.y*dotysep)
        cr.fill()

        #cr.arc(self.center.x*dotxsep, self.center.y*dotysep, 1, 0, 2*math.pi)
        #cr.set_source_rgb(0, 0, 0)
        #cr.fill()


class cell_array:

    N = point(0, -1)
    E = point(1, 0)
    S = point(0, 1)
    W = point(-1, 0)

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        jitter_mag = 0.0

        self.cells = [[0 for y in range(self.ysize)] for x in range(self.xsize)]

        for x in range(self.xsize):
            for y in range(self.ysize):
                NW = point(x, y) + self.point_jitter(jitter_mag)
                NE = point(x+1, y) + self.point_jitter(jitter_mag)
                SW = point(x, y+1) + self.point_jitter(jitter_mag)
                SE = point(x+1, y+1) + self.point_jitter(jitter_mag)
                self.cells[x][y] = cell(NW, NE, SW, SE, (x, y))

    def __str__(self):
        result = ""
        for y in range(self.ysize):
            for x in range(self.xsize):
                result += str(self.cells[x][y])
            result += '\n'
        return result

    def point_jitter(self, magnitude):
        x = random.uniform(magnitude * -1, magnitude)
        y = random.uniform(magnitude * -1, magnitude)
        return point(x, y)
