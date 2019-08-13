from datastructures import point, cell
import random
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


class map:

    def __init__(self, xsize, ysize):

        self.xsize = xsize
        self.ysize = ysize
        self.point_map = None

    def generate(self):
        self.point_map = self.build_point_map(self.xsize, self.ysize)
        self.cell_map = self.points_to_cells()

        #for p in self.point_map:
        #    plt.scatter(p[0], p[1])
        voronoi_plot_2d(self.cell_map)
        plt.show()

    def build_point_map(self, xsize, ysize):

        points = np.zeros((ysize * xsize, 2))

        count = 0

        for x in range(xsize):
            for y in range(ysize):
                p = point(x, y) + self.point_jitter(0.5)
                points[count] = np.array([p.x, p.y])
                count += 1

        return points

    def points_to_cells(self):
        return Voronoi(self.point_map)

    def point_jitter(self, magnitude):
        x = random.uniform(magnitude * -1, magnitude)
        y = random.uniform(magnitude * -1, magnitude)
        return point(x, y)
