# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:47:11 2022

@author: cesar
"""
#Ejercicio10
print("Ejercicio 10,Doble Factorial n!!")
def ingresar():
    while True:
        swp=input('Ingresa un numero ENTERO \npara calcular el DOBLE FACTORIAL n!!, por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
a=ingresar()
if(a%2==1):
    x=1
    for i1 in range (1,a+1,1):
        if(i1%2==1):
          x=i1*x
    print(f'El doble factorial de "{a}" es n!!={x}')
elif(a%2==0):
    y=1
    for i2 in range(1,a+1,1):
        if(i2%2==0):
            y=i2*y
    print(f'El doble factorial de "{a}" es n!!={y}')
