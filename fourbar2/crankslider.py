from link import *
from anim import Animation, plt


l2.l = 40
l3.l = 120
l4.l = 20

a = l2.l
b = l3.l
c = l4.l

def coor(T2, T3, T4):

    l1.x[i] = 0
    l1.y[i] = 0

    l2.x[i] = l1.x[i] + a * cos(T2)
    l2.y[i] = l1.y[i] + a * sin(T2)

    l3.x[i] = l2.x[i] + b * cos(T3)
    l3.y[i] = l2.y[i] + b * sin(T3)

    l4.x[i] = l3.x[i] + c * cos(T4)
    l4.y[i] = l3.y[i] + c * sin(T4)


l2.T = numpy.linspace(0, 2 * pi, num=frames)

for i, T2 in enumerate(l2.T):

    T4 = pi / 2
    T3 = asin((-c * sin(T4) - a * sin(T2)) / b)
    d = a * cos(T2) + b * cos(T3) + c * cos(T4)

    l3.T[i] = T3
    l4.T[i] = T4

    coor(T2, T3, T4)

    assert(abs(l4.x[i] - d) < 0.1)
    assert(abs(l4.y[i] - 0) < 0.1)


anim = Animation([])
plt.show()
