
import sys
import noise
import numpy as np
import random
from gi.repository import Gtk
from generator import generator
import cairo
import math

size = 2048
numpoints = 1048576

#todo-seperate render size and number of points
#to-do add jitter to grid
class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

        self.generator = generator(10, 10)

    def init_ui(self):

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("GTK window")
        self.resize(1024, 1024)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_draw(self, wid, cr):

        dotxsep = self.get_size()[0] / self.generator.xsize
        dotysep = self.get_size()[1] / self.generator.ysize

        for row in self.generator.cells.cells:
            for cell in row:

                cr.set_source_rgb(cell.r, 0, 0)
                cr.arc(cell.NW.x*dotxsep, cell.NW.y*dotysep, 1, 0, 2*math.pi)
                cr.fill()
                cr.arc(cell.NE.x*dotxsep, cell.NE.y*dotysep, 1, 0, 2*math.pi)
                cr.fill()
                cr.arc(cell.SW.x*dotxsep, cell.SW.y*dotysep, 1, 0, 2*math.pi)
                cr.fill()
                cr.arc(cell.SE.x*dotxsep, cell.SE.y*dotysep, 1, 0, 2*math.pi)
                cr.fill()


def main():

    app = Example()
    Gtk.main()
    print("test")


if __name__ == "__main__":
    main()
