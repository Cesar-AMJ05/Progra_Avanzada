# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:10:19 2022

@author: cesar
"""
#Ejercicio07
print("Ejercicio 7,Suma de numeros del intervalo [a,b]")
def ingresar():
    while True:
        swp_a=input('Ingresa un numero ENTERO POSITIVO para a por favor:')
        swp_b=input('Ingresa un numero ENTERO POSITIVO para a por favor:')
        swp=[]
        try:
            swp_a=int(swp_a)
            swp_b=int(swp_b)
            if(swp_a >= 0 and swp_a % 1 == 0):
                swp.append(swp_a)
            if(swp_b >= 0 and swp_b % 1 == 0 and swp_b>swp_a):
                    print("Procesando... (⌐■_■)\n")
                    swp.append(swp_b)
                    break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp

num=ingresar()
a=num[0]
b=num[1]
Lista=[val for i, val in enumerate (range(a,(b+1)))]
y=0
for n in range(0,len(Lista),1):
    x=int(Lista[n])
    y=x+y
print(f"Tu intervalo [a,b] es [{a},{b}] y la suma \nde sus numeros intermedios es igual a {y}")