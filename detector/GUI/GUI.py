# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk, font
import getpass

""" Prueba 1"
# Prueba 1
# class App:
#     def __init__(self):
#         self.root = Tk()
#         self.root.geometry("300x200")
#         self.root.resizable(width=False, height=False)
#         self.root.title("Tesis")

#         self.tinfo = Text(self.root, width=40, height=10)
#         self.tinfo.pack(side=TOP)

#         self.binfo = ttk.Button(self.root, text="Info", command=self.see_info)
#         self.binfo.pack(side=LEFT)

#         self.bexit = ttk.Button(self.root, text="Exit", command=self.root.destroy)
#         self.bexit.pack(side=RIGHT)

#         self.binfo.focus_set()
#         self.root.mainloop()

#     def see_info(self):
#         self.tinfo.delete("1.0", END)

#         info1 = self.root.winfo_class()
#         info2 = self.root.winfo_geometry()
#         info3 = str(self.root.winfo_width())
#         info4 = str(self.root.winfo_height())
#         info5 = str(self.root.winfo_rootx())
#         info6 = str(self.root.winfo_rooty())
#         info7 = str(self.root.winfo_id())
#         info8 = self.root.winfo_name()
#         info9 = self.root.winfo_manager()

#         texto_info = f"Clase de 'root': {info1}\n"
#         texto_info += f"Resolución y posición: {info2}\n"
#         texto_info += f"Anchura ventana: {info3}\n"
#         texto_info += f"Altura ventana: {info4}\n"
#         texto_info += f"Pos. Ventana X: {info5}\n"
#         texto_info += f"Pos. Ventana Y: {info6}\n"
#         texto_info += f"Id. de 'root': {info7}\n"
#         texto_info += f"Nombre objeto: {info8}\n"
#         texto_info += f"Gestor ventanas: {info9}\n"

#         self.tinfo.insert("1.0", texto_info)
"""

# Geometría
""" Pack

# Pack
# class App:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Acceso")
#         fuente = font.Font(weight="bold")
#         self.etiq1 = ttk.Label(self.root, text="Usuario:", font=fuente)
#         self.etiq2 = ttk.Label(self.root, text="Contraseña:", font=fuente)

#         self.usuario = StringVar()
#         self.clave = StringVar()

#         self.usuario.set(getpass.getuser())

#         self.ctext1 = ttk.Entry(self.root, textvariable=self.usuario, width=30)
#         self.ctext2 = ttk.Entry(self.root, textvariable=self.clave, width=30, show="*")
#         self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)

#         self.btn1 = ttk.Button(self.root, text="Aceptar", command=self.aceptar)
#         self.btn2 = ttk.Button(self.root, text="Cancelar", command=quit)

#         self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
#         self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
#         self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
#         self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
#         self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
#         self.btn1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
#         self.btn2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

#         self.ctext2.focus_set()
#         self.root.mainloop()

#     def aceptar(self):
#         if self.clave.get() == "tkinter":
#             print("Acceso permitido")
#             print(f"Usuario: {self.ctext1.get()}")
#             print(f"Contraseña: {self.ctext2.get()}")
#         else:
#             print("Acceso denegado")

#         self.clave.set("")
#         self.ctext2.focus_set()
"""
""" Grid
# # Grid
# class App:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Access")

#         self.root.resizable(0, 0)
#         fuente = font.Font(weight="bold")

#         self.marco = ttk.Frame(
#             self.root, borderwidth=2, relief="raised", padding=(10, 10)
#         )
#         self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente, padding=(5, 5))
#         self.etiq2 = ttk.Label(
#             self.marco, text="Contraseña:", font=fuente, padding=(5, 5)
#         )

#         self.usuario = StringVar()
#         self.clave = StringVar()
#         self.usuario.set(getpass.getuser())
#         self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, width=30)
#         self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, show="*", width=30)
#         self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
#         self.btn1 = ttk.Button(
#             self.marco, text="Aceptar", padding=(5, 5), command=self.aceptar
#         )
#         self.btn2 = ttk.Button(
#             self.marco, text="Cancelar", padding=(5, 5), command=quit
#         )

#         self.marco.grid(column=0, row=0)
#         self.etiq1.grid(column=0, row=0)
#         self.ctext1.grid(column=1, row=0, columnspan=2)
#         self.etiq2.grid(column=0, row=1)
#         self.ctext2.grid(column=1, row=1, columnspan=2)
#         self.separ1.grid(column=0, row=3, columnspan=3)
#         self.btn1.grid(column=1, row=4)
#         self.btn2.grid(column=2, row=4)

#         self.ctext2.focus_set()
#         self.root.mainloop()

#     def aceptar(self):
#         if self.clave.get() == "tkinter":
#             print("Acceso permitido")
#             print(f"Usuario: {self.ctext1.get()}")
#             print(f"Contraseña: {self.ctext2.get()}")
#         else:
#             print("Acceso denegado")
#             self.clave.set("")
#             self.ctext2.focus_set()
"""
""" Grid Expandable
# Grid
# class App:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Access")

#         fuente = font.Font(weight="bold")

#         self.marco = ttk.Frame(
#             self.root, borderwidth=2, relief="raised", padding=(10, 10)
#         )
#         self.etiq1 = ttk.Label(self.marco, text="Usuario:", font=fuente, padding=(5, 5))
#         self.etiq2 = ttk.Label(
#             self.marco, text="Contraseña:", font=fuente, padding=(5, 5)
#         )

#         self.usuario = StringVar()
#         self.clave = StringVar()
#         self.usuario.set(getpass.getuser())
#         self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, width=30)
#         self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, show="*", width=30)
#         self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
#         self.btn1 = ttk.Button(
#             self.marco, text="Aceptar", padding=(5, 5), command=self.aceptar
#         )
#         self.btn2 = ttk.Button(
#             self.marco, text="Cancelar", padding=(5, 5), command=quit
#         )

#         self.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
#         self.etiq1.grid(column=0, row=0, sticky=(N, S, E, W))
#         self.ctext1.grid(column=1, row=0, columnspan=2, sticky=(E, W))
#         self.etiq2.grid(column=0, row=1, sticky=(N, S, E, W))
#         self.ctext2.grid(column=1, row=1, columnspan=2, sticky=(E, W))
#         self.separ1.grid(column=0, row=3, columnspan=3, sticky=(N, S, E, W))
#         self.btn1.grid(column=1, row=4, sticky=(E))
#         self.btn2.grid(column=2, row=4, sticky=(W))

#         self.root.columnconfigure(0, weight=1)
#         self.root.rowconfigure(0, weight=1)
#         self.marco.columnconfigure(0, weight=1)
#         self.marco.columnconfigure(1, weight=1)
#         self.marco.columnconfigure(2, weight=1)
#         self.marco.rowconfigure(0, weight=1)
#         self.marco.rowconfigure(1, weight=1)
#         self.marco.rowconfigure(4, weight=1)

#         self.ctext2.focus_set()
#         self.root.mainloop()

#     def aceptar(self):
#         if self.clave.get() == "tkinter":
#             print("Acceso permitido")
#             print(f"Usuario: {self.ctext1.get()}")
#             print(f"Contraseña: {self.ctext2.get()}")
#         else:
#             print("Acceso denegado")
#             self.clave.set("")
#             self.ctext2.focus_set()


# Place
"""
""" Geometry
# class App:
#     def __init__(self):

#         self.root = Tk()
#         self.root.geometry("430x200")
#         self.root.resizable(0, 0)
#         self.root.title("Acceso")
#         self.font = font.Font(weight="bold")

#         self.lbl1 = ttk.Label(self.root, text="Usuario: ", font=self.font)
#         self.lbl2 = ttk.Label(self.root, text="Contraseña: ", font=self.font)
#         self.msg = StringVar()
#         self.lbl3 = ttk.Label(
#             self.root, textvariable=self.msg, font=self.font, foreground="blue"
#         )

#         self.user = StringVar()
#         self.pswd = StringVar()
#         self.user.set(getpass.getuser())
#         self.ctext1 = ttk.Entry(self.root, textvariable=self.user, width=30)
#         self.ctext2 = ttk.Entry(self.root, textvariable=self.pswd, width=30, show="*")
#         self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)
#         self.btn1 = ttk.Button(
#             self.root, text="Aceptar", padding=(5, 5), command=self.aceptar
#         )
#         self.btn2 = ttk.Button(self.root, text="Cancelar", padding=(5, 5), command=quit)

#         self.lbl1.place(x=30, y=40)
#         self.lbl2.place(x=30, y=80)
#         self.lbl3.place(x=150, y=120)
#         self.ctext1.place(x=150, y=42)
#         self.ctext2.place(x=150, y=82)
#         self.separ1.place(x=5, y=145, bordermode=OUTSIDE, height=10, width=420)
#         self.btn1.place(x=170, y=160)
#         self.btn2.place(x=290, y=160)
#         self.ctext2.focus_set()
#         self.ctext2.bind("<Button-1>", self.erase_msg)
#         self.root.mainloop()

#     def aceptar(self):
#         if self.pswd.get() == "tkinter":
#             self.lbl3.configure(foreground="blue")
#             self.msg.set("Acceso permitido")
#         else:
#             self.lbl3.configure(foreground="red")
#             self.msg.set("Acceso denegado")

#     def erase_msg(self, evento):
#         self.pswd.set("")
#         self.msg.set("")
"""


class Scrollbar:
    def __init__(self):
        self.root = Tk()
        self.sb = ttk.Scrollbar(self.root)
        self.sb.pack(side=RIGHT, fill=Y)
        self.my_list = Listbox(self.root, yscrollcommand=self.sb.set)
        for line in range(30):
            self.my_list.insert(END, f"Number: {line}")

        self.my_list.pack(side=LEFT)
        self.sb.config(command=self.my_list.yview)
        self.root.mainloop()


class AppNoModal:
    ventana = 0
    posx_y = 0

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x200+500+50")
        self.root.resizable(0, 0)
        self.root.title("Ventana de aplicación")

        btn = ttk.Button(self.root, text="Abrir", command=self.open)
        btn.pack(side=TOP, padx=20, pady=20)
        btn2 = ttk.Button(self.root, text="Cerrar", command=self.root.destroy)
        btn2.pack(side=BOTTOM, padx=20, pady=20)
        self.root.mainloop()

    def open(self):
        self.dialog = Toplevel()
        App.ventana += 1
        App.posx_y += 50
        tamypos = f"200x100+{App.posx_y}+{App.posx_y}"
        self.dialog.geometry(tamypos)
        self.dialog.resizable(0, 0)
        ident = self.dialog.winfo_id()
        title = f"{App.ventana}: {ident}"
        self.dialog.title(title)
        btn = ttk.Button(self.dialog, text="Cerrar", command=self.dialog.destroy)
        btn.pack(side=BOTTOM, padx=20, pady=20)
        self.root.wait_window(self.dialog)


class AppModal:
    ventana = 0
    posx_y = 0

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x200+500+50")
        self.root.resizable(0, 0)
        self.root.title("Ventana de aplicación")
        btn = ttk.Button(self.root, text="Open", command=self.open)
        btn.pack(side=BOTTOM, padx=20, pady=20)
        btn2 = ttk.Button(self.root, text="No modal", command=self.open2)
        btn2.pack(side=BOTTOM, padx=20, pady=20)
        self.root.mainloop()

    def open(self):
        self.dialog = Toplevel()
        App.ventana += 1
        App.posx_y += 50
        tamypos = f"200x100+{App.posx_y}+{App.posx_y}"
        self.dialog.geometry(tamypos)
        self.dialog.resizable(0, 0)
        ident = self.dialog.winfo_id()
        title = f"{App.ventana}: {ident}"
        self.dialog.title(title)
        btn = ttk.Button(self.dialog, text="Close", command=self.dialog.destroy)
        btn.pack(side=BOTTOM, padx=20, pady=20)
        self.dialog.transient(master=self.root)
        self.dialog.grab_set()
        self.root.wait_window(self.dialog)

    def open2(self):
        self.dialog2 = Toplevel()
        App.ventana += 1
        App.posx_y += 50
        tamypos = f"200x100+{App.posx_y}+{App.posx_y}"
        self.dialog2.geometry(tamypos)
        self.dialog2.resizable(0, 0)
        ident = self.dialog2.winfo_id()
        title = f"{App.ventana}: {ident}"
        btn = ttk.Button(self.dialog2, text="Close", command=self.dialog2.destroy)
        btn.pack(side=BOTTOM, padx=20, pady=20)
        self.root.wait_window(self.dialog2)


import os


class AppPost:
    def __init__(self):
        self.root = Tk()
        self.root.title("High Speed")

        # Variables de control
        self.num_via = IntVar(value=1)
        self.ida_vue = BooleanVar()
        self.clase = StringVar(value="t")
        self.km = IntVar(value=1)
        self.precio = DoubleVar(value=0.10)
        self.total = DoubleVar(value=0.0)
        abs_path = os.path.dirname(os.path.realpath(__file__))
        abs_path_img = os.path.join(abs_path, "CM_formulacion1.png")
        tren = PhotoImage(file=abs_path_img)
        # tren = tren.zoom(10)
        # tren = tren.subsample(10)
        self.img1 = ttk.Label(self.root, image=tren, anchor="center")
        self.lbl1 = ttk.Label(self.root, text="Viajeros:")
        self.viaje = Spinbox(
            self.root,
            from_=1,
            to=20,
            wrap=True,
            textvariable=self.num_via,
            state="readonly",
        )
        self.idavue = ttk.Checkbutton(
            self.root,
            text="Ida y vuelta",
            variable=self.ida_vue,
            onvalue=True,
            offvalue=False,
        )
        self.lbl2 = ttk.Label(self.root, text="Clase:")
        self.clase1 = ttk.Radiobutton(
            self.root, text="Turista", variable=self.clase, value="t"
        )
        self.clase2 = ttk.Radiobutton(
            self.root, text="Primera", variable=self.clase, value="p"
        )
        self.clase3 = ttk.Radiobutton(
            self.root, text="Deluxe", variable=self.clase, value="l"
        )
        self.lbl3 = ttk.Label(self.root, text="Distancia en km:")
        self.dist = ttk.Entry(self.root, textvariable=self.km, width=10)
        self.lbl4 = ttk.Label(self.root, text="Precio:")
        self.coste = ttk.Entry(self.root, textvariable=self.precio, width=10)
        self.lbl5 = ttk.Label(self.root, text="A pagar (euros):")
        self.lbl6 = ttk.Label(
            self.root,
            textvariable=self.total,
            foreground="yellow",
            background="black",
            borderwidth=5,
            anchor="e",
        )
        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)
        self.btn1 = ttk.Button(self.root, text="Calcular", command=self.calcular)
        self.btn2 = ttk.Button(self.root, text="Salir", command=quit)

        self.img1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.lbl1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.viaje.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.idavue.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.clase1.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.clase2.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.clase3.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.dist.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.coste.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.lbl6.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.btn1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.btn2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.root.mainloop()

    def calcular(self):
        error_dato = False
        total = 0
        try:
            km = int(self.km.get())
            precio = float(self.precio.get())
        except:
            error_dato = True
        if not error_dato:
            total = self.num_via.get() * km * precio
            if self.ida_vue.get():
                total = total * 1.5
            if self.clase.get() == "p":
                total = total * 1.2
            elif self.clase.get() == "l":
                total = total * 2
            self.total.set(total)
        else:
            self.total.set("¡ERROR!")


