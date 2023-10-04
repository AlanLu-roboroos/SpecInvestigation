from scipy.optimize import curve_fit
import numpy as np
from sys import argv

def func(xx, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    return a + b*x**1 + c*x**2 + d*x**3 + e*x**4 + f*x**5 + g*x**6 + h*x**7 + i*x**8 + j*x**9 + k*x**10 + l*x**11 + m*x**12 + n*x**13 + o*x**14 + p*x**15 + q*x**16 + r*x**17 + s*x**18 + t*x**19 + u*x**20 + v*x**21 + w*x**22 + x*x**23 + y*x**24 + z*x**25


with open(argv[1], "r") as f:
    data = f.readlines()

yValues = [float(i.split()[0]) for i in data]

xValues = list(np.linspace(0, 8, len(data)))

t = curve_fit(func, xValues, yValues)

params = list(map(float, t[0]))

text = str(params[0])
for i in range(1, len(params)):
    text += f" + {params[i]}x^{{{i}}}"
print(text)
