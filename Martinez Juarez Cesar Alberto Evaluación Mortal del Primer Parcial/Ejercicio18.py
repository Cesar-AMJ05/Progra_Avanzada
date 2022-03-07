# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 00:28:32 2022

@author: cesar
"""
#Ejercicio18
print("Ejercicio 18, Numeros Romanos")
print("Sigue las instrucciones, ingresa un numero para convertitlo en romano○\n")
def ingresar():
    while True:
        swp=input('Ingresa un numero ENTERO en el intervalo [1,3999]por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0 and swp<=3999):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
numR=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
numD=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
texto=""
n=0
w=a=ingresar()
while a>0:
    for x in range(a//numD[n]):
        texto+=numR[n]
        a-=numD[n]
    n+=1
print(f"Tu numero {w} en Romano es: {texto}")