from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import numpy as np

# Custom functions and classes
from utils.signalload import CSV_pandas_path
from utils.plot_funcs import signal_plt
from utils.auxfunctions import superimposed
from utils.preprocess import windows_creator
from utils.detection import detection_iter

from pydantic import BaseModel
import json

app = FastAPI()
origins = ["null", "http://localhost:8080", "http://127.0.0.1:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SignalName(BaseModel):
    # csv_name: str
    signal_name: str


# Variables
request_information = {}


@app.get("/", tags=["HomePage"])
async def root() -> dict:
    return {"ping": "pong"}


@app.post("/uploadCSV", tags=["CSV"])
async def post_CSV(csv_files: UploadFile = File(...)) -> dict:
    with open(csv_files.filename, "wb+") as f:
        f.write(csv_files.file.read())

    csv_file_name = csv_files.filename
    signals = CSV_pandas_path(csv_file_name)

    request_information["filename"] = csv_file_name
    request_information["signals"] = signals
    print(f"csv filename: {csv_file_name}")

    return {"signals_list": signals.labels_list, "file_name": csv_file_name}


@app.post("/signalName", tags=["CSV"])
async def post_signal_name(load: SignalName):
    signal_name = load.signal_name
    signals = request_information["signals"]
    request_information["signal_name"] = signal_name

    signal, t, params = signals.load_data(signal_name)

    request_information["signal"] = signal
    request_information["t"] = t
    request_information["params"] = params

    return {"response": signal_name}


@app.post("/plots/imgSignal", tags=["static_plots"])
async def plot_signal(request: dict = Body(...)):
    signal = request_information["signal"].tolist()
    t = request_information["t"].tolist()

    return [t, signal]


@app.post("/plots/imgSISignal", tags=["static_plots"])
async def plot_si_signal(request: dict = Body(...)):
    signal = request_information["signal"]
    fs = request_information["params"]["fs"]
    si_signal = superimposed(signal, fs).tolist()
    t = request_information["t"].tolist()

    return [t, si_signal]


@app.post("/plots/imgTripSignal", tags=["static_plots"])
async def plot_trip_signal(request: dict = Body(...)):
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
    t_window = np.insert(t_window[:, -1], 0, 0).tolist()
    trip = np.insert(trip, 0, 0).tolist()

    return [t_window, trip]


#     (signal_window, signal_si_window, t_window), (
#     signal_fft,
#     signal_si_fft,
#     xf,
# ) = windows_creator(N, signals, signal_name, windows_fourier=True)
