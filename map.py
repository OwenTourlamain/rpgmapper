from datastructures import point, cell
import random


class map:

    def __init__(self, xsize, ysize):

        self.xsize = xsize
        self.ysize = ysize
        self.point_map = None

    def generate(self):
        self.point_map = self.build_point_map(self.xsize, self.ysize)
        self.cell_map = self.points_to_cells(self.xsize, self.ysize)

    def build_point_map(self, xsize, ysize):

        points = [[0 for y in range(ysize)] for x in range(xsize)]

        for x in range(xsize):
            for y in range(ysize):
                points[x][y] = point(x, y) + self.point_jitter(0.3)

        return points

    def points_to_cells(self, xsize, ysize):
        cells = []

        for x in range(xsize):
            for y in range(ysize):
                if x == xsize - 1 or y == ysize - 1:
                    continue
                NW = self.point_map[x][y]
                NE = self.point_map[x + 1][y]
                SW = self.point_map[x][y + 1]
                SE = self.point_map[x + 1][y + 1]
                cells.append(cell(NW, NE, SW, SE))

        return cells

    def point_jitter(self, magnitude):
        x = random.uniform(magnitude * -1, magnitude)
        y = random.uniform(magnitude * -1, magnitude)
        return point(x, y)
