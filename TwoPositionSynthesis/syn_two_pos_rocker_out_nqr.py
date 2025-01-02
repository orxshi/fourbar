# This code synthesize non-quick-return four-bar only
# See Section 5.2 (two-position synthesis for rocker output, p. 234)

from Vector import *


# input
c    = 80
T4   = 40
beta = 30
K    = 50

# convert degrees to radians
beta = radians(beta)
T4   = radians(T4)

R_O4 = Vector(x = 0, y = 0) # O4 is the origin
R_B1 = R_O4 + Vector.polar(c, T4)
R_B2 = R_O4 + Vector.polar(c, T4 + beta)

M = R_B2 - R_B1

R_O2 = R_B1 + K * unit(M)
R_O2_B2 = R_B2 - R_O2
R_O2_B1 = R_B1 - R_O2

assert mag(R_O2_B1) > mag(M), 'Increase K so that |O2-B1| > |M|'
        
d = mag(R_O2 - R_O4)
a = mag(M) / 2
b = mag(R_O2_B1) - a

print(round(a), round(b), round(c), round(d))
