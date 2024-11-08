import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
#from link import frames, l1, l2, l3, l4
import numpy
from itertools import cycle

class Animation:
        def __init__(self, muf, l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, frames):

                self.l1x = l1x
                self.l1y = l1y

                self.l2x = l2x
                self.l2y = l2y

                self.l3x = l3x
                self.l3y = l3y

                self.l4x = l4x
                self.l4y = l4y

                self.mufs = cycle(muf)

                xmin = 9999
                ymin = 9999

                xmax = -9999
                ymax = -9999

                xmin = min(min(l1x), min(l2x), min(l3x), min(l4x))
                ymin = min(min(l1y), min(l2y), min(l3y), min(l4y))

                xmax = max(max(l1x), max(l2x), max(l3x), max(l4x))
                ymax = max(max(l1y), max(l2y), max(l3y), max(l4y))

                self.fig, axes = plt.subplots()
                #self.fig.suptitle(code)
                axes.set_aspect('equal', adjustable='box')
                axes.set(xlim=[xmin - 50, xmax + 50], ylim=[ymin - 50, ymax + 50])
                self.fig.subplots_adjust(bottom=0.2)

                self.toggle = []
                self.paused = False

                self.line1, = axes.plot([], [], '-ko')
                self.line2, = axes.plot([], [], '-ro')
                self.line3, = axes.plot([], [], '-bo')
                self.line4, = axes.plot([], [], '-go')

                self.coupler, = axes.plot([], [], '--')

                axpause = self.fig.add_axes([0.4, 0.05, 0.2, 0.075])
                self.bpause = Button(axpause, 'Play/Pause')
                self.bpause.on_clicked(self.toggle_pause)

                axgoto = self.fig.add_axes([0.6, 0.05, 0.2, 0.075])
                self.bgoto = Button(axgoto, 'Go to')
                self.bgoto.on_clicked(self.gotoframe)

                self.cur_frame = None
                self.ani = FuncAnimation(self.fig, self.update, frames=frames, interval=0, blit=True, repeat=True)


        def minn(self, l, xmin, ymin):
                for x in l.x:
                        xmin = min(xmin, x)
                
                for y in l.y:
                	ymin = min(ymin, y)

                return xmin, ymin


        def maxx(self, l, xmax, ymax):
                for x in l.x:
                        xmax = max(xmax, x)
	
                for y in l.y:
                        ymax = max(ymax, y)

                return xmax, ymax


        def toggle_pause(self, event):
                if self.paused:
                        self.ani.resume()
                else:
                        self.ani.pause()
                self.paused = not self.paused


        def update(self, frame):

                self.cur_frame = frame

                l1xf = self.l1x[frame]
                l2xf = self.l2x[frame]
                l3xf = self.l3x[frame]
                l4xf = self.l4x[frame]

                l1yf = self.l1y[frame]
                l2yf = self.l2y[frame]
                l3yf = self.l3y[frame]
                l4yf = self.l4y[frame]

                vax = numpy.array(self.l2x)
                vbx = numpy.array(self.l3x)
                xcc = 0.5 * (vax + vbx)

                vay = numpy.array(self.l2y)
                vby = numpy.array(self.l3y)
                ycc = 0.5 * (vay + vby)

                ccx = xcc[:frame]
                ccy = ycc[:frame]

                self.line1.set_data([l4xf, l1xf], [l4yf, l1yf])
                self.line2.set_data([l1xf, l2xf], [l1yf, l2yf])
                self.line3.set_data([l2xf, l3xf], [l2yf, l3yf])
                self.line4.set_data([l3xf, l4xf], [l3yf, l4yf])

                self.coupler.set_data([ccx, ccy])

                return self.line1, self.line2, self.line3, self.line4, self.coupler


        def gotoframe(self, event):
                self.update(next(self.mufs))                
                self.fig.canvas.draw()





