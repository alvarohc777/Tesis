from utils.preprocess import windows_creator
from utils.signalload import CSV_pandas, CSV_pandas_path
from utils.animation import signal_animation, signal_render
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from utils.detection import harmonic_distortion, detector, detection_iter


N = 64
# signal_name = "I: X0024A-R1A"
signal_name = "I: X0022A-R1A"
# signal_name = "I: X0042A-R1A"

# signals = CSV_pandas_path()
signals = CSV_pandas()
signals.relay_list()
# _, t, _ = signals.load_data(signal_name)
# t = signals.t

# signal, signal_si, t = windows_creator(N, signals, signal_name)

# signal, signal_si, t = windows_creator(N, signals, signal_name, windows_fourier=False)
(signal, signal_si, t), (signal_fft, signal_si_fft, xf) = windows_creator(
    N, signals, signal_name, windows_fourier=True
)


y = signal
x = t
trip = detection_iter(signal_si_fft)
plt.stem(t[:, -1], trip)
# plt.stem(t, trip)
plt.show()
