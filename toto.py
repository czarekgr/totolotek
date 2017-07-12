#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'czarek'

import random
import os

kupon = []


def losuj(ile=6, do=49):  # losowanie zbioru różnych liczb
    wynik = set([])
    for i in range(1, ile + 1):
        while 1:
            liczba = ord(os.urandom(1)) >> 2
            if liczba not in wynik and liczba > 0 and liczba <= do:
                wynik.add(liczba)
                break
    return (wynik)

def obstaw(ile=6, do=49):  # wypełnienie zakładu (kratki na kuponie)
    obstawione = set([])
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


i = int(input("ile zakładów?:"))
ilosc_losowan = int(input("ile losowań?:"))

for z in range(i):
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
        if wynik > 4:
            print(wynik, "w", i, "losowaniu")

print(wyniki)
