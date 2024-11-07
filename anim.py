import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
from link import links, frames, l1, l2, l3, l4
import numpy
from itertools import cycle

class Animation:
        def __init__(self, muf):

                self.mufs = cycle(muf)

                xmin = 9999
                ymin = 9999

                xmax = -9999
                ymax = -9999

                xmin, ymin = self.minn(links[1], xmin, ymin)
                xmin, ymin = self.minn(links[2], xmin, ymin)
                xmin, ymin = self.minn(links[3], xmin, ymin)

                xmax, ymax = self.maxx(links[1], xmax, ymax)
                xmax, ymax = self.maxx(links[2], xmax, ymax)
                xmax, ymax = self.maxx(links[3], xmax, ymax)		

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

                l1x = l1.x[frame]
                l2x = l2.x[frame]
                l3x = l3.x[frame]
                l4x = l4.x[frame]

                l1y = l1.y[frame]
                l2y = l2.y[frame]
                l3y = l3.y[frame]
                l4y = l4.y[frame]

                vax = numpy.array(l2.x)
                vbx = numpy.array(l3.x)
                xcc = 0.5 * (vax + vbx)

                vay = numpy.array(l2.y)
                vby = numpy.array(l3.y)
                ycc = 0.5 * (vay + vby)

                ccx = xcc[:frame]
                ccy = ycc[:frame]

                self.line1.set_data([l4x, l1x], [l4y, l1y])
                self.line2.set_data([l1x, l2x], [l1y, l2y])
                self.line3.set_data([l2x, l3x], [l2y, l3y])
                self.line4.set_data([l3x, l4x], [l3y, l4y])

                self.coupler.set_data([ccx, ccy])

                return self.line1, self.line2, self.line3, self.line4, self.coupler


        def gotoframe(self, event):
                self.update(next(self.mufs))                
                self.fig.canvas.draw()





