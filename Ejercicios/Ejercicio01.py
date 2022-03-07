# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 09:44:38 2022

@author: cesar
"""
#Ejercicio01
print("Ejercicio 1,Numero PAR o IMPAR")
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
tipo = ""
a=ingresar()
if(a % 2 == 0):
     tipo = "Par"
else:
     tipo = "Impar"
print(f"\n Tu numero {a} es {tipo}")   