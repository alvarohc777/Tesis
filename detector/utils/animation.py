from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def signal_animation(x, y):
    # Setting de la gráfica
    ymin, ymax = np.min(y), np.max(y)
    frames = len(x)

    fig = plt.figure()
    axis = fig.add_subplot(111)
    (line,) = axis.plot([], [])

    def ini():
        line.set_data([], [])
        return (line,)

    def animate(i):
        line.set_data(x[i], y[i])
        axis.set_xlim(x[i, 0], x[i, -1])
        axis.set_ylim(ymin, ymax)
        return (line,)

    return fig, animate, ini, frames


def signal_render(anims_list, interval=200):

    anim = []
    for figcomps in anims_list:
        fig, animate, ini, frames = figcomps
        anim.append(
            FuncAnimation(fig, animate, init_func=ini, frames=frames, interval=200)
        )
    return anim
