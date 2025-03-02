# Example 4.1 (p. 194)
# Position Analysis of a Fourbar Linkage with the Vector Loop Method

from math import pi, cos, sin, atan2, sqrt, radians, degrees


# Link lengths
a = 40
b = 120
c = 80
d = 100

theta2 = radians(40)
theta1 = 0


K1 = d / a
K2 = d / c
K3 = (a**2 - b**2 + c**2 + d**2) / (2 * a * c)
K4 = d / b
K5 = (c**2 - d**2 - a**2 - b**2) / (2 * a * b)

A = cos(theta2) - K1 - K2 * cos(theta2) + K3
B = -2 * sin(theta2)
C = K1 - (K2 + 1) * cos(theta2) + K3
D = cos(theta2) - K1 + K4 * cos(theta2) + K5
E = -2 * sin(theta2)
F = K1 + (K4 - 1) * cos(theta2) + K5

theta4_open = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))
theta4_cros = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))

theta3_open = 2 * atan2((-E - sqrt(E**2 - 4 * D * F)) , (2 * D))
theta3_cros = 2 * atan2((-E + sqrt(E**2 - 4 * D * F)) , (2 * D))


# Angles may be positive or negative.
# For example, -30 degrees is equaivalent to -30 + 360 = 330 degrees.
# Similarly, 30 degrees is equaivalent to 30 - 360 = -330 degrees.

# theta4_open is made positive to compare with the book.
# theta4_cros is made negative to compare with the book.
# theta3_open is made positive to compare with the book.
# theta3_cros is made negative to compare with the book.
if theta4_open < 0:
    theta4_open += 2 * pi
if theta4_cros > 0:
    theta4_cros -= 2 * pi
if theta3_open < 0:
    theta3_open += 2 * pi
if theta3_cros > 0:
    theta3_cros -= 2 * pi

print('theta4_open:', round(degrees(theta4_open), 2))
print('theta4_cros:', round(degrees(theta4_cros), 2))
print('theta3_open:', round(degrees(theta3_open), 2))
print('theta3_cros:', round(degrees(theta3_cros), 2))