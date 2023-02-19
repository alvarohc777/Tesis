from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from utils_tesis.signalload import CSV_pandas_path
import utils_tesis.plot_api as plt_api
from pydantic import BaseModel

api =NinjaAPI()

class SignalName(BaseModel):
    # csv_name: str
    signal_name: str

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

    
@api.post("/signalName")
async def post_signal_name(request, load: SignalName):
    signal_name = load.signal_name
    # signals = request_information["signals"]
    request_information["signal_name"] = signal_name

    return {"response": signal_name}

@api.post("/plots/imgSignal")
async def plot_signal(request: dict = Body(...)):

    t, signal, line_shape, plot_type = plt_api.img_signal(request_information)
    print(plot_type)
    return [t, signal, line_shape, plot_type]