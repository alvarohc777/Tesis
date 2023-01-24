from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.signalload import CSV_pandas_path

app = FastAPI()
origins = ["null", "http://localhost:8080", "http://127.0.0.1:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Variables
csv_file_name = None


@app.get("/", tags=["HomePage"])
async def root() -> dict:
    return {"ping": "pong"}


@app.post("/uploadCSV", tags=["CSV"])
async def post_CSV(csv_files: UploadFile = File(...), file_type=File(...)) -> dict:
    with open(csv_files.filename, "wb+") as f:
        f.write(csv_files.file.read())
    print(type(csv_files))
    csv_file_name = csv_files.filename
    print(f"csv filename: {csv_file_name}")
    signals = CSV_pandas_path(csv_file_name)
    print(signals.labels_list)
    return {"signals_list": signals.labels_list, "file_name": csv_file_name}
