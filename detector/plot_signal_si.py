from utils.preprocess_old import windows_creator, windows_fourier
import matplotlib.pyplot as plt
from utils.signalload import CSV
from utils.auxfunctions import superimposed

signal = CSV()
t = signal.t
fs = signal.fs


signal = signal.R01Ia
# signal = signal.Ic

si = superimposed(signal, fs)


fig, ax = plt.subplots(2, figsize=(10, 6))
fig.text(0.08, 0.5, "Amplitud (A)", ha="center", va="center", rotation="vertical")
ax[1].set_xlabel("Tiempo (s)")
ax[0].plot(t, signal)
ax[1].plot(t, si)
ax[0].set_xticks([])
plt.show()

# signal, si, t = windows_creator(64)

# # fft, si_fft, xf = windows_fourier(64)
# print(signal.shape)
# # plt.stem(t[81], signal[81])


# fig, ax = plt.subplots(2, figsize=(10, 6))
# fig.suptitle("SFTF Señal", fontsize=16)
# fig.text(0.08, 0.5, "Amplitud (A)", ha="center", va="center", rotation="vertical")
# # ax[0].set_xticks(xf[1::2])
# ax[1].set_xlabel("Tiempo (s)")
# # ax[1].set_ylabel("Amplitud (A)")
# ax[0].plot(t[81], si[81])
# ax[1].plot(t[81], si[81])
# ax[0].set_xticks([])
# plt.show()
# # plt.plot(t[81], si[81])
# # plt.stem(xf, fft[0])
