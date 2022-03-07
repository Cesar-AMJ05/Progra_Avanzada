# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:23:58 2022

@author: cesar
"""
#Ejercicio9
print("Ejercicio 9,Separador de numero 2.0")
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
b=len(str(a))
y=0
A=[val for i, val in enumerate(str(a))]
B=A.copy()
for n in range(0,b):
    domi=int(A[n])
    B[n]=str(domi)
    igualdad="+".join(B)
    x=int(A[n])
    y=x+y
print(f"N={igualdad}={y}")