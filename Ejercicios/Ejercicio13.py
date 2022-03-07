# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 07:44:56 2022

@author: cesar
"""
#Ejercicio13
print("Ejercicio 13, Seria de Padovan\n")
while True:
    entrada = (input('Ingresa la cantidad de numeros \nque quiere de la serie de PADOVAN,por favor:'))
    key = entrada.isnumeric()
    if(key):
        x = int(entrada)
        if(x >= 0 and x % 1 == 0 and key):
            print("Procesando... (⌐■_■)")
            a=b=c=d=1
            rec=[]
            if(x<=3):
                for y1 in range(0,x,1):
                    rec.append(a)
                u=''.join(str(rec))
                print(u)
            else:
                for y2 in range(0,3,1):
                    rec.append(a)
                for y3 in range(3,x):
                    d=a+b
                    a=b
                    b=c
                    c=d
                    rec.append(d)
                u=''.join(str(rec))
                print(u)
            break
    else:
        print("¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")