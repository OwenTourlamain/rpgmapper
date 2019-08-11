
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

        self.generator = generator(100, 100)

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
        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(0.5)

        for row in self.generator.cells.cells:
            for cell in row:
                print(cell.center.x, end=',')
                print(cell.center.y)

                cr.arc(cell.center.x*10, cell.center.y*10, 0.5, 0, 2*math.pi)
                cr.set_line_width(0.04)
                cr.fill()


def main():

    app = Example()
    Gtk.main()
    print("test")


if __name__ == "__main__":
    main()
