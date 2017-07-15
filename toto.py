#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'czarek'

import random
import os  # Do losowania, uwaga typowo uniksowe, w windzie może być inaczej

kupon = []


def losuj(ile=6, do=49):  # losowanie zbioru różnych liczb (domyślnie 6 liczb z zakresu 1..49)
    wynik = set()
    for i in range(ile):
        while 1:
            liczba = ord(os.urandom(1)) >> 2 # Przesuniecie bitowe dla przyspieszenia jak losują się duże liczby
            if liczba not in wynik and liczba > 0 and liczba <= do:
                wynik.add(liczba)
                break
    return (wynik)

def obstaw(ile=6, do=49):  # wypełnienie zakładu (kratki na kuponie)
    obstawione = set()
    for i in range(1, ile + 1):
        while 1:
            try:
                print("podaj liczbę nr", i, end="")
                liczba = int(input("  :"))
            except ValueError:
                continue
            if liczba not in obstawione and liczba > 0 and liczba <= do:
                obstawione.add(liczba)
                break

    return (obstawione)


# start programu, tu jeszcze do poprawy


i = int(input("ile zakładów?:"))
ilosc_losowan = int(input("ile losowań?:"))

for z in range(i):  # obstawianie zakładów
    print("zakład nr:", z + 1)
    print(12 * "-")
    kupon.append(obstaw())
    print()


wyniki = {3: 0, 4: 0, 5: 0, 6: 0}

for i in range(ilosc_losowan):
    los = losuj()
    for zaklad in kupon:
        wynik = len(zaklad & los)
        if wynik > 2:
            wyniki[wynik] += 1
        if wynik > 4:  # jak się trafi 5 lub 6 to wypisze ten fakt
            print(wynik, "w", i, "losowaniu")


print("\n\nNa",ilosc_losowan,"losowań trafiłeś:")
for i in range(3,7):
    print(i,":  ",wyniki[i])

