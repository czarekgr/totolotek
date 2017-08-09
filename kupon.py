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
    kolor_aktywny = "red"
    kolor_nieaktywny="gray85" \
                     ""
    def zmien_aktywnosc(self, zezwolenie):
        if (self.aktywny == 0 and zezwolenie):
            self.aktywny = 1
            self.configure(bg=self.kolor_aktywny,activebackground=self.kolor_aktywny)
        else:
            self.aktywny = 0
            self.configure(bg=self.kolor_nieaktywny,activebackground=self.kolor_nieaktywny)


class Zaklad(Frame):
    """Pojedynczy zakład (kratka 7x7"""

    def __init__(self, master, ile=6, do=49):
        super().__init__(master, bd=4, bg='red')
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
        self.ramka_dol.grid(row=1, column=0, pady=50)
        self.etykieta1=Label(self.ramka_dol, text="Na ile losowań?").grid(row=0, column=0)
        self.ilosc_los = Entry(self.ramka_dol).grid(row=0, column=1,sticky=S,pady=10)
    #    self.etykieta1=Label(self.ramka_dol, text="Trafiłeś").grid(row=3, column=0, sticky=E, pady=5)
        self.etykieta2=Label(self.ramka_dol, text="Szóstek:").grid(row=1, column=1, sticky=E, pady=5)
        self.etykieta3=Label(self.ramka_dol, text="Piątek:").grid(row=2, column=1, sticky=E, pady=5)
        self.etykieta4=Label(self.ramka_dol, text="Czwórek:").grid(row=3, column=1, sticky=E, pady=5)
        self.etykieta5 = Label(self.ramka_dol, text="Trójek:").grid(row=4, column=1, sticky=E, pady=5)
        self.wynik6 = Label(self.ramka_dol, text="0").grid(row=1,column=2)
        self.wynik5 = Label(self.ramka_dol, text="0").grid(row=2, column=2)
        self.wynik4 = Label(self.ramka_dol, text="0").grid(row=3, column=2)
        self.wynik3 = Label(self.ramka_dol, text="0").grid(row=4, column=2)
        self.pack()
        for liczba in range(5):
            self.k.append(Zaklad(self.ramka_gora).pack(side='left'))
        p = Button(self.ramka_dol, text ="Start").grid(row=6, column=0)

     #   self.pack()



okno = Tk()
okno.title("Kupon totolotka")

kupon = []
# x = Zaklad(okno,6, 49)

x = Kupon(okno)

okno.mainloop()
