# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 01:06:56 2022

@author: cesar
"""
#Ejercicio15
print("Sigue las instrucciones, ingresando solamente NUMEROS\n para calcular el MCD y MCM")
while True:
    entrada1 = (input('Ingresa un numero ENTERO por favor:'))
    key = entrada1.isnumeric()
    entrada2=(input('Ingresa un numero ENTERO por favor:'))
    key2 = entrada2.isnumeric()
    if(key and key2):
        a = int(entrada1)
        b = int(entrada2)
        if(a >= 0 and a % 1 == 0 and key and b >= 0 and b % 1 == 0 and key2 ):
            print("Procesando... (⌐■_■)\n")
            x=a
            y=b
            while  True:
                Rest= x%y
                if(Rest>0):
                    x=y
                    y=Rest
                else:
                    break
            y2=(a*b)/y
            print(f" El MCD de {a} y {b} es MCD={y}\n")
            print(f" El MCM de {a} y {b} es MCM={y2}")
            break
    else:
        print("¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")