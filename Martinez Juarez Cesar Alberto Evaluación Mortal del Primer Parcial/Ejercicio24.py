# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:18:39 2022

@author: cesar
"""
#Ejercicio24
while True:
    texto=[]
    pivote=""
    entrada = (input('Ingresa Una frase con menos de  100 caracteres por favor:'))
    if(len(entrada)<=100):
            print("Procesando... (⌐■_■)\n")
            texto=entrada.split(" ")
            for i in range(len(texto),0,-1):
                if(i==len(texto)):
                    pivote=" ".join(texto)
                    print(pivote)
                elif(i<=len(texto)):
                    texto.pop(i)
                    pivote=" ".join(texto)
                    print(pivote)
            break
    else:
        print("¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")

    