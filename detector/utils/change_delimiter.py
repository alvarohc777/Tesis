import re
import os
import csv


PATH = "C:\\Users\\aherrada\\OneDrive - Universidad del Norte\\Uninorte\\DetectionDataBase\\MedioCiclo\\"
file = "IEEE34_F01.csv"
# casos = os.listdir(PATH)
# print(casos)

# for caso in casos:
#     # with open(f"{PATH}\\{caso}", "rU") as f:
#     with open(PATH, "rU") as f:
#         reader = csv.reader(f, delimiter=",")
#         writer = csv.writer(open(f"{PATH}\\n{caso}", "w"), delimiter=";")
#         writer.writerows(reader)
#         print("delimiter succesfully changed")

with open(f"{PATH}\\{file}", "rU") as f:
    reader = csv.reader(f, delimiter=",")
    writer = csv.writer(open(f"{PATH}\\new_{file}", "w"), delimiter=";")
    writer.writerows(reader)
    print("delimiter succesfully changed")
# Modificar el Script para hacerlo una función con una API para:
# aceptar cualquier PATH (crear una clase para cargue de CSV)
# entregue el delimitador del CSV
# preguntar por qué delimitador cambiarlo.
