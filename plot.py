import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from constants import *
from sys import argv

fig = plt.figure()
ax: plt.Axes = fig.add_subplot(projection='3d')

if len(argv) > 1:
    inputFile = argv[1]
    with open(inputFile, "r") as f:
        data = f.readlines()

    qx = []
    qy = []
    qz = []
    for line in data:
        temp = line.split()
        qx.append(float(temp[0]))
        qy.append(float(temp[1]))
        qz.append(float(temp[2]))

    ax.plot(qx, qy, qz, label='quad air resistance')

x_0 = 0
y_0 = 0
z_0 = 0

vel_0 = 10
theta = 45
phi = 45


def deg2rad(ang):
    return ang * math.pi / 180
    # return ang


# Prepare arrays x, y, z
time = np.linspace(0, 5, 100)

# Linear Air Resistance
def lx(vel_0, theta, phi):
    return np.cos(deg2rad(phi)) * ((vel_0*np.cos(deg2rad(theta))*mass)/c)*(1-np.exp(-c*time/mass))+x_0  # type: ignore

def ly(vel_0, theta, phi):
    return np.sin(deg2rad(phi)) * ((vel_0*np.cos(deg2rad(theta))*mass)/c)*(1-np.exp(-c*time/mass))+y_0  # type: ignore

def lz(vel_0, theta, phi):
    return (mass/c)*(g*mass/c + vel_0*np.sin(deg2rad(theta)))*(1-np.exp(-c*time/mass))-g*mass*time/c+z_0  # type: ignore


# ax.plot(lx(vel_0, theta, phi), ly(vel_0, theta, phi), lz(vel_0, theta, phi), label='linear air resistance')

# No Air Resistance
def nx(vel_0, theta, phi):
    return vel_0*np.cos(deg2rad(phi))*np.cos(deg2rad(theta))*time + x_0  # type: ignore

def ny(vel_0, theta, phi):
    return vel_0*np.sin(deg2rad(phi))*np.cos(deg2rad(theta))*time + y_0  # type: ignore

def nz(vel_0, theta, phi):
    return -(9.8/2) * time**2 + vel_0 * np.sin(deg2rad(theta))*time + z_0  # type: ignore


ax.plot(nx(vel_0, theta, phi), ny(vel_0, theta, phi), nz(vel_0, theta, phi), label='no air resistance')

theta_s = Slider(
    ax=plt.axes((0.05, 0.25, 0.0225, 0.63)),
    label="theta",
    valmin=0,
    valmax=90,
    valinit=theta,
    orientation='vertical'
)

phi_s = Slider(
    ax=plt.axes((0.1, 0.25, 0.0225, 0.63)),
    label="phi",
    valmin=0,
    valmax=90,
    valinit=phi,
    orientation='vertical'
)

vel_0_s = Slider(
    ax=plt.axes((0.15, 0.25, 0.0225, 0.63)),
    label="vel_0",
    valmin=0,
    valmax=90,
    valinit=vel_0,
    orientation='vertical'
)


def update(val):
    # vel_0 = 10
    theta = theta_s.val
    phi = phi_s.val
    vel_0 = vel_0_s.val
    # phi = 45

    ax.cla()

    ax.plot(lx(vel_0, theta, phi), ly(vel_0, theta, phi), lz(vel_0, theta, phi), label='linear air resistance')
    ax.plot(nx(vel_0, theta, phi), ny(vel_0, theta, phi), nz(vel_0, theta, phi), label='no air resistance')

    ax.legend()
    ax.axes.set_xlim3d(left=0, right=10)
    ax.axes.set_ylim3d(bottom=-2, top=8)
    ax.axes.set_zlim3d(bottom=-7, top=3)
    ax.view_init(elev=15, azim=-43)
    # plt.savefig('Pictures/figure1.png', format='png', dpi=1200)


theta_s.on_changed(update)
phi_s.on_changed(update)
vel_0_s.on_changed(update)

ax.legend()
ax.axes.set_xlim3d(left=0, right=10)
ax.axes.set_ylim3d(bottom=-2, top=8)
ax.axes.set_zlim3d(bottom=-7, top=3)
ax.view_init(elev=15, azim=-43)
# plt.savefig('Pictures/figure1.png', format='png', dpi=1200)
plt.show()
