import utils.auxfunctions as ax
import utils.signalload as sl
from utils.deco import calc_perf
from utils.signalload import CSV, CSV_prueba
from utils.auxfunctions import (
    superimposed,
    moving_window,
    fourier,
    iterator_mp,
    superi_iterator_gif,
)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import get_window as wndw


from itertools import repeat
import concurrent.futures

# Transformada rápida de Fourier
from scipy.fft import rfft, rfftfreq


@calc_perf
def main():
    # from utils.auxfunctions import iterator_mp

    signal = CSV_prueba()
    dt = signal.dt
    t = signal.t
    fs = signal.fs
    signal = signal.R01Ia
    plt.plot(t, signal)
    plt.show()

    si_signal = superimposed(signal, fs)
    plt.plot(t, si_signal)
    plt.show()

    # Creador de la Window Function
    window_len_t = 1 / 60
    window_len = int((window_len_t) // dt)
    N = window_len
    step = 8

    window_name = "boxcar"
    window_function = wndw(window_name, window_len, fftbins=True)

    windows, windows_si, windows_t = list(
        map(moving_window, [signal, si_signal, t], repeat(window_len), repeat(step))
    )

    # Para plottear en paralelo
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(
            iterator_mp,
            [windows, windows_si],
            repeat(windows_t),
            repeat(window_function),
            repeat(N),
            repeat(dt),
            ["STFT", "SI"],
        )

    # Para plottear y guardar el GIF
    # superi_iterator_gif(windows, windows_si, windows_t, window_function, N, dt)


if __name__ == "__main__":
    main()
