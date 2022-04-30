# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:33:30 2022

@author: cesar
Ejercicio06-Python Scripts
Serie de Padovan-Programacion Funcional
"""
def ingresar():
    while True:
        num=input('Ingresa un numero ENTERO POSITIVO por favor:')
        try:
            num=int(num)
            if(num >= 0 and num % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return num

def Serie_Padovan(n):
    f1=f2=fnow=fnext=1
    for i in range (3,n+1):
        fnext=f1+f2
        f1=f2
        f2=fnow
        fnow=fnext
    return fnext

limite=ingresar()
for w in range(limite):
    print(Serie_Padovan(w),end=",")