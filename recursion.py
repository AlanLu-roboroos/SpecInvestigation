from math import sqrt, cos, sin
# import matplotlib.pyplot as plt
import math
from constants import *

# fig = plt.figure()
# ax: plt.Axes = fig.add_subplot()

delta_t = 0.000001
max_t = 8

x_0 = 0
y_0 = 0
z_0 = 0

vel_0 = 10
theta = 45
phi = 45

def deg2rad(ang):
    return ang * math.pi / 180

def quad(vel_0, theta, phi):
    v_x = [float(vel_0*cos(deg2rad(phi))*cos(deg2rad(theta)))]
    v_y = [float(vel_0*sin(deg2rad(phi))*cos(deg2rad(theta)))]
    v_z = [float(vel_0*sin(deg2rad(theta)))]
    x = [0.0]
    y = [0.0]
    z = [0.0]

    idx = 0
    while idx * delta_t < max_t:
        v_x.append(v_x[idx] + delta_t * cos(deg2rad(phi)) * (-k/mass)*sqrt(v_x[idx]**2 + v_y[idx]**2 + v_z[idx]**2)*v_x[idx])
        v_y.append(v_y[idx] + delta_t * sin(deg2rad(phi)) * (-k/mass)*sqrt(v_x[idx]**2 + v_y[idx]**2 + v_z[idx]**2)*v_y[idx])
        v_z.append(v_z[idx] + delta_t * (-g - (k/mass)*sqrt(v_x[idx]**2 + v_y[idx]**2 + v_z[idx]**2)*v_z[idx]))
        idx += 1
        x.append(x[idx-1] + delta_t * v_x[idx])
        y.append(y[idx-1] + delta_t * v_y[idx])
        z.append(z[idx-1] + delta_t * v_z[idx])
        # print(f"idx: {idx}, v_x: {v_x[idx]}, v_y: {v_y[idx]}")
    return x, y, z


x, y, z = quad(vel_0, theta, phi)

with open("out.txt", "w") as f:
    for i in range(0, len(x)):
        f.write(f"{x[i]} {y[i]} {z[i]}\n")

    # ax.plot(x, y, label='quad')
    # ax.legend()
    # # plt.savefig('Pictures/figure1.png', format='png', dpi=1200)
    # plt.show()

    # print(v_x, v_y)
