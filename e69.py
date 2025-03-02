# Example 6.9 (p. 327)
# Velocity Analysis of a Fourbar Slider-Crank Linkage with the Vector Loop Method

from e43 import *

ddot = 1200 # mm / s

# Circuit 1
omega2_1 = (ddot * cos(theta3_1)) / a / (cos(theta2_1) * sin(theta3_1) - sin(theta2_1) * cos(theta3_1))
omega3_1 = a * omega2_1 * cos(theta2_1) / b / cos(theta3_1)

print('omega2_1:', round(omega2_1, 3))
print('omega3_1:', round(omega3_1, 3))

# Circuit 1
omega2_2 = (ddot * cos(theta3_2)) / a / (cos(theta2_2) * sin(theta3_2) - sin(theta2_2) * cos(theta3_2))
omega3_2 = a * omega2_2 * cos(theta2_2) / b / cos(theta3_2)

print('omega2_2:', round(omega2_2, 3))
print('omega3_2:', round(omega3_2, 3))