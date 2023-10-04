import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from constants import *
from sys import argv

fig = plt.figure()
ax: plt.Axes = fig.add_subplot(projection='3d')

with open(argv[1], "r") as f:
    data = f.readlines()
    points = [list(map(float, i.split())) for i in data]

n = len(points)

time = np.linspace(0, 1, 100)

def bern(t, i):
    return math.comb(n, i)*math.pow(t, i)*math.pow(1-t, n-i)

def x(t):
    total = 0
    for i in range(0, n):
        total += bern(t, i) * points[i][0]
    return total

def y(t):
    total = 0
    for i in range(0, n):
        total += bern(t, i) * points[i][1]
    return total

def z(t):
    total = 0
    for i in range(0, n):
        total += bern(t, i) * points[i][2]
    return total


xvals = []
yvals = []
zvals = []

for i in time:
    xvals.append(x(i))
    yvals.append(y(i))
    zvals.append(z(i))


ax.plot(xvals, yvals, zvals, label='bezier quad')
ax.scatter([i[0] for i in points], [i[1] for i in points], [i[2] for i in points])

ax.legend()
ax.axes.set_xlim3d(left=0, right=10)
ax.axes.set_ylim3d(bottom=-2, top=8)
ax.axes.set_zlim3d(bottom=-7, top=3)
ax.view_init(elev=15, azim=-43)
# plt.savefig('Pictures/figure1.png', format='png', dpi=1200)
plt.show()
