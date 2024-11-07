from link import *
from solve import Solver
from anim import Animation
import matplotlib.pyplot as plt
from synthesize import *


def GCRR():
        # Input is the shortest (GCRR)
        l2.len = 40
        l3.len = 120
        l4.len = 80
        l1.len = 100
  
def GRCR():
        # Coupler is the shortest (GRCR)
        l2.len = 100
        l3.len = 40
        l4.len = 80
        l1.len = 120

def GCCC():
        # Ground is the shortest (GCCC)
        l2.len = 100
        l3.len = 120
        l4.len = 80
        l1.len = 40

def offset_slider():
        l2.len = 40
        l3.len = 120
        l4.len = 20

def inline_slider():
        l2.len = 40
        l3.len = 120
        l4.len = 0




#a, b, c, d = syn_two_pos_rocker_out(c = 80, T4 = 0, beta = 30, condition = 'Grashof')
#l2.len = a
#l3.len = b
#l4.len = c
#l1.len = d


#GCRR()
offset_slider()
#inline_slider()

sliding = True

if sliding:
    #Tc = 2
    Tc = 4
    #if Tc == 4:
        #l1.x = numpy.linspace(80, 160, num=int(frames/2))
else:
    Tc, cond, code = grashof(l2.len, l3.len, l4.len, l1.len)


#solver = Solver(Tc, sliding)
solver = Solver(Tc, False, True)
solver.gen()

print(solver.muf)

anim = Animation(solver.muf)
plt.show()


