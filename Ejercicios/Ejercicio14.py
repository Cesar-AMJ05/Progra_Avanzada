# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:34:34 2022

@author: cesar
"""
#Ejercicio14
print("Ejercicio 14, Números pseudoaleatorios")
print("Sigue las instrucciones, ingresando solamente\nNUMEROS")
while True:
    Datos=[]
    entrada = (input('Ingresa la cantidad de pseudonumeros aletorios a mostrar:'))
    a=(input("Ingresa un Multiplicador:"))
    b=(input("Ingresa un Sesgo:"))
    m=(input("Ingresa un Modulo:"))
    x0=(input("Ingresa un El valor Inicial:"))
    key = entrada.isnumeric()
    key2= a.isnumeric()
    key3= b.isnumeric()
    key4= m.isnumeric()
    key5= x0.isnumeric()
    if(key and key2 and key3 and key4 and key5):
        x = int(entrada)
        a=float(a)
        b=float(b)
        m=float(m)
        x0=float(x0)
        if(x >= 0 and x % 1 == 0 and key and m>0):
            print("Procesando... (⌐■_■)\n")
            for n in range(0,x,1):
                U=x0/m
                print(U)
                Xn=((a*x0)+b)%m
                x0=Xn
            break
    else:
        print("¡NUMERO ENTERO POSITIVO para la cantidad de pseudonumeros! ༼ つ ◕_◕ ༽つ")