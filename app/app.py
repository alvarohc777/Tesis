from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from utils.signalload import CSV_pandas_path
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
    request_information["filename"] = csv_files.filename
    request_information["csv"] = signals
    print(type(csv_files))
    print(f"csv filename: {csv_file_name}")
    return {"signals_list": signals.labels_list, "file_name": csv_file_name}


@app.post("/signalName", tags=["CSV"])
async def post_signal_name(load: SignalName) -> dict:
    request_information["signal_name"] = load.signal_name
    print(request_information["signal_name"])
    print(request_information["filename"])
    print(type(request_information["csv"]))
    return {
        "signal_name": load.signal_name,
        "filename": request_information["filename"],
    }


@app.post("/plotsList", tags=["Plots"])
async def post_plots_list(request: dict = Body(...)):
    return request
