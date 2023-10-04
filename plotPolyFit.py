import matplotlib.pyplot as plt
import numpy as np
from sys import argv
import math

fig = plt.figure()
ax: plt.Axes = fig.add_subplot(projection="3d")

xcoef = []
ycoef = []
zcoef = []

for i in range(1, len(argv)):
    with open(argv[i], "r") as f:
        data = f.readlines()
        xcoef.append(list(map(float, data[0].split(","))))
        ycoef.append(list(map(float, data[1].split(","))))
        zcoef.append(list(map(float, data[2].split(","))))

print(list(xcoef))

def deg2rad(ang):
    return ang * math.pi / 180

def x(time, idx):
    command = ""
    count = 0
    for i in range(len(xcoef[idx]), 0, -1):
        command += f"{xcoef[idx][count]}*time**{i-1} + "
        count += 1
    command += "0"

    return eval(command)

def y(time, idx):
    command = ""
    count = 0
    for i in range(len(xcoef[idx]), 0, -1):
        command += f"{ycoef[idx][count]}*time**{i-1} + "
        count += 1
    command += "0"
    return eval(command)


def z(time, idx):
    command = ""
    count = 0
    for i in range(len(xcoef[idx]), 0, -1):
        command += f"{zcoef[idx][count]}*time**{i-1} + "
        count += 1
    command += "0"
    print(command)
    return eval(command)


time = np.linspace(0, 3, 100)


# ax.plot(nx(vel_0, theta), nz(vel_0, theta), label='no air resistance')
for i in range(0, len(xcoef)):
    ax.plot(x(time, i), y(time, i), z(time, i), label=f"Qudratic Air Resistance from Polynomials")

# ax.plot(x, y, label="quad")
ax.legend()
ax.axes.set_xlim3d(left=0, right=10)
ax.axes.set_ylim3d(bottom=-2, top=8)
ax.axes.set_zlim3d(bottom=-7, top=3)
ax.view_init(elev=15, azim=-43)
# plt.savefig('Pictures/figure1.png', format='png', dpi=1200)
plt.show()
