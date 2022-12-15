from utils.signalload import CSV_pandas, CSV_pandas_path
from utils.auxfunctions import superimposed, moving_window, fourier
import numpy as np
import matplotlib.pyplot as plt
from itertools import repeat


# Parametros de selección del usuario:


N = 64  # Tamaño de la ventana (muestras)
step = 4  # Pasos de las ventanas (muestras que entran, muestras que salen por ventana)
window_name = "boxcar"
# ----------------------------------


signal = CSV_pandas_path()
signal.relay_list()
signal, t, params = signal.load_data("I: X0024A-R1A")
signal_si = superimposed(signal, params["fs"])

print(signal.shape)
# Hacer de esto una función
windows, windows_si, windows_t = list(
    map(moving_window, [signal, signal_si, t], repeat(N), repeat(step))
)

xf, windows_fft = fourier(windows, N, params["dt"])
xf, windows_si_fft = fourier(windows_si, N, params["dt"])
print(windows.shape, windows_si_fft.shape)
plt.stem(xf, windows_si_fft[90])
plt.show()
# plt.plot(windows)
# plt.show()
