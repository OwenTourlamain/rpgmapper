from datastructures import point, cell, cell_array

class generator:

    def __init__(self, xsize, ysize):

        self.xsize = xsize
        self.ysize = ysize
        self.cells = cell_array(self.xsize, self.ysize)
