import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import numpy as np
from itertools import cycle


class Animation:
        def __init__(self, toggles, l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, l5x, l5y, frames):

                self.l1x = l1x
                self.l1y = l1y

                self.l2x = l2x
                self.l2y = l2y

                self.l3x = l3x
                self.l3y = l3y

                self.l4x = l4x
                self.l4y = l4y

                self.l5x = l5x
                self.l5y = l5y

                self.toggles_empty = True
                if len(toggles) != 0:
                    self.toggles_empty = False
                    self.toggles = cycle(toggles)

                # Find minimum and maximum x and y

                xmin = 9999
                ymin = 9999

                xmax = -9999
                ymax = -9999

                xmin = min(min(l1x), min(l2x), min(l3x), min(l4x), min(l5x))
                ymin = min(min(l1y), min(l2y), min(l3y), min(l4y), min(l5y))

                xmax = max(max(l1x), max(l2x), max(l3x), max(l4x), max(l5x))
                ymax = max(max(l1y), max(l2y), max(l3y), max(l4y), max(l5y))

                # create figure with axes
                self.fig, axes = plt.subplots()
                # set min and max of axes
                axes.set(xlim=[xmin - 0.1, xmax + 0.1], ylim=[ymin - 0.1, ymax + 0.1])
                # set 1:1 aspect ratio
                axes.set_aspect('equal', adjustable='box')
                # add margin at the bottom for buttons
                self.fig.subplots_adjust(bottom=0.2)

                self.toggle = []
                self.paused = False

                # initialize link lines
                self.line1, = axes.plot([], [], '-ko')
                self.line2, = axes.plot([], [], '-ro')
                self.line3, = axes.plot([], [], '-bo')
                self.line4, = axes.plot([], [], '-go')
                self.line5, = axes.plot([], [], '-mo')
                self.line6, = axes.plot([], [], '-yo')

                self.coupler, = axes.plot([], [], '--')

                # make pause button
                axpause = self.fig.add_axes([0.4, 0.05, 0.2, 0.075])
                self.bpause = Button(axpause, 'Play/Pause')
                self.bpause.on_clicked(self.toggle_pause)

                # make goto button
                axgoto = self.fig.add_axes([0.6, 0.05, 0.2, 0.075])
                self.bgoto = Button(axgoto, 'Go to')
                self.bgoto.on_clicked(self.gotoframe)

                self.cur_frame = None
                self.ani = FuncAnimation(self.fig, self.update, frames=frames, interval=0, blit=True, repeat=True)



        def toggle_pause(self, event):
                if self.paused:
                        self.ani.resume()
                else:
                        self.ani.pause()
                self.paused = not self.paused


        def update(self, frame):

                self.cur_frame = frame

                # links positions for the current frame
                l1xf = self.l1x[frame]
                l2xf = self.l2x[frame]
                l3xf = self.l3x[frame]
                l4xf = self.l4x[frame]
                l5xf = self.l5x[frame]

                l1yf = self.l1y[frame]
                l2yf = self.l2y[frame]
                l3yf = self.l3y[frame]
                l4yf = self.l4y[frame]
                l5yf = self.l5y[frame]

                # path of the coupler
                vax = np.array(self.l2x)
                vbx = np.array(self.l3x)
                xcc = 0.5 * (vax + vbx)

                vay = np.array(self.l2y)
                vby = np.array(self.l3y)
                ycc = 0.5 * (vay + vby)

                ccx = xcc[:frame]
                ccy = ycc[:frame]

                # draw the lines
                self.line1.set_data([l4xf, l1xf], [l4yf, l1yf])
                self.line2.set_data([l1xf, l2xf], [l1yf, l2yf])
                self.line3.set_data([l2xf, l3xf], [l2yf, l3yf])
                self.line4.set_data([l3xf, l4xf], [l3yf, l4yf])
                self.line5.set_data([l3xf, l5xf], [l3yf, l5yf])
                self.line6.set_data([l2xf, l5xf], [l2yf, l5yf])

                # draw the coupler path
                #self.coupler.set_data([ccx, ccy])

                #return self.line1, self.line2, self.line3, self.line4, self.coupler
                return self.line1, self.line2, self.line3, self.line4, self.line5, self.line6


        def gotoframe(self, event):
                if self.toggles_empty == True:
                    return
                if not self.paused:
                    self.toggle_pause(event)
                self.update(next(self.toggles))                
                self.fig.canvas.draw()
