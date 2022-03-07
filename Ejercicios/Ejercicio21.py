# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 01:55:56 2022

@author: cesar
"""
#Ejercicio21
def ingresar():
    while True:
        swp=input('Ingresa un numero ENTERO POSITIVO por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
a=ingresar()   
sep=[val for i, val in enumerate(str(a))]
x=0
listF=[]
rec=[]
key=False
num=[]
suma=0
archivo=[]
rep=[]
while True:
    for i in range (0,len(sep),1):
            num.append((sep[i]))
            x=int(sep[i])**2
            rec.append(x)

    for n in range (len(rec)):
                suma+=int(rec[n])
    listF.append(suma)
    muestra="^2+".join(num)
    print(f"{muestra}^2={suma}")
    
    if(len(listF)==len(set(listF))):
        key=False
    else:
        key=True
        
    if(suma==1):
            print("\nEs un numero Feliz ya que NO se repite y llega a 1")
            print(f"{muestra}^2={suma}<-- Cumple con las caracteristicas")
            print(f"\nPor lo tanto {a} es un numero Feliz")
            break
    elif(key):
            muestra="^2+".join(num)
            print("\nNo es un numero Feliz ya que se repite")
            print(f"{muestra}^2={suma}<-- Se repite")
            print(f"\nPor lo tanto {a} es un numero Infeliz")
            break
    else:
            num.clear()
            sep.clear()
            sep=rec.copy()
            rec.clear()
            sep=[val for i, val in enumerate(str(suma))]
            suma=0

