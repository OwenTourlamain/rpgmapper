
import sys
import noise
import numpy as np
import random
from gi.repository import Gtk
from map import map
import cairo
import math
import time

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
        self.resize(500, 500)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_draw(self, wid, cr):

        #dotxsep = self.get_size()[0] / self.map.xsize
        #dotysep = self.get_size()[1] / self.map.ysize
        dotxsep = 4
        dotysep = 4

        #for cell in self.map.cell_map:
        #    cell.draw(cr, dotxsep, dotysep)

        toggle = True

        #self.draw_bounding_box(cr, self.map.xsize, self.map.ysize, dotxsep, dotysep)

        for row in self.map.points:
            for p in row:
                cr.arc(
                    (p.x*dotxsep) + (dotxsep / 2),
                    (p.y*dotysep) + (dotysep / 2),
                    2, 0, 2*math.pi)
                #print(p.height)
                cr.set_source_rgb(p.height, p.height, p.height)
                cr.fill()

            #if toggle:

            # cr.move_to(abs(x[1])*dotxsep + (dotxsep / 2), abs(x[0])*dotysep + (dotysep / 2))
            # cr.line_to(abs(y[1])*dotxsep + (dotxsep / 2), abs(y[0])*dotysep + (dotysep / 2))
            # cr.stroke()
            #print("move: ", int(x[0])*dotxsep, end=', ')
            #print(int(x[1])*dotysep)
            toggle = False
            # else:
            #     cr.line_to(abs(x[0])*dotxsep + (dotxsep / 2), abs(x[1])*dotysep + (dotysep / 2))
            #     cr.stroke()
            #     print("line: ", int(x[0])*dotxsep, end=', ')
            #     print(int(x[1])*dotysep)
            #     toggle = True


        return

        for row in self.map.point_map:
            for p in row:
                cr.arc(
                    (p.x*dotxsep)+(dotxsep / 2),
                    (p.y*dotysep) + (dotysep / 2),
                    2, 0, 2*math.pi)
                cr.set_source_rgb(0, 0, 0)
                cr.fill()

        self.map.show()

    def draw_bounding_box(self, cr, ysize, xsize, dotysep, dotxsep):

        cr.set_source_rgb(0, 0, 0)

        cr.set_line_width(1)

        cr.move_to(0 + (dotysep / 2), 0 + (dotxsep / 2))
        cr.line_to(0 + (dotysep / 2), (xsize*dotxsep) - (dotxsep / 2))
        cr.line_to((ysize*dotysep) - (dotysep / 2), (xsize*dotxsep) - (dotxsep / 2))
        cr.line_to((ysize*dotysep) - (dotysep / 2), 0 + (dotxsep / 2))
        cr.line_to(0 + (dotysep / 2), 0 + (dotxsep / 2))
        cr.stroke()


def main():

    app = Example()
    Gtk.main()


if __name__ == "__main__":
    main()
