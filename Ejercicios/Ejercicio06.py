# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:56:17 2022

@author: cesar
"""
#Ejercicio6
print("Ejercicio 6,Descomposicion por unidades de un numero")
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
A=[val for i, val in enumerate(str(a))]
B=A.copy()
for n in range(0,b):
    domi=int(A[n])*(10**(b-(n+1)))
    B[n]=str(domi)
    igualdad="+".join(B)
print(f"{a}={igualdad}")
