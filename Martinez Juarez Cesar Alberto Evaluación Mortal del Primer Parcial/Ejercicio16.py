# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:20:29 2022

@author: cesar
"""
print("\nEjercicio16, Numeros Narcicistas")
print("\nIngresa dos nueros a y b para el intervalo y asi \nencontrar los numeros narcicistas de dicho intervalo")

def ingresar_a():
    while True:
        swp=input('Ingresa un numero a por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
a=ingresar_a()

def ingresar_b():
    while True:
        swp=input('Ingresa un numero b que cumpla b>a por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0 and swp>a):
                print("Procesando... (⌐■_■)\n")
                break
            else:
                print("\n¡NUMERO ENTERO POSITIVO que cumpla b>a! ༼ つ ◕_◕ ༽つ")      
        except:
            print("\n¡NUMERO ENTERO POSITIVO que cumpla b>a! ༼ つ ◕_◕ ༽つ")      
    return swp

b=ingresar_b()
intervalo=f"[{a},{b}]"
print(f"El intervalo ingresado es [{a},{b}]")
N_Num=[]
def nar(n):
    nstr=str(n)
    m=len(nstr)
    numero=[]
    for i in range(0,m):
        numero.append(int(nstr[i]))
    suma = 0
    for elemento in numero:
        suma += elemento**m
    if suma == n or round(suma**(1/m)) == n:
        v=n
    else:
        v=0
    return v
for i in range(a,b+1):
    a=nar(i)
    N_Num.append(a)
    try:
        N_Num.remove(0)
    except:
        a=0
recntt=[str(a) for a in N_Num]
print(f"Los Números narcisistas de su intervalo {intervalo} son:\n {a}", ', ' . join(recntt))