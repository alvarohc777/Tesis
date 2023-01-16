import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Módulos con funciones auxiliares de la tesis
from utils.preprocess import windows_creator
from utils.signalload import CSV_pandas_path, CSV_pandas
from utils.plot_funcs import signal_plt, plot_signal_fft
from utils.detection import detection_iter
from utils.animation import signal_animation, signal_render

st.title("Tesis")
st.markdown("Esta es la interfaz gráfica de mi tesis" "Álvaro Herrada - 2023")

N = 64
signal_name = "I: X0024A-R1A"
signals = CSV_pandas()
signal, t, _ = signals.load_data(signal_name)

(signal_window, signal_si_window, t_window), (
    signal_fft,
    signal_si_fft,
    xf,
) = windows_creator(N, signals, signal_name, windows_fourier=True)

signal_fundamental = signal_fft[:, 1]
si_fundamental = signal_si_fft[:, 1]

trip = detection_iter(signal_fft, signal_fundamental)
col1, col2 = st.columns(2)
fig = signal_plt(t, signal)
fig2 = plot_signal_fft(t, signal, t_window, trip)
# plt.show()
col1.pyplot(fig)
col2.pyplot(fig2)

ani_frames = signal_animation(t_window, signal_window)
ani_frames2 = signal_animation(t_window, signal_fft)
anim = signal_render([ani_frames])
components.html(anim[0].to_jshtml(), height=800)
# col1.pyplot(fig)
# col2.pyplot(fig)
