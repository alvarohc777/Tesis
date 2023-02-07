from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import numpy as np

# Custom functions and classes
from utils.signalload import CSV_pandas_path
from utils.plot_funcs import signal_plt
from utils.auxfunctions import superimposed
from utils.preprocess import windows_creator
from utils.detection import detection_iter
import utils.plot_api as plt_api

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


@app.post("/uploadCSV", tags=["CSV"])
async def post_CSV(csv_files: UploadFile = File(...)) -> dict:
    with open(csv_files.filename, "wb+") as f:
        f.write(csv_files.file.read())
    request_information.clear()
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

    return {"response": signal_name}


@app.post("/plots/imgSignal", tags=["static_plots"])
async def plot_signal(request: dict = Body(...)):

    t, signal, line_shape = plt_api.img_signal(request_information)

    return [t, signal, line_shape]


@app.post("/plots/imgSISignal", tags=["static_plots"])
async def plot_si_signal(request: dict = Body(...)):

    si_signal, t, line_shape = plt_api.img_si_signal(request_information)

    return [t, si_signal, line_shape]


@app.post("/plots/imgTrip", tags=["static_plots"])
async def plot_trip_signal(request: dict = Body(...)):

    t_window, trip, line_shape = plt_api.img_trip(request_information)

    return [t_window, trip, line_shape]


app.mount("/", StaticFiles(directory="public", html=True), name="static")


# Para servir la página
prueba = FastAPI()
prueba.mount("/prueba", StaticFiles(directory="public", html=True), name="prueba")
