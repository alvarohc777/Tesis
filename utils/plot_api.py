from utils.auxfunctions import superimposed, moving_window
from utils.preprocess import windows_creator
from utils.detection import detection_iter
import numpy as np
from itertools import repeat
import matplotlib.pyplot as plt


def img_signal(request_information, no_return=False):
    signal_name = request_information["signal_name"]
    signals = request_information["signals"]
    signal, t, params = signals.load_data(signal_name)
    request_information["signal"] = signal
    request_information["t"] = t
    request_information["params"] = params
    if no_return:
        return
    return t.tolist(), signal.tolist(), "linear", "img"


def img_si_signal(request_information, no_return=False):
    signal = request_information.get("signal", "")

    if len(signal) == 0:
        img_signal(request_information, no_return=True)

    signal = request_information["signal"]
    fs = request_information["params"]["fs"]
    si_signal = superimposed(signal, fs)
    t = request_information["t"]

    return t.tolist(), si_signal.tolist(), "linear", "img"


def anim_signal(request_information, no_return=False):
    signal = request_information.get("signal", "")
    t = request_information["t"]
    window_length = request_information["window_length"]
    step = request_information["step"]
    signal_window, t_window = list(
        map(moving_window, [signal, t], repeat(window_length), repeat(step))
    )
    return t_window, signal_window, "", "anim"


def anim_si_signal(request_information, no_return=False):
    pass


def anim_fft(request_information, no_return=False):
    pass


def anim_si_fft(request_information, no_return=False):
    pass


def anim_trip(request_information, no_return=False):
    pass


def img_trip(request_information, no_return=False):
    signals = request_information["signals"]
    signal_name = request_information["signal_name"]
    (signal_window, signal_si_window, t_window), (
        signal_fft,
        signal_si_fft,
        xf,
    ) = windows_creator(
        64,
        signals=signals,
        signal_name=signal_name,
        windows_fourier=True,
    )
    signal_fundamental = signal_fft[:, 1]
    si_fundamental = signal_si_fft[:, 1]
    trip = detection_iter(signal_fft, signal_fundamental)
    t_window = np.insert(t_window[:, -1], 0, 0)
    trip = np.insert(trip, 0, 0)
    return t_window.tolist(), trip.tolist(), "hv", "img"
