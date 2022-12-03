import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog


class CSV:
    def __init__(self):
        self.csv_load()

    def csv_load(self):
        """Creación de la ventana para selección de archivo CSV"""
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        root.lift()
        (self.path, *self._) = filedialog.askopenfilenames(
            multiple=False,
            title="cargue CSV",
            filetypes=(("archivos CSV", "*.csv"),),
        )
        self.nombre = self.path[self.path.rfind("/") + 1 :]
        self.nombre = self.nombre.replace(".csv", "")
        print(f"Se seleccionó {self.nombre}")
        root.destroy()
        self.extraer_csv()

    def extraer_csv(self):
        """Extracción de características del CSV, esto se realiza automáticamente"""

        df = pd.read_csv(self.path, delimiter=";")
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
