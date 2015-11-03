# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0,10,100)
y = x**2+2

ax.plot(x,y)
ax.fill_between(x[20:80], y[20:80], color=(0,0.7,0.7,0.3) )
ax.plot(np.linspace(-1,10), np.zeros((50,1)), color=(0,0,0))
ax.plot(np.zeros((50,1)), np.linspace(-10,100), color=(0,0,0))
ax.plot(np.ones((10,1))+1, np.linspace(0,6,10), color=(1,0,0))
ax.plot(np.ones((10,1))+7, np.linspace(0,66,10), color=(1,0,0))
ax.text(10,-5,"X")
ax.text(10,-5,"X")
ax.text(-0.5,80,"Y")
ax.text(2,-5,"a")
ax.text(8,-5,"b")
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels('')
ax.set_yticklabels('')
ax.set_ylim([-10,80])
ax.set_axis_off()
ax.text(1.5, 30, "$\int_a^b{f(x)} = F(b)-F(a)$")

fig.savefig('fig.png')

plt.show()
