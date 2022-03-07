# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:09:17 2022

@author: cesar
"""
#Ejercicio19
print("Ejercicio 19,Serie de numeros de Pell")
def ingresar():
    while True:
        swp=input('Ingresa un cuantos datos quieres de la serie.\nnumero ENTERO POSITIVO por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
x=1
y=2
z=0
a=ingresar()
for i in range(1,a,1):  
    if(i<=1):
        z=i
    else:
        z=(y*2)+x
        x=y
        y=z
    print(z, end=" ")