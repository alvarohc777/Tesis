from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import codecs
import csv
from utils.signalload import CSV_pandas_path
import json

app = FastAPI()
origins = [
    "null",
    "http://localhost:80",
    "http://127.0.0.1:80"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods =['*'],
    allow_headers=['*']
)




@app.get('/', tags=['ROOT'])
async def root() -> dict:
    return {'ping': 'pong'}

dict_prueba = [
    {"id": "1",
    "info": "jugar"},
    {
    "id": "2",
    "info": "study"
    }
]

csv_file_name = None

@app.get("/info", tags=['info'])
async def get_info() -> dict:
    return {"data": dict_prueba}

@app.get("/info/{id}", tags=['info'])
async def get_info_id(id:int) -> dict:
    for prueba in dict_prueba:
        if int((prueba['id'])) == id:
            return {
                "data": prueba,
            }
    return {
        "data": f"No se encontró la información"
    }
    
csv_file = 0
@app.post('/uploadCSV', tags=['CSV'])
async def post_CSV(csv_files: UploadFile = File(...), nombre = File(...)) ->dict:
    
    with open(csv_files.filename, 'wb+') as f:
        f.write(csv_files.file.read())
    print(type(csv_files))
    csv_file_name = csv_files.filename
    print(f"csv filename: {csv_file_name}")
    signals = CSV_pandas_path(csv_file_name)
    print(signals.labels_list)

    return {
        'signal_list': signals.labels_list,
        'file_name': csv_file_name
    }



# # signals = CSV_pandas_path().labels_list
# # print(type(signals))
# @app.get('/signal_list', tags=['signals'])
# async def get_signal_list() -> dict:
#     return {'signals': signals}