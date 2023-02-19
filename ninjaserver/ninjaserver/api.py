from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from utils_tesis.signalload import CSV_pandas_path
api =NinjaAPI()

@api.get('/hello')
def hello(request):
    return "Hello World"


# Variables
request_information = {}

@api.post('/uploadCSV')
def post_CSV(request, csv_files: UploadedFile = File(...)):
    with open(csv_files.name, "wb+") as f:
        f.write(csv_files.file.read())
    request_information.clear()
    request_information["plots"] = {}
    csv_file_name = csv_files.name
    signals = CSV_pandas_path(csv_file_name)

    request_information["filename"] = csv_file_name
    request_information["signals"] = signals
    request_information["window_length"] = 64
    request_information["step"] = 4

    print(f"csv filename: {csv_file_name}")

    return {"signals_list": signals.labels_list, "file_name": csv_file_name}

    



# @app.post("/uploadCSV", tags=["CSV"])
# async def post_CSV(csv_files: UploadFile = File(...)) -> dict:
#     with open(csv_files.filename, "wb+") as f:
#         f.write(csv_files.file.read())
#     request_information.clear()
#     request_information["plots"] = {}
#     csv_file_name = csv_files.filename
#     signals = CSV_pandas_path(csv_file_name)

#     request_information["filename"] = csv_file_name
#     request_information["signals"] = signals
#     request_information["window_length"] = 64
#     request_information["step"] = 4

#     print(f"csv filename: {csv_file_name}")

#     return {"signals_list": signals.labels_list, "file_name": csv_file_name}