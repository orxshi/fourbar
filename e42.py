# Example 4.2 (p. 197)
# Position Analysis of a Fourbar Crank-Slider Linkage with the Vector Loop Method

from math import pi, cos, sin, asin, degrees, radians


# The lengths of the links
a = 40
b = 120
c = -20
# ground link will have changing length (d)

theta1 = 0
theta2 = radians(60)
theta4 = pi / 2

theta3_cros = asin((a * sin(theta2) - c * sin(theta4)) / b)
theta3_open = asin((-a * sin(theta2) + c * sin(theta4)) / b) + pi
d = a * cos(theta2) - b * cos(theta3_cros) - c * cos(theta4)

if theta3_cros < 0:

    theta3_cros += 2 * pi

if theta3_open < 0:
    theta3_open += 2 * pi

print('theta3_open:', round(degrees(theta3_open), 2))
print('theta3_cros:', round(degrees(theta3_cros), 2))
print('d:', round(d, 2))