import utils.auxfunctions as ax
import utils.signalload as sl

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


signal = sl.CSV()

y = signal.R01Ia
x = signal.t

# plt.plot(y[400:500])
# plt.show()

# Configurar el setting de la gráfica
ymin, ymax = min(y), max(y)
fig = plt.figure()
axis = fig.add_subplot(111)
(line,) = axis.plot([], [])


def ini():
    line.set_data([], [])
    return (line,)


y_window = ax.moving_window(y, 64, 1)
x_window = ax.moving_window(x, 64, 1)
frames = len(x_window)
print(x_window.shape)


def animate(i):
    line.set_data(x_window[i], y_window[i])
    axis.set_xlim(x_window[i, 0], x_window[i, -1])
    axis.set_ylim(ymin, ymax)
    return (line,)


anim = FuncAnimation(fig, animate, init_func=ini, frames=frames, interval=100)
plt.show()
