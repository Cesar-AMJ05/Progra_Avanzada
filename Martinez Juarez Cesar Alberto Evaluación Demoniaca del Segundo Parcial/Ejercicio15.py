# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:29:45 2022
@author: cesar
Ejercicio15-Fibonacci, con valores de n en el intervalo [1, 10000]
PD: No me creia que si le habia entendido a la recursividad :P
"""
def Fibonacho(n):
    if (n==0 or n==1):
        return 1
    else:
        return Fibonacho(n-1)+Fibonacho(n-2)
def ingresar():
    while True:
        swp=input('Ingresa un numero entero y positivoᓚᘏᗢ\nn en el intervalo [1, 10000]:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
def Proceso():
    while True:
        n=ingresar()
        try:
            if(n>=1 and n<=10000):
                break
            else:print("ಠ_ಠ Un numero entero y positivo n en el intervalo [1, 10000]:")
        except:print("ಠ_ಠ  Un numero entero y positivo n en el intervalo [1, 10000]:")
    for i in range(n):
        if i<n-1:
            print(Fibonacho(i),end=",")
        else:print(Fibonacho(i))
#Inicio        
main=Proceso()