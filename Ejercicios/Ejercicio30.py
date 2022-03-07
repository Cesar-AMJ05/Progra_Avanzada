# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 03:26:56 2022

@author: cesar
"""
#Ejercicio30
print("Ejercicio 30,Permutaciones de una lista")
import itertools
def ingresar():
    while True:
        swp=input('Ingresa un numero ENTERO POSITIVO de 2 a 6 numeros por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                if(len(str(swp))<=6 and len(str(swp))>=2):
                    print("Procesando... (⌐■_■)\n")
                    break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
lista=str(ingresar())
A=[val for i, val in enumerate(str(lista))]
permutaciones=list(itertools.permutations(A))
for i in range(0,len(permutaciones),1):
    print(permutaciones[i], end="\n")