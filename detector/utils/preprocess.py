from utils.deco import calc_perf
from utils.signalload import CSV, CSV_prueba
from utils.auxfunctions import superimposed, moving_window, fourier, xf_calc

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import get_window as wndw

import inspect
from itertools import repeat


def windows_creator(window_len):
    # from utils.auxfunctions import iterator_mp

    # signal = CSV_prueba()
    signal = CSV()
    dt = signal.dt
    t = signal.t
    fs = signal.fs
    signal = signal.R01Ia
    # plt.plot(t, signal)
    # plt.show()

    si_signal = superimposed(signal, fs)
    # plt.plot(t, si_signal)
    # plt.show()

    # Creador de la Window Function
    window_len_t = 1 / 60
    # window_len = int((window_len_t) // dt)
    N = window_len
    step = 4

    window_name = "boxcar"
    window_function = wndw(window_name, window_len, fftbins=True)

    windows, windows_si, windows_t = list(
        map(moving_window, [signal, si_signal, t], repeat(window_len), repeat(step))
    )

    # regresa dt si la función es llamada desde windows_fourier()
    # porque esta necesita la variable dt para hallar xf
    if inspect.stack()[1][3] == "windows_fourier":
        return windows, windows_si, windows_t, dt
    else:
        return windows, windows_si, windows_t


def windows_fourier(window_len):

    windows, windows_si, windows_t, dt = windows_creator(window_len)
    xf = xf_calc(window_len, dt)
    windows_fft = fourier(windows, window_len)
    windows_si_fft = fourier(windows_si, window_len)

    return windows_fft, windows_si_fft, xf
