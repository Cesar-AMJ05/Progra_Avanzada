# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 01:03:43 2022

@author: cesar
"""
#Ejercicio28
import math
print("Ejercicio 28,Promedio, Numero de datos y desviación estandar de\nlista dada por el usuario")

def ingresar():
    while True:
        swep=input('Ingresa un numero ENTERO por favor:')
        try:
            num=float(swep)
            break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return num
def decision():
    while True:
        respuesta =input("¿Desea agragar mas numeros?\n [SI,NO]= ")
        try:
            des=str(respuesta)
            if(des=="si" or des=="SI"):
                acceso=True
                break
            elif(des=="no" or des=="NO"):
                acceso=False
                break
            else:print("¡Escribe SI o NO! ༼ つ ◕_◕ ༽つ")                
        except:
            print("¡Escribe SI o NO! ༼ つ ◕_◕ ༽つ")
    return acceso
lista_num=[]
ctt=var=0
while True:
    a=ingresar()
    lista_num.append(a)   
    ctt=len(lista_num)
    print(f"Has ingresado {ctt} numeros a la lista")
    print("\n"+str(lista_num))
    op=decision()
    if op==True:
        continue
    else: break
print("\nProcesando... (⌐■_■)\n")
ctt=len(lista_num)
prom=sum(lista_num)/ctt
for i in range(0,ctt,1):
    var+=(lista_num[i]-prom)**2
des=math.sqrt(var/(ctt-1))
print(f"Tus Datos= {lista_num}\n")
print(f"Num.Datos= {ctt} | Promedio={prom} | Desviación E.={des}")
