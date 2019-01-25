#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(12,6), dpi=80)

plt.subplot(121)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=1.5, linestyle="-")

plt.plot(X, S, color="green", linewidth=1.5, linestyle="-")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

plt.ylim(C.min()*1.1, C.max()*1.1)
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

plt.subplot(122)

plt.plot(X, C, "-.m", linewidth='1.5')

plt.plot(X, S, color="yellow", linewidth=1.5, linestyle="-")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True),
        [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])

plt.ylim(C.min()*1.1, C.max()*1.1)
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

plt.legend("upper left", frameon=True)

plt.savefig("matplot_p1.png")

