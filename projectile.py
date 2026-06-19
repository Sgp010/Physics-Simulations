import matplotlib.pyplot as plt
import numpy as np

g = float(input()) # acceleration
s = 9.8 # meters
m = 1 # kg
angle = int(input()) * 3.14/180

v_s = s * np.sin(angle)
h_s = s * np.cos(angle)
a_s = (0 + v_s)/2

t = v_s/g

apex = t * a_s
h_d = 6.9* 2 * t
a_v = 0

def height(v,g, t):
    n = v- (g*t)
    a_v = (n+v)/2
    h = a_v * t
    return h

x = []
y = []
r = int(1000*2*t)
for i in range(r):
    x.append(h_s * (i/1000))
    y.append(height(v_s, g, (i/1000)))
plt.plot(x,y)
plt.show()