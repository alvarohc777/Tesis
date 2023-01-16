from tkinter import *
from tkinter import ttk
from utils.signalload import CSV_pandas


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tesis")
        self.root.geometry("300x200")
        self.root.resizable(0, 0)

        self.CSV_file = StringVar()
        self.signal = StringVar()

        self.btn1 = ttk.Button(self.root, text="Load CSV", command=self.load_csv)
        self.sb = ttk.Scrollbar(self.root)
        self.rb_list = Listbox(self.root, yscrollcommand=self.sb.set)

        self.btn1.pack(side=BOTTOM)
        self.sb.pack(side=RIGHT, fill=Y)

        # self.rb_list.config(yscrollcommand=self.sb.set)
        self.rb_list.pack(side=TOP)

        self.root.mainloop()

    def load_csv(self):
        try:
            signals = CSV_pandas()
        except:
            print("Try Again")
            return
        signals = signals.labels_list
        for signal in signals:
            button = ttk.Radiobutton(
                self.rb_list,
                text=signal,
                variable=self.signal,
                value=signal,
                command=self.sel,
            )
            button.pack(side=TOP)
        self.sb.config(command=self.rb_list.yview)

    def sel(self):
        print(f"selected option: {self.signal.get()}")


def main():
    app = App()
    return 0


if __name__ == "__main__":
    main()
