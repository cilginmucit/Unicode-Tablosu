import tkinter as tk
import tkinter.ttk as ttk
import unicodedata

class UnicodeTable:
    def __init__(self, root:tk.Tk, lengdis:int=40, end:int=65536): #For Windows 11 with 1080p resolution and 100% zoom, the maximum value is lengdis:int = 59, but the optimal value is lengdis:int = 40
        self.root:tk.Tk = root
        self.lengdis = lengdis
        self.bolum = 0
        self.end = end
        
        self.xtext = ""
        self.ytext = ""
        self.ztext = ""
        
        self.init_ui()
        self.populate_data()
        self.update_bolum(0)
        
    def init_ui(self):
        self.root.title("Unicode Tablosu")
        
        self.x = tk.Label(self.root)
        self.x.grid(column=1, row=1, sticky="news")

        self.y = tk.Label(self.root)
        self.y.grid(column=3, row=1, sticky="news")

        self.z = tk.Label(self.root)
        self.z.grid(column=5, row=1, sticky="news")

        self.dividers:list[tk.Label] = []
        for col in [0, 2, 4, 6]:
            divider = tk.Label(self.root, text="|\n")
            divider.grid(column=col, row=1, sticky="news")
            self.dividers.append(divider)
        
        self.dividers[0].grid_configure(padx=[10,0])
        self.dividers[3].grid_configure(padx=[0,10])

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(2, weight=0)
        self.root.columnconfigure(4, weight=0)
        self.root.columnconfigure(6, weight=0)

        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(5, weight=1)

        self.root.rowconfigure(1, weight=1)

        self.b_up =   ttk.Button(self.root, text="↑", command=self.scroll_up)
        self.b_down = ttk.Button(self.root, text="↓", command=self.scroll_down)

        self.b_up.grid(  column=0, row=0, sticky="news", columnspan=7,padx=[10,10],pady=[10,10])
        self.b_down.grid(column=0, row=2, sticky="news", columnspan=7,padx=[10,10],pady=[10,10])

    def populate_data(self):
        for i in range(((self.end // self.lengdis) + 1) * self.lengdis):
            if self.end > i:
                char = chr(i)
                try:
                    name = unicodedata.name(char)
                except ValueError:
                    name = f"CONTROL-{i}"
                self.xtext += f"{i}\n"
                self.ytext += f"{repr(char)}\n"
                self.ztext += f"{name}\n"
            else:
                self.xtext += "\n"
                self.ytext += "\n"
                self.ztext += "\n"

    def update_bolum(self, start):
        t1_original = self.xtext.split("\n")
        t2_original = self.ytext.split("\n")
        t3_original = self.ztext.split("\n")


        t1 = t1_original[start:start + self.lengdis]
        t2 = t2_original[start:start + self.lengdis]
        t3 = t3_original[start:start + self.lengdis]


        t4 = 1.5
        t5 = 2.4
        self.x.config(text="Sayı\n"     + "-" * int(t4 * len(max(t1_original, key=len))) + "\n" + "\n".join(t1))
        self.y.config(text="Karekter\n" + "-" * int(t5 * len(max(t2_original, key=len))) + "\n" + "\n".join(t2))
        self.z.config(text="İsim\n"     + "-" * int(t4 * len(max(t3_original, key=len))) + "\n" + "\n".join(t3))

        for divider in self.dividers:
            divider.config(text="|\n" * (self.lengdis + 1) + "|")

    def scroll_up(self):
        if self.bolum < self.lengdis:
            return
        self.bolum -= self.lengdis
        self.update_bolum(self.bolum)

    def scroll_down(self):
        if self.bolum + self.lengdis > self.end:
            return
        self.bolum += self.lengdis
        self.update_bolum(self.bolum)


if __name__ == "__main__":
    root = tk.Tk()
    app = UnicodeTable(root)
    root.mainloop()
