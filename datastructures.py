class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class cell:

    def __init__(self, NW, NE, SW, SE, index):

        self.NW = NW
        self.NE = NE
        self.SW = SW
        self.SE = SE
        self.index = index

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

        self.cells = [[0 for y in range(self.ysize)] for x in range(self.xsize)]

        for x in range(self.xsize):
            for y in range(self.ysize):
                NW = point(x, y)
                NE = point(x+1, y)
                SW = point(x, y+1)
                SE = point(x+1, y+1)
                self.cells[x][y] = cell(NW, NE, SW, SE, (x, y))

    def __str__(self):
        result = ""
        for y in range(self.ysize):
            for x in range(self.xsize):
                result += str(self.cells[x][y])
            result += '\n'
        return result
