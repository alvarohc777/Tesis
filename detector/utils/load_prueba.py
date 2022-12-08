import pandas as pd


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


path = "C:\\Users\\aherrada\\OneDrive - Universidad del Norte\\Uninorte\\DetectionDataBase\\septDataBaseCSV\\Fallas\\Fault01_B112_RF40.csv"
df = pd.read_csv(path, delimiter=";")
df.columns = df.columns.str.replace(" ", "")

# df[0:1] = df[0:1].str.decore("utf-8")
# df.columns = df.columns.str.decode("utf-8")

pattern = r"^b'([\w ]*)'"

node_from = df.iloc[0].str.replace(pattern, r"\1", regex=True)
node_to = df.iloc[1].str.replace(pattern, r"\1", regex=True)
df = df.drop(index=0)
df = df.drop(index=1)


# Obtener un número par de muestras
if len(df) % 2 != 0:
    df.drop(df.tail(1).index, inplace=True)

# df.columns = df.columns.str.replace(r"^(\d)*(V|I)*", )

# Cambiar los nombres de los medidores de corriente y voltaje
df.columns = df.columns.str.replace(r"(V|I)[.\w-]*", r"\1", regex=True)
df.columns = df.columns.str.replace("\d*\.*\d+", r"Model", regex=True)

a = df.columns[1:]
node_from["new"] = ""
node_from["new"] = a

# node_from = node_from.str.cat(node_to, sep="")


# print(df.head())
# print(node_from)
