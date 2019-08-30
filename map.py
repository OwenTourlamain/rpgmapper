from datastructures import point, point3, cell
import random
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


class map:

    def __init__(self, xsize, ysize):

        self.xsize = xsize
        self.ysize = ysize
        self.points = None

    def generate(self):
        self.init_points()
        self.add_heightmap()

    def show(self):
        pass#plt.show()

    def init_points(self):

        self.points = []

        for x in range(self.xsize):
            row = []
            for y in range(self.ysize):
                p = point3(x, y, 0)
                row.append(p)
            self.points.append(row)

    def add_heightmap(self):
        self.points[0][0].height = 1
        self.points[0][self.ysize-1].height = 0.5
        self.points[self.xsize-1][self.ysize-1].height = 0.25
        self.points[self.xsize-1][0].height = 0.75

    def point_jitter(self, magnitude):
        x = random.uniform(magnitude * -1, magnitude)
        y = random.uniform(magnitude * -1, magnitude)
        return point(x, y)
