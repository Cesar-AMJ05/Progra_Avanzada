# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 23:00:48 2022

@author: cesar
"""
print("Ejercicio 17,Numero de Keith")
def ingresar():
    while True:
        swp=input('Ingresa cuantos numeros de Keith quieres ver por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp

def keith(n):
    valores = []
    nc=str(n) 
    Ln=len(nc)
    bien=True
    resultado=0
    for dig1 in range(0,Ln):
        valores.append(nc[dig1])
    while bien:
        val=0
        for dig2 in range(0,Ln):
            val=val+int(valores[dig2])
        del(valores[0])
        valores.append(str(val))
        if val==n:
           resultado=val
           bien = False
        elif val>n:
            bien=False
    return resultado
num =ingresar()
listo=True
inicio=13
cuenta=0
while listo:
    inicio=inicio+1
    calculo=keith(inicio)
    if calculo>0:
        print(calculo, end=" ")
        cuenta+=1
        if cuenta==num:
            listo=False