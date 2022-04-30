# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:58:20 2022

@author: cesar
Ejercicio06-Python Scripts
Suma Armonica-Recursividad
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
    return int(num)

def Suma_Harmonica(n):
    if(n<=1):
        return(n)
    return 1/n+Suma_Harmonica(n-1)

limite=ingresar()
re_dec=Suma_Harmonica(limite)
print(f"El resultado de la suma Armonica para {limite} interaciones es:{re_dec}")

