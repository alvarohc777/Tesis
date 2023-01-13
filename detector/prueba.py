from utils.signalload import CSV_pandas, CSV_pandas_path
from utils.auxfunctions import superimposed, moving_window, fourier
from utils.detection import detector, harmonic_distortion, detection_iter
import numpy as np
import matplotlib.pyplot as plt
from itertools import repeat


# Parametros de selección del usuario:


N = 64  # Tamaño de la ventana (muestras)
step = 4  # Pasos de las ventanas (muestras que entran, muestras que salen por ventana)
window_name = "boxcar"
# ----------------------------------

# Cargue de datos


signal = CSV_pandas_path()
signal.relay_list(voltages=True, Models=True)
signal.relay_list()

# signal_name = input("Input relay name ").strip()
signal, t, params = signal.load_data("I: X0024A-R1A")
# signal, t, params = signal.load_data("I: X0022A-R1A")

# Preprocesamiento
signal_si = superimposed(signal, params["fs"])

print(signal.shape)
# Hacer de esto una función
windows, windows_si, windows_t = list(
    map(moving_window, [signal, signal_si, t], repeat(N), repeat(step))
)

xf, windows_fft = fourier(windows, N, params["dt"])
xf, windows_si_fft = fourier(windows_si, N, params["dt"])


# detector
# Cambiar el 90 por algún otro número (input)
signal_fundamental = windows_fft[:, 1]
si_fundamental = windows_si_fft[:, 1]

fig, ax = plt.subplots(3, figsize=(10, 6))

# HDF, HDC = harmonic_distortion(windows_fft[90], windows_fft[90, 1])
ax[0].plot(t, signal)


# trip = detection_iter(windows_fft, signal_fundamental)
trip, HDF, HDC = detection_iter(windows_fft, signal_fundamental, return_THD=True)
ax[1].stem(windows_t[:, -1], trip)
print(windows_t.shape)

ax[2].stem(windows_t[:, -1], HDF)
plt.show()
