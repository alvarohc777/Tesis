# import pandas as pd

# # función para devolver la lista de labels correcta
# def new_labels(list1, list2, labels):
#     final_list = []
#     for x, y, z in zip(list1, list2, labels):
#         if y == "":
#             final_list.append(f"{z}: {x}")
#         elif z == "Model":
#             final_list.append(f"{x}: {y}")
#         else:
#             final_list.append(f"{z}: {x}-{y}")
#     return final_list


# path = "C:\\Users\\aherrada\\OneDrive - Universidad del Norte\\Uninorte\\DetectionDataBase\\septDataBaseCSV\\Fallas\\Fault01_B112_RF40.csv"
# df = pd.read_csv(path, delimiter=";")
# # Obtener un número par de muestras
# if len(df) % 2 != 0:
#     df.drop(df.tail(1).index, inplace=True)

# df.columns = df.columns.str.replace(" ", "")
# pattern = r"^b'([\w ]*)'"

# node_from = df.iloc[0].str.replace(pattern, r"\1", regex=True).str.strip()
# node_to = df.iloc[1].str.replace(pattern, r"\1", regex=True).str.strip()
# df = df.drop(index=0)
# df = df.drop(index=1)

# df.columns = df.columns.str.replace(r"(V|I)[.\w-]*", r"\1", regex=True)
# df.columns = df.columns.str.replace("\d*\.*\d+", r"Model", regex=True)

# # Extraer si la medición es V, I o models; borrar si es Model
# labels_list = df.columns.values.tolist()
# # labels_list = [s.replace('Model','') for s in labels_list]

# # convertir los labels de cada nodo a una lista
# node_from_list = node_from.values.tolist()
# node_to_list = node_to.values.tolist()

# labels_list = new_labels(node_from_list, node_to_list, labels_list)
# df.columns = labels_list
# df = df.reset_index(drop=True)
# # print(df.head(5))


# def print_relays(labels_list, currents=True, voltages=False, Models=False):

#     for i in labels_list:
#         if ("V:" in i) and voltages:
#             print(i)
#         elif ("I:" in i) and currents:
#             print(i)
#         elif Models:
#             print(i)

from signalload import CSV_pandas

signal = CSV_pandas()
# print(dir(signal))
# print(signal.I_X0004A_X0009A)
signal.relay_list()
