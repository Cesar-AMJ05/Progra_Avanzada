# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 01:01:03 2022

@author: cesar
"""
#Ejercicio11
print("Ejercicio 11,Codigo de barras EAN-8")
while True:
    entrada = (input('Ingresa un numero ENTERO de 8 DIGITOS por favor:'))
    key = entrada.isnumeric()
    rec=[]
    if(key and len(entrada)==8 ):
        a = int(entrada)
        if(a >= 0 and a % 1 == 0 and key):
            print("Procesando... (⌐■_■)\n")
            for i in entrada:
                rec.append(int(i))
            a=rec[0]+rec[2]+rec[4]+rec[6]
            b=(rec[1]+rec[3]+rec[5]+rec[7])*3
            c=a+b
            d=c%10
            e=d-10
            print(f"Su numero de control EAN-8 es {entrada}{e}")
            break 
    else:
        print("¡NUMERO ENTERO POSITIVO DE 8 DIGITOS! ༼ つ ◕_◕ ༽つ\n")