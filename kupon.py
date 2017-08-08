#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'czarek'

from tkinter import *
#from tkinter.ttk import *

print(TkVersion)


class Dyscyplina(Button):
    """Pojedyncza kratka z liczbą"""
    aktywny = 0
    ilosc = 0

    def zmien_aktywnosc(self, zezwolenie):
        if (self.aktywny == 0 and zezwolenie):
            self.aktywny = 1
            self.configure(bg="green")
        else:
            self.aktywny = 0
            self.configure(bg="gray85")


class Zaklad(Frame):
    """Pojedynczy zakład (kratka 7x7"""

    def __init__(self, master, ile=6, do=49):
        super().__init__(master, bd=4, bg='green')
        self.z = []
        self.do = do
        self.ile = ile
        for liczba in range(0, do):
            c = liczba // 7
            r = liczba % 7
            self.z.append(Dyscyplina(self, text=str(liczba + 1), borderwidth=1, padx=5, pady=2, height=1, width=1))
            self.z[liczba].grid(row=r, column=c)
            self.z[liczba]["command"] = lambda x=liczba: self.dupka(x)
            self.pack()

    def dupka(self, k):
        print("dupa", k + 1)
        i = self.ile_obstawionych()
        print("obstaw ", i)
        self.z[k].zmien_aktywnosc(i < self.ile)

    def ile_obstawionych(self):
        ile = 0
        for liczba in range(0, self.do):
            ile = ile + self.z[liczba].aktywny
        return (ile)


class Kupon(Frame):
    """kupon zawiera 5 zakładów"""

    def __init__(self, master):
        super().__init__(master)
        self.k = []
        self.ramka_gora = Frame(self)
        self.ramka_gora.grid(row=0, column=0)
        self.ramka_dol = Frame(self)
 #       self.sep = Separator(self)
        self.ramka_dol.grid(row=1, column=0, pady=50)
        self.pack()
        for liczba in range(3):
            self.k.append(Zaklad(self.ramka_gora).pack(side='left'))
        p = Button(self.ramka_dol, text ="Przykładowy przycisk").pack(side='bottom')

     #   self.pack()



okno = Tk()
okno.title("Kupon totolotka")

kupon = []
# x = Zaklad(okno,6, 49)

x = Kupon(okno)

okno.mainloop()
