from signalload import CSV_pandas
import numpy as np
import matplotlib.pyplot as plt


signal = CSV_pandas()
# print(dir(signal))
# print(signal.I_X0004A_X0009A)
signal.relay_list()
print(signal.df.columns[0])
x, t, params = signal.load_data("I: X0024A-R1A")

# print(x[:, :20].shape)
print(params["dt"])
# plt.plot(x[0], x[1])
# plt.show()
