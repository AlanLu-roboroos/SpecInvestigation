import matplotlib.pyplot as plt
import numpy as np
import math
from sys import argv

fig = plt.figure()
ax: plt.Axes = fig.add_subplot()

x = []
y = []

with open(argv[1], "r") as f:
    data = f.readlines()

for line in data:
    temp = line.split()
    x.append(float(temp[0]))
    y.append(float(temp[1]))

def deg2rad(ang):
    return ang * math.pi / 180

def nx(vel_0, theta):
    return vel_0*np.cos(deg2rad(theta))*time + x_0  # type: ignore

def ny(vel_0, theta):
    return vel_0*np.cos(deg2rad(theta))*time + y_0  # type: ignore

def nz(vel_0, theta):
    return -(9.8/2) * time**2 + vel_0 * np.sin(deg2rad(theta))*time + z_0  # type: ignore


time = np.linspace(0, 5, 100)
vel_0 = 10
theta = 45

x_0 = 0
y_0 = 0
z_0 = 0


ax.plot(nx(vel_0, theta), nz(vel_0, theta), label='no air resistance')

ax.plot(x, y, label="quad")
ax.legend()
ax.set_xlim(left=-10, right=10)
ax.set_ylim(top=10, bottom=-10)
ax.set_aspect('equal')

plt.show()
