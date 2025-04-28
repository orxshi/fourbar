from Vector import Vector
from math import radians

# Link lengths
a = 5
b = 15
c = 10
d = 19
# Link 2 kinematics
omega2 = 25 # rad/s
alpha2 = -40 # rad/s^2
# gravitational acceleration
g = 386 # in/s^2
# External force at P in GCS
FP = Vector.polar(80, radians(330))
# External torque on link 4 in GCS
T4 = 120 # lb.in
# Weights
# w2 = 1.5 # lb
# w3 = 7.7 # lb
# w4 = 5.8 # lb
# Mass moment of inertias
# IG2 = 0.4 # lb.in.s^2
# IG3 = 1.5 # lb.in.s^2
# IG4 = 0.8 # lb.in.s^2
# Following center of gravities are in LRCS
# CG1_LRCS  = Vector.polar(19, radians(0))
# CG2_LRCS  = Vector.polar(3, radians(30))
# CG3_LRCS  = Vector.polar(9, radians(45))
# CG4_LRCS  = Vector.polar(5, radians(0))
RPG3_LRCS = Vector.polar(3, radians(100))
# compute masses of links
# m2 = w2 / g
# m3 = w3 / g
# m4 = w4 / g