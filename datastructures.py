import random


class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)


class cell:

    def __init__(self, NW, NE, SW, SE, index):

        self.NW = NW
        self.NE = NE
        self.SW = SW
        self.SE = SE
        self.index = index
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

        self.center = point(
            ((self.NW.x + self.NE.x + self.SW.x + self.SE.x) / 4.0),
            ((self.NW.y + self.NE.y + self.SW.y + self.SE.y) / 4.0))

    def __str__(self):
        return str(self.center)


class cell_array:

    N = point(0, -1)
    E = point(1, 0)
    S = point(0, 1)
    W = point(-1, 0)

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        jitter_mag = 0.4

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
