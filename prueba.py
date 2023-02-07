from utils.signalload import CSV_pandas
import utils.plot_api as plt_api
import matplotlib.pyplot as plt

request_information = {}
signals = CSV_pandas()
signals.relay_list()
request_information["signal_name"] = "I: X0023A-R1A"
request_information["signals"] = signals

t, signal, _, _ = plt_api.img_trip(request_information)
plt.plot(t, signal)
plt.show()
