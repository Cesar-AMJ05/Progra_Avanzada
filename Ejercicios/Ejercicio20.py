# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:13:36 2022

@author: cesar
"""
#Ejercicio20
import math
print("Hola (⌐■_■), a continuacion se mostrara la demostracion de π/4\nmediante fraccion continua\n")
cont=suma=0
dato=1
vueltas=0
while True:
    suma=dato+1
    for i in range(dato,0,-1):
        cont=((2*i)-1)+(i/suma)
        suma=cont
    cont=(1/cont)
    print(f"[{vueltas}]-->{cont}")
    vueltas+=1
    if cont>=(math.pi)/4:
        break
    else:
        dato+=1
        continue
print("Procesando... (⌐■_■)\n")
print (f"Despues de {vueltas} repeticiones,\nEl valor aprox de π/4 es:\nπ/4≈{cont}")

