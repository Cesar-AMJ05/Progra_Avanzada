# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:48:44 2022

@author: cesar
"""
import re
print("Ejercicio 25,Contador de letras")

nota = input("Ingrese un texto:")
Libreta = {}
texto=re.sub("[^A-Za-z]","",nota)
for letra in texto.lower():
    if letra not in Libreta:
        Libreta[letra] = 1
    else:
        Libreta[letra] +=1
for i, k in Libreta.items():
    print("{}:  {}".format(i,k))