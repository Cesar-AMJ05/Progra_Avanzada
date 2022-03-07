# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:33:43 2022

@author: cesar
"""
#Ejercicio08
print("Ejercicio 8,Invertir Numero")
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
B=[val for i, val in enumerate(str(a))]
B.reverse()
resultado="".join(B)
print(f"N={a} y N(invertido)={resultado}")
