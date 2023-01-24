from utils.preprocess import windows_creator
from utils.signalload import CSV_pandas, CSV_pandas_path
from utils.animation import signal_animation, signal_render, fft_animation
from utils.plot_funcs import plot_signal_fft
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from utils.detection import harmonic_distortion, detector, detection_iter
import numpy as np

N = 64
signal_name = "I: X0024A-R1A"  # Fallas
# signal_name = "I: X0022A-R1A"  # Caps
# signal_name = "I: X0042A-R1A"  # HIF
signal_name = "I: X0024A-R1A"  # HIF

# signals = CSV_pandas_path()
signals = CSV_pandas()
signals.relay_list()
signal, t, _ = signals.load_data(signal_name)

(signal_window, signal_si_window, t_window), (
    signal_fft,
    signal_si_fft,
    xf,
) = windows_creator(N, signals, signal_name, windows_fourier=True)

signal_fundamental = signal_fft[:, 1]
si_fundamental = signal_si_fft[:, 1]

# y = signal_fft
# x = np.tile(xf, (len(y), 1))
y = signal_fft
x = xf

trip = detection_iter(signal_fft, signal_fundamental)
fig = plot_signal_fft(t, signal, t_window, trip)
# a = fft_animation(x, y)
# anim = signal_render([a], interval=20)
plt.show()
