from forceloop import *
import matplotlib.pyplot as plt


T12 = np.array(T12)
Tavg = np.mean(T12)

areas = []
dtheta = 2 * pi / reso
current = 0
for T in T12:
    area = (Tavg - T) * dtheta
    current += area
    areas.append(current)

min_index = areas.index(min(areas))
max_index = areas.index(max(areas))

theregion= 0
for T in T12[min(max_index,min_index):max(max_index,min_index)]:
    theregion += (T - Tavg) * dtheta

k = 0.5 # coefficient of fluctuation
omega_avg = omega2

# absolute because theta_min_omega may be greater than theta_max_omega
I = theregion / k / omega_avg ** 2

print('I:', I)

Fl = k * omega2 # fluctuation

min_speed = 0.5 * (2 * omega2 - Fl) 
max_speed = Fl + min_speed

areas = [i * 2 / I for i in areas]

begin_speed = sqrt(max_speed ** 2 - areas[max_index])

Omega_2 = []
for area in areas:
    Omega_2.append(sqrt(begin_speed ** 2 + area))


power = Tavg * omega_avg

Tm = []
for i in range(len(Theta_rad)):
    Tm.append(power / Omega_2[i])

fig = plt.figure()
plt.plot(Theta_deg, T12)
# ax.ticklabel_format(useOffset=False)
plt.ticklabel_format(style='plain', useOffset=False, axis='y') 
plt.plot(Theta_deg, Tm)
plt.axhline(y = Tavg, color = 'r', linestyle = '-') 
plt.xlabel('Angle (deg)')
plt.ylabel('Smoothed input torque')
plt.show()


