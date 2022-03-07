# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:02:00 2022

@author: cesar
"""
#Ejercicio03
print("Ejercicio 3,¿Es un Año Bisiesto?")
def ingresar():
    while True:
        swp=input('Indique el año que desdea calcular por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
año =ingresar()
if(año%4==0 and año%100!=0 or año%400==0):
    print(f"\n El año {año} es Bisiesto")
else:
    print(f"\n El año {año} NO es Bisiesto")