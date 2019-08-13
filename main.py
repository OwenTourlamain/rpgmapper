
import sys
import noise
import numpy as np
import random
from gi.repository import Gtk
from map import map
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

        self.map = map(100, 100)
        self.map.generate()

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

        dotxsep = self.get_size()[0] / self.map.xsize
        dotysep = self.get_size()[1] / self.map.ysize

        for cell in self.map.cell_map:
            cell.draw(cr, dotxsep, dotysep)

        return

        for row in self.map.point_map:
            for p in row:
                cr.arc(
                    (p.x*dotxsep)+(dotxsep / 2),
                    (p.y*dotysep) + (dotysep / 2),
                    2, 0, 2*math.pi)
                cr.set_source_rgb(0, 0, 0)
                cr.fill()


def main():

    app = Example()
    Gtk.main()


if __name__ == "__main__":
    main()