class AppInm:
    def __init__(self):
        self.root = Tk()
        self.root.title("High Speed")

        # Variables de control
        self.num_via = IntVar(value=1)
        self.ida_vue = BooleanVar()
        self.clase = StringVar(value="t")
        self.km = IntVar(value=1)
        self.precio = DoubleVar(value=0.10)
        self.total = DoubleVar(value=0.0)

        self.km.trace("w", self.calcular)
        self.precio.trace("w", self.calcular)
        self.calcular()

        abs_path = os.path.dirname(os.path.realpath(__file__))
        abs_path_img = os.path.join(abs_path, "CM_formulacion1.png")
        tren = PhotoImage(file=abs_path_img)
        # tren = tren.zoom(10)
        # tren = tren.subsample(10)
        self.img1 = ttk.Label(self.root, image=tren, anchor="center")
        self.lbl1 = ttk.Label(self.root, text="Viajeros:")
        self.viaje = Spinbox(
            self.root,
            from_=1,
            to=20,
            wrap=True,
            textvariable=self.num_via,
            state="readonly",
        )
        self.idavue = ttk.Checkbutton(
            self.root,
            text="Ida y vuelta",
            variable=self.ida_vue,
            onvalue=True,
            offvalue=False,
        )
        self.lbl2 = ttk.Label(self.root, text="Clase:")
        self.clase1 = ttk.Radiobutton(
            self.root, text="Turista", variable=self.clase, value="t"
        )
        self.clase2 = ttk.Radiobutton(
            self.root, text="Primera", variable=self.clase, value="p"
        )
        self.clase3 = ttk.Radiobutton(
            self.root, text="Deluxe", variable=self.clase, value="l"
        )
        self.lbl3 = ttk.Label(self.root, text="Distancia en km:")
        self.dist = ttk.Entry(self.root, textvariable=self.km, width=10)
        self.lbl4 = ttk.Label(self.root, text="Precio:")
        self.coste = ttk.Entry(self.root, textvariable=self.precio, width=10)
        self.lbl5 = ttk.Label(self.root, text="A pagar (euros):")
        self.lbl6 = ttk.Label(
            self.root,
            textvariable=self.total,
            foreground="yellow",
            background="black",
            borderwidth=5,
            anchor="e",
        )
        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL)
        self.btn1 = ttk.Button(self.root, text="Calcular", command=self.calcular)
        self.btn2 = ttk.Button(self.root, text="Salir", command=quit)

        self.img1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.lbl1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.viaje.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.idavue.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.clase1.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.clase2.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.clase3.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.dist.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.coste.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.lbl5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.lbl6.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.btn1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.btn2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.root.mainloop()

    def calcular(self, *args):
        error_dato = False
        total = 0
        try:
            km = int(self.km.get())
            precio = float(self.precio.get())
        except:
            error_dato = True
        if not error_dato:
            total = self.num_via.get() * km * precio
            if self.ida_vue.get():
                total = total * 1.5
            if self.clase.get() == "p":
                total = total * 1.2
            elif self.clase.get() == "l":
                total = total * 2
            self.total.set(total)
        else:
            self.total.set("¡ERROR!")


# PyRemote
class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x200")
        self.root.configure(background="beige")
        self.root.resizable(0, 0)
        self.root.mainloop()


def main():
    my_app = App()
    return 0


if __name__ == "__main__":
    main()


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("App Tesis")
        # self.root.resizable(1, 1)
        self.root.geometry("600x600")
        # self.root.configure(background="beige")
        self.frame = Frame(self.root, width=300, height=300)
        self.frame.pack(expand=True, fill=BOTH)

        self.canvas = Canvas(
            self.frame,
            bg="#FFFFFF",
            width=300,
            height=300,
            scrollregion=(0, 0, 500, 500),
        )
        # Scrollbar
        self.hbar = Scrollbar(self.frame, orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.hbar.config(command=self.canvas.xview)
        self.vbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.canvas.yview)

        self.canvas.config(width=300, height=300)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)

        self.btn1 = ttk.Button(self.canvas, text="Load CSV", command=self.load_csv)
        self.btn1.pack(side=BOTTOM, padx=20, pady=20)
        self.signal = StringVar()
        self.rb_list = Listbox(self.canvas, yscrollcommand=self.hbar.set)
        self.root.mainloop()

    def load_csv(self):
        try:
            signals = CSV_pandas()
        except:
            print("Try Again")
        signals = signals.labels_list
        for signal in signals:
            button = ttk.Radiobutton(
                self.canvas,
                text=signal,
                variable=self.signal,
                value=signal,
                command=self.sel,
            )
            button.pack(side=TOP)
        self.canvas_update()

    def canvas_update(self):
        self.vbar.configure(scrollregion=self.canvas.bbox("all"))

    def sel(self):
        print(f"Selected option: {self.signal.get()}")
