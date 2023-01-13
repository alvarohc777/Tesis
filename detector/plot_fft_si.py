# from utils.preprocess import windows_creator, windows_fourier
from utils.preprocess_old import windows_creator, windows_fourier
import matplotlib.pyplot as plt
from utils.signalload import CSV
from utils.auxfunctions import superimposed, xf_calc, fourier


signal, si, t = windows_creator(64)

fft, si_fft, xf = windows_fourier(64)
# print(signal.shape)
# plt.stem(t[81], signal[81])


fig, ax = plt.subplots(2, figsize=(10, 6))
# fig.suptitle("SFTF Señal", fontsize=16)
fig.text(0.08, 0.5, "Amplitud (A)", ha="center", va="center", rotation="vertical")
# # ax[0].set_xticks(xf[1::2])
ax[1].set_xlabel("Frecuencia (Hz)")
ax[0].set_xlabel("tiempo (s)")
# # ax[1].set_ylabel("Amplitud (A)")
# ax[0].plot(t[82], si[82])
# ax[1].stem(xf, si_fft[82])
ax[0].plot(t[82], signal[82])
print(len(t), len(signal), fft.shape)
ax[1].stem(xf[:15], fft[82, :15])
# ax[0].set_xticks([])
plt.show()
# # plt.plot(t[81], si[81])
# # plt.stem(xf, fft[0])


# signal = CSV()
# t = signal.tP
# fs = signal.fs
# dt = signal.dt
# signal = signal.R01Ia
# N = 64


# si = superimposed(signal, fs)

# signal_fft = fourier(signal, N)
# si_fft = fourier(si, N)

# xf = xf_calc(N, dt)

# fig, ax = plt.subplots(2, figsize=(10, 6))
# fig.text(0.08, 0.5, "Amplitud (A)", ha="center", va="center", rotation="vertical")
# ax[1].set_xlabel("Tiempo (s)")
# ax[0].stem(xf, signal_fft)
# ax[1].stem(xf, si_fft)
# ax[0].set_xticks([])
# plt.show()
