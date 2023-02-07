from utils.signalload import CSV_pandas
import matplotlib.pyplot as plt
from utils.auxfunctions import superimposed

# Parámetros escogidos por el cliente
N = 64
signal_name = "I: X0023A-R1A"
signals = CSV_pandas()


# 1. signal (static) API
signal, t, params = signals.load_data(signal_name)
# plt.plot(t, signal)


def img_si_signal():
    pass


# 2. super_imposed (static) API
if "signal" in locals():
    signal_si = superimposed(signal, params["fs"])
    # plt.plot(t, signal_si, t, signal)
    plt.plot(t, signal_si)

# 3. signal (anim) API


plt.show()
