# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:08:16 2022

@author: cesar
"""
#Ejercicio02
print("Ejercicio 2,Tablas de Multiplicar")
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
Diccionario={}
a=ingresar()
for i in range (1,11):
    resultado= i*a
    Diccionario[i]=resultado
    print(f"{a} X {i} = {resultado}")