from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from utils.signalload import CSV_pandas_path
from utils.plot_funcs import signal_plt
import matplotlib.pyplot as plt
import numpy as np

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


@app.post("/plotsList", tags=["Plots"])
async def post_plots_list(request: dict = Body(...)):
    signal = request_information["signal"].tolist()
    t = request_information["t"].tolist()

    return [t, signal]


@app.post("plots/imgSignal")








