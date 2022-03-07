# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:52:14 2022

@author: cesar
"""
#Ejercicio22
print("La criba de Sundaram")
while True:
    a = (input('Ingrese el numero de repeticiones que\nQuiere observar con el algoritmo de por favor:'))
    key = a.isnumeric()
    if(key):
        a = int(a)
        if(a >= 0 and a % 1 == 0 and key):
            print("Procesando... (⌐■_■)\n")
            break
    else: print("¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")    
B=[]
i=j=2
for i1 in range (1,a+1,1):
    B.append(True)   
while True:
    if(i<=a):
        x=i*j
        if(x<a):
            #print(x, end=" ")
            B[x]=False
            j+=1
        else:
            i+=1
            j=2
    else:
        break
for w in range(2,a,1):
    if(B[w]):
        print(w, end=" ")
