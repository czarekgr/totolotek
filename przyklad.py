#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'czarek'

# origin https://github.com/czarekgr/totolotek.git


class Dupa:
    def __init__(self,k):
        self.k= k


kutas = []
for a in range(10):
    kutas.append(Dupa(a))

print(kutas[3].k)
