from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse
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
    request_information["plots"] = {}
    csv_file_name = csv_files.filename
    signals = CSV_pandas_path(csv_file_name)

    request_information["filename"] = csv_file_name
    request_information["signals"] = signals
    request_information["window_length"] = 64
    request_information["step"] = 4

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

    t, signal, line_shape, plot_type = plt_api.img_signal(request_information)
    print(plot_type)
    return [t, signal, line_shape, plot_type]


@app.post("/plots/imgSISignal", tags=["static_plots"])
async def plot_si_signal(request: dict = Body(...)):

    t, si_signal, line_shape, plot_type = plt_api.img_si_signal(request_information)
    print(plot_type)
    return [t, si_signal, line_shape, plot_type]


@app.post("/plots/imgTrip", tags=["static_plots"])
async def plot_trip_signal(request: dict = Body(...)):

    t_window, trip, line_shape, plot_type = plt_api.img_trip(request_information)
    print(plot_type)
    return [t_window, trip, line_shape, plot_type]


@app.post("/plots/animSignal", tags=["anim_plots"])
async def plot_signal_anim(request: dict = Body(...)):
    t_windows, signal_windows, line_shape, plot_type = plt_api.anim_signal(
        request_information
    )

    return [t_windows, signal_windows, line_shape, plot_type]


@app.post("/plots/animSISignal", tags=["anim_si_plots"])
async def plot_si_signal_anim(request: dict = Body(...)):
    t_windows, si_signal_windows, line_shape, plot_type = plt_api.anim_si_signal(
        request_information
    )
    return [t_windows, si_signal_windows, line_shape, plot_type]


@app.post("/plots/animTrip", tags=["anim_trip"])
async def plot_trip_anim(request: dict = Body(...)):
    # t_windows = request_information["t_windows"]
    # trip_windows, max_min, plot_type = plt_api.anim_trip(request_information)
    # return [t_windows, trip_windows, max_min, plot_type]
    return {"response": "animTrip"}


@app.post("/plots/animFFT", tags=["anim_fft"])
async def plot_fft_anim(request: dict = Body(...)):
    xf, fft_windows, max_min, plot_type = plt_api.anim_fft(request_information)
    return [xf, fft_windows, max_min, plot_type]


@app.post("/plots/animSIFFT", tags=["anim_si_fft"])
async def plot_si_fft_anim(request: dict = Body(...)):
    xf, si_fft_windows, max_min, plot_type = plt_api.anim_si_fft(request_information)
    
    return [xf, si_fft_windows, max_min, plot_type]


favicon_path = "public/static/favicon.ico"


# @app.get("/favicon.ico", include_in_schema=False)
# async def favicon():
#     return FileResponse(favicon_path)


app.mount("/", StaticFiles(directory="public", html=True), name="static")
