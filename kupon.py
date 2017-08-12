#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'czarek'

import random
import os

from tkinter import *


# from tkinter.ttk import *

class Dyscyplina(Button):
    """Pojedyncza kratka z liczbą"""
    aktywny = 0
    ilosc = 0
    kolor_aktywny = "red"
    kolor_nieaktywny = "gray85"

    def zmien_aktywnosc(self, zezwolenie):
        if (self.aktywny == 0 and zezwolenie):
            self.aktywny = 1
            self.configure(bg=self.kolor_aktywny, activebackground=self.kolor_aktywny)
        else:
            self.aktywny = 0
            self.configure(bg=self.kolor_nieaktywny, activebackground=self.kolor_nieaktywny)
    def zeruj_aktywnosc(self):
        self.aktywny = 0
        self.configure(bg=self.kolor_nieaktywny, activebackground=self.kolor_nieaktywny)

    def ustaw_aktywnosc(self):
        self.aktywny = 1
        self.configure(bg=self.kolor_aktywny, activebackground=self.kolor_aktywny)

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
            self.z[liczba]["command"] = lambda x=liczba: self.zaznacz(x)

    def zaznacz(self, k):
        i = self.ile_obstawionych()
        self.z[k].zmien_aktywnosc(i < self.ile)

    def ile_obstawionych(self):
        ile = 0
        for liczba in range(0, self.do):
            ile = ile + self.z[liczba].aktywny
        return (ile)

    def get_obstawione(self):
        obstawione = set()
        for i in range(0, self.do):
            if self.z[i].aktywny == 1:
                obstawione.add(i + 1)
        return obstawione

    def obstaw(self,liczby):
        for i in range(0,self.do):
            self.z[i].zeruj_aktywnosc()
        for i in range(0,self.do):
            if i in liczby:
                self.z[i].ustaw_aktywnosc()


class Kupon(Frame):
    """kupon zawiera 5 zakładów"""

    def __init__(self, master):
        super().__init__(master)
        self.ilosc_zakladow = 5
        self.k = []
        self.ramka_gora = Frame(self)
        self.ramka_gora.grid(row=0, column=0)
        self.ramka_dol = Frame(self)
        self.ramka_dol.grid(row=1, column=0, pady=50)
        self.etykieta1 = Label(self.ramka_dol, text="Na ile losowań?").grid(row=0, column=0)
        self.ilosc_los = Entry(self.ramka_dol )
        self.ilosc_los.grid(row=0, column=1, sticky=S, pady=10)
        self.ilosc_los.insert(8,"1000")
        self.etykieta2 = Label(self.ramka_dol, text="Szóstek:").grid(row=1, column=1, sticky=E, pady=5)
        self.etykieta3 = Label(self.ramka_dol, text="Piątek:").grid(row=2, column=1, sticky=E, pady=5)
        self.etykieta4 = Label(self.ramka_dol, text="Czwórek:").grid(row=3, column=1, sticky=E, pady=5)
        self.etykieta5 = Label(self.ramka_dol, text="Trójek:").grid(row=4, column=1, sticky=E, pady=5)
        self.wynik6 = Label(self.ramka_dol, text ="0")
        self.wynik6.grid(row=1, column=2)
        self.wynik5 = Label(self.ramka_dol, text="0")
        self.wynik5.grid(row=2, column=2)
        self.wynik4 = Label(self.ramka_dol, text="0")
        self.wynik4.grid(row=3, column=2)
        self.wynik3 = Label(self.ramka_dol, text="0")
        self.wynik3.grid(row=4, column=2)
        self.pack()

        for liczba in range(self.ilosc_zakladow):
            self.k.append(Zaklad(self.ramka_gora))
            self.k[liczba].grid(row=0, column=liczba)


        Button(self.ramka_dol, text="Start", command=self.start).grid(row=6, column=0)
        Button(self.ramka_dol, text="Obstaw losowo", command=self.obstaw_los).grid(row=6, column=1)


    def get_obstawione(self):
        obstawione = []
        for self.zaklad in self.k:
            obstawione.append(self.zaklad.get_obstawione())
        return (obstawione)

    def start(self):  # tu będzie start obliczeń
        kupon=self.get_obstawione()
        print(kupon)
        ilosc_losowan=int(self.ilosc_los.get())
        print(ilosc_losowan)
        wyniki = {3: 0, 4: 0, 5: 0, 6: 0}

        for i in range(ilosc_losowan):
            los = self.losuj()
            for zaklad in kupon:
                wynik = len(zaklad & los)
                if wynik > 2:
                    wyniki[wynik] += 1
                if wynik > 4:  # jak się trafi 5 lub 6 to wypisze ten fakt
                    print(wynik, "w", i, "losowaniu")

        print("\n\nNa",ilosc_losowan,"losowań trafiłeś:")
        for i in range(3,7):
            print(i,":  ",wyniki[i])


            if i ==3:
                self.wynik3.config(text=str(wyniki[3]))
            if i ==4:
                self.wynik4.config(text=str(wyniki[4]))
            if i ==5:
                self.wynik5.config(text=str(wyniki[5]))
            if i ==6:
                self.wynik6.config(text=str(wyniki[6]))



    def obstaw_los(self):
        pass
        for self.zaklad in self.k:
            self.zaklad.obstaw(self.losuj())

    def losuj(self,ile=6, do=49):  # losowanie zbioru różnych liczb (domyślnie 6 liczb z zakresu 1..49)
        wynik = set()
        for i in range(ile):
            while 1:
                liczba = ord(os.urandom(1)) >> 2 # Przesuniecie bitowe dla przyspieszenia jak losują się duże liczby
                if liczba not in wynik and liczba > 0 and liczba <= do:
                    wynik.add(liczba)
                    break
        return (wynik)




okno = Tk()
okno.title("Kupon totolotka")
x = Kupon(okno)
okno.mainloop()
