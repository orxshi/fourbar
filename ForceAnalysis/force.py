# Example 11.3 (p. 602)
# Dynamic Force Analysis of a Fourbar Linkage

from pos import pos
from vel import vel
from acc import *
from Vector import Vector, rotate, unit, mag
from scipy import linalg
import numpy as np
from math import radians
from constants import *




def force(a, b, c, d, theta2, omega2, alpha2, m2, m3, m4, IG2, IG3, IG4, CG2_LRCS, CG3_LRCS, CG4_LRCS):

  # Link 1 kinematics
  theta1 = 0
  omega1 = 0
  alpha1 = 0

  # position analysis
  theta3_open, theta4_open, theta3_cros, theta4_cros = pos(a, b, c, d, theta2)

  # do the position analysis for open circuit
  theta3 = theta3_open
  theta4 = theta4_open

  # velocity analysis
  omega3, omega4 = vel(a, b, c, d, theta2, theta3, theta4, omega2)

  # acceleration analysis
  alpha3, alpha4 = acc(a, b, c, d, theta2, theta3, theta4, omega2, omega3, omega4, alpha2)

  
  
  RO2  = Vector.polar(0, 0)
  RO4  = RO2 + Vector.polar(d, 0)
  RA   = RO2 + Vector.polar(a, theta2)
  RBO4 = Vector.polar(c, theta4)
  RBO2 = RO4 + RBO4
  RBA  = RBO2 - RA

  VO2, AO2 = VelAcc(RO2, omega1, alpha1)
  VA, AA   = VelAcc(RA, omega2, alpha2)
  VB, AB   = VelAcc(RBO2, omega4, alpha4)
  VBA, ABA = VelAcc(RBA, omega3, alpha3)
  VO4, AO4 = VelAcc(RO4, omega1, alpha1)

  RG2   = rotate(CG2_LRCS, theta2)
  RG3A  = rotate(CG3_LRCS, theta3)
  RG4O4 = rotate(CG4_LRCS, theta4)

  VG2O2, AG2O2 = VelAcc(RG2, omega2, alpha2)
  VG3A, AG3A   = VelAcc(RG3A, omega3, alpha3)
  VG4O4, AG4O4 = VelAcc(RG4O4, omega4, alpha4)

  # velocities and accelerations in GCS
  VG2 = VG2O2 + AO2
  AG2 = AG2O2 + VO2
  VG3 = VG3A + VA
  AG3 = AG3A + AA
  VG4 = VG4O4 + VO4
  AG4 = AG4O4 + AO4

  # print('AG2:', AG2)
  # print('AG3:', AG3)
  # print('AG4:', AG4)

  

  CG2 = rotate(CG2_LRCS, theta2)
  # The following vectors are respect to CGs of links
  R12 = -CG2
  R32 = R12 + RA
  R23 = -rotate(CG3_LRCS, theta3)
  R43 = RBO2 - (RA - R23)
  R34 = RBO4 - RG4O4
  R14 = -RG4O4
  RP  = rotate(RPG3_LRCS, theta3)

  # print('R12:', R12)
  # print('R32:', R32)
  # print('R23:', R23)
  # print('R43:', R43)
  # print('R34:', R34)
  # print('R14:', R14)
  # print('RP:', RP)

  M = np.zeros((9, 9))

  M[0,0] = 1
  M[0,2] = 1

  M[1,1] = 1
  M[1,3] = 1

  M[2,0] = -R12.y
  M[2,1] = R12.x
  M[2,2] = -R32.y
  M[2,3] = R32.x
  M[2,8] = 1

  M[3,2] = -1
  M[3,4] = 1

  M[4,3] = -1
  M[4,5] = 1

  M[5,2] = R23.y
  M[5,3] = -R23.x
  M[5,4] = -R43.y
  M[5,5] = R43.x

  M[6,4] = -1
  M[6,6] = 1

  M[7,5] = -1
  M[7,7] = 1

  M[8,4] = R34.y
  M[8,5] = -R34.x
  M[8,6] = -R14.y
  M[8,7] = R14.x

  RHS = np.zeros(9)

  RHS[0] = m2 * AG2.x
  RHS[1] = m2 * AG2.y
  RHS[2] = IG2 * alpha2
  RHS[3] = m3 * AG3.x - FP.x
  RHS[4] = m3 * AG3.y - FP.y
  RHS[5] = IG3 * alpha3 - RP.x * FP.y + RP.y * FP.x
  RHS[6] = m4 * AG4.x
  RHS[7] = m4 * AG4.y
  RHS[8] = IG4 * alpha4 - T4

  x = linalg.solve(M, RHS)

  # print('F12x:', x[0])
  # print('F12y:', x[1])
  # print('F32x:', x[2])
  # print('F32y:', x[3])
  # print('F43x:', x[4])
  # print('F43y:', x[5])
  # print('F14x:', x[6])
  # print('F14y:', x[7])
  # print('T12:' , x[8])

  # print(RHS[0])
  # print(RHS[1])
  # print(RHS[2])
  # print(RHS[3])

  

  return x


# # Link lengths
# a = 5
# b = 15
# c = 10
# d = 19

# # Link 2 kinematics
# theta2 = radians(60)
# omega2 = 25 # rad/s
# alpha2 = -40 # rad/s^2

# x = force(a, b, c, d, theta2, omega2, alpha2)