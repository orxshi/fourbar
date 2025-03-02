# Example 4.3 (p. 200)
# Position Analysis of a Fourbar Slider-Crank Linkage with the Vector Loop Method

# I think there is a mistake in Example 4.3
# dTDC = b + a only if offset c = 0
# Same applies to dBDC
# However, final answers are matching

from math import pi, degrees, atan2, sqrt, sin, asin, cos


# Link lengths
a = 40
b = 120
c = -20
d = 100

# This part defers from the book
# Use the fact that (a+b)^2 = c^2 + dTDC^2
dTDC = sqrt((a + b) ** 2 - c ** 2)
dBDC = sqrt((a - b) ** 2 - c ** 2)

assert(d <= dTDC)
assert(d >= dBDC)

K1 = a ** 2 - b ** 2 + c ** 2 + d ** 2
K2 = -2 * a * c
K3 = -2 * a * d

A = K1 - K3
B = 2 * K2
C = K1 + K3

theta2_1 = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))
theta2_2 = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))

print('theta2_1:', round(degrees(theta2_1), 3))
print('theta2_2:', round(degrees(theta2_2), 3))


# Circuit 1
# There are two theta3_1 but only one is correct
theta3_1a = asin((a * sin(theta2_1) - c) / b)
theta3_1b = asin(-(a * sin(theta2_1) - c) / b) + pi

dd1 = a * cos(theta2_1) - b * cos(theta3_1a)
dd2 = a * cos(theta2_1) - b * cos(theta3_1b)

if abs(dd1 - d) < 0.1:
    theta3_1 = theta3_1a
elif abs(dd2 - d) < 0.1:
    theta3_1 = theta3_1b
else:
    assert(False)

# Circuit 2
# There are two theta3_2 but only one is correct
theta3_2a = asin((a * sin(theta2_2) - c) / b)
theta3_2b = asin(-(a * sin(theta2_2) - c) / b) + pi

dd1 = a * cos(theta2_2) - b * cos(theta3_2a)
dd2 = a * cos(theta2_2) - b * cos(theta3_2b)

if abs(dd1 - d) < 0.1:
    theta3_2 = theta3_2a
elif abs(dd2 - d) < 0.1:
    theta3_2 = theta3_2b
else:
    assert(False)


print('theta3_1:', round(degrees(theta3_1), 3))
print('theta3_2:', round(degrees(theta3_2), 3))


    