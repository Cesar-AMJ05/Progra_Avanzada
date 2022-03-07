# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:11:29 2022

@author: cesar
"""
#Ejercicio04
print("Ejercicio 4,Triangulo de Numeros")
def ingresar():
    while True:
        swp=input('Ingresa un numero ENTERO POSITIVO por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
a=ingresar()
for i in range (1,a+a,2):
    for j in range (i, 0, -2):
        print(j,end=" ")
    print("\n")