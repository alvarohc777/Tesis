import re
import os
import csv


PATH = "C:\\Users\\aherrada\\OneDrive - Universidad del Norte\\Uninorte\\DetectionDataBase\\septDataBaseCSV\\Caps"
casos = os.listdir(PATH)
print(casos)

for caso in casos:
    with open(f"{PATH}\\{caso}", "rU") as f:
        reader = csv.reader(f, delimiter=",")
        writer = csv.writer(open(f"{PATH}\\n{caso}", "w"), delimiter=";")
        writer.writerows(reader)
        print("delimiter succesfully changed")
# Modificar el Script para hacerlo una función con una API para:
# aceptar cualquier PATH (crear una clase para cargue de CSV)
# entregue el delimitador del CSV
# preguntar por qué delimitador cambiarlo.
