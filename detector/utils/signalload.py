from tkinter import filedialog
import tkinter as tk
import numpy as np
import pandas as pd
import csv


class CSV:
    def __init__(self):
        self.csv_load()

    def csv_load(self):
        """Creación de la ventana para selección de archivo CSV"""
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        root.lift()
        # try:
        #     self.path, *self._ = filedialog.askopenfilename(
        #         multiple=False,
        #         title="cargue CSV",
        #         filetypes=(("archivos CSV", "*.csv"),),
        #     )
        # except ValueError:
        #     raise SystemExit

        self.path = filedialog.askopenfilename(
            multiple=False,
            title="cargue CSV",
            filetypes=(("archivos CSV", "*.csv"),),
        )
        print(self.path)

        self.nombre = self.path[self.path.rfind("/") + 1 :]
        self.nombre = self.nombre.replace(".csv", "")
        print(f"Se seleccionó {self.nombre}")
        root.destroy()
        self.extraer_csv()

    def extraer_csv(self):
        """Extracción de características del CSV, esto se realiza automáticamente"""
        with open(self.path, "r") as f:
            header = next(f)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(header).delimiter

        df = pd.read_csv(self.path, delimiter=delimiter)
        xy = df.to_numpy()[2:, :].astype(float)
        if len(xy) % 2 == 0:
            N = len(xy)
        else:
            N = len(xy) - 1
        xy = xy[:N:8]
        self.t = xy[:, 0]
        self.tf = max(self.t)
        self.ti = self.t[0]
        self.fs = int((len(self.t) - 1) / (self.tf - 0))
        self.dt = 1 / self.fs

        try:
            self.R01Ia = xy[:, 22]
            self.R01Va = xy[:, 1]
            self.R01Vb = xy[:, 2]
            self.R01Vc = xy[:, 3]
            self.R10Va = xy[:, 1]
            self.R10Vb = xy[:, 2]
            self.R10Vc = xy[:, 3]
            self.R15Va = xy[:, 1]
            self.R15Vb = xy[:, 2]
            self.R15Vc = xy[:, 3]
            self.R01Ib = xy[:, 23]
            self.R01Ic = xy[:, 24]
            self.R10Ia = xy[:, 25]
            self.R10Ib = xy[:, 26]
            self.R10Ic = xy[:, 27]
            self.R15Ia = xy[:, 28]
            self.R15Ib = xy[:, 29]
            self.R15Ic = xy[:, 30]
        except:
            self.Va = xy[:, 1]
            self.Vb = xy[:, 2]
            self.Vc = xy[:, 3]
            self.Ia = xy[:, 4]
            self.Ib = xy[:, 5]
            self.Ic = xy[:, 6]

class CSV_pandas(CSV):
    def extraer_csv(self):
        with open(self.path, "r") as f:
            header = next(f)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(header).delimiter
        print(delimiter)
        df = pd.read_csv(self.path, delimiter=";")
        # Obtener un número par de muestras
        if len(df) % 2 != 0:
            df.drop(df.tail(1).index, inplace=True)

        df.columns = df.columns.str.replace(" ", "")
        pattern = r"^b'([\w ]*)'"

        node_from = df.iloc[0].str.replace(pattern, r"\1", regex=True).str.strip()
        node_to = df.iloc[1].str.replace(pattern, r"\1", regex=True).str.strip()
        df = df.drop(index=0)
        df = df.drop(index=1)

        df.columns = df.columns.str.replace(r"(V|I)[.\w-]*", r"\1", regex=True)
        df.columns = df.columns.str.replace("\d*\.*\d+", r"Model", regex=True)

        # Extraer si la medición es V, I o models; borrar si es Model
        labels_list = df.columns.values.tolist()
        # labels_list = [s.replace('Model','') for s in labels_list]

        # convertir los labels de cada nodo a una lista
        node_from_list = node_from.values.tolist()
        node_to_list = node_to.values.tolist()

        self.labels_list = self.new_labels(node_from_list, node_to_list, labels_list)
        df.columns = self.labels_list
        self.df = df.reset_index(drop=True)
    
        # for label in self.labels_list[1:]:
        #     exec(f"self.{label} = '{label}'")

    def relay_list(self, currents=True, voltages=False, Models=False):
        for i in self.labels_list:
            if ("V:" in i) and voltages:
                print(i)
            elif ("I:" in i) and currents:
                print(i)
            elif Models:
                print(i)
    
    # función para devolver la lista de labels correcta
    def new_labels(self, list1, list2, labels):
        final_list = []
        for x, y, z in zip(list1, list2, labels):
            if y == "":
                final_list.append(f"{z}: {x}")
            elif z == "Model":
                final_list.append(f"{x}: {y}")
            else:
                final_list.append(f"{z}: {x}-{y}")
        return final_list
    
    def load_data(self, relay_name):
        pass
        



class CSV_prueba(CSV):
    def __init__(self):
        self.csv_load()

    def csv_load(self):
        self.path = "C:\\Users\\aherrada\\OneDrive - Universidad del Norte\\Uninorte\\DetectionDataBase\\septDataBaseCSV\\Fallas\\Fault01_B112_RF1e-05.csv"
        self.nombre = self.path[self.path.rfind("/") + 1 :]
        self.nombre = self.nombre.replace(".csv", "")
        print(f"Se seleccionó {self.nombre}")
        self.extraer_csv()


class CSV_PATH(CSV):
    def __init__(self, PATH):
        self.path = PATH
        self.extraer_csv()


def synthetic_signal(t, harmonics=[60], fundamental=60):
    """
    Function for the creation of a synthetic signal



    Returns
    -------
    numpy.array
        (3, n) three phase matrix
    """
    wt = 2 * np.pi * fundamental * t
    ang_A = float(0) * np.pi / 180
    ang_B = float(240) * np.pi / 180
    ang_C = float(120) * np.pi / 180

    A, B, C = 0, 0, 0

    for s in harmonics:
        n = s / fundamental
        A += 100 * np.sin(n * (wt + ang_A))
        B += 100 * np.sin(n * (wt + ang_B))
        C += 100 * np.sin(n * (wt + ang_C))

    return np.array((A, B, C))


class SyntheticSignal:
    """Creates a synthetic signal"""

    def __init__(
        self, samples_cycle=64, cycles=4, frequency_components=[60, 120]
    ) -> None:
        """Constructor of the signal

        Parameters
        ----------

        samples_cycle: int
            Number of samples in a period of the signal.

        cycles: int
            Number of cycles of the signal.

        frequency_components: list
            List containing frequencies (int) in the signal.
        """
        self.dt = 1 / (60 * samples_cycle)
        self.t = np.arange(0, cycles / 60, self.dt)
        self.tf = self.t[-1]
        self.fs = int(1 / self.dt)
        wt = 2 * np.pi * 60 * self.t
