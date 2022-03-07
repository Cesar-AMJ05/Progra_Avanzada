# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:48:30 2022

@author: cesar
"""
#Ejercicio29
print("Ejercicio 29,Calculadora numeros Complejos")
import math, cmath

def entrada():
    while True:
            user = input("Dame un numero complejo recuerda que debe ser de la forma:\na+bj:\n")
            try:
                n= complex(user)
                break
            except:
                print("¡¡Debe ser numero complejo de la forma: a+bj\n")
    return n

def Real():
    print("Elejiste la Opcion 1. Mostar la parte real del numero complejo")
    n=entrada()
    nreal=n.real
    print(f"Tu numero complejo es: {n}\nLa parte real de tu numero complejo es: {nreal}")

def Img():
    print("Elejiste la Opcion 2. Mostar la parte compleja del numero complejo")
    n=entrada()
    nimg=n.imag
    print(f"Tu numero complejo es: {n}\nLa parte imaginaria o compleja de tu numero complejo es: {nimg}")

def partes():
    print("Elejiste la Opcion 3. Mostar la parte real e imaginaria del numero complejo")
    n=entrada()
    nreal=n.real
    nimg=n.imag
    print(f"Tu numero complejo es: {n}\nLa parte real de tu numero complejo es: {nreal}\nLa parte imaginaria de tu numero complejo es: {nimg}")

def modulo():
    print("Elejiste la Opcion 4. Calcular el modulo o valor absoluto de tu numero complejo")
    n=entrada()
    modn=math.sqrt((n.real**2)+(n.imag**2))
    print(f"El modulo de {n} es: {modn}")

def fase():
    print("Elejiste la Opcion 5. Calcular la fase de tu numero complejo")
    n=entrada()
    fasen=cmath.phase(n)
    fasend=math.degrees(fasen)
    print(f"La fase de {n} es: {fasen} radianes o {fasend}")

def p_escalar():
    print("Elejiste la Opcion 6. Calcular el producto escalar de tu numero complejo")
    n=entrada()
    r=float(input("Dame el numero por el cual se va a multiplicar tu numero complejo:\n"))
    complejoc=r*n
    print(f"Tu numero complejo se mmultiplico por {r}.\nEl producto escalar es: {r} * {n} = {complejoc}")

def error():
    print("error, opcion invalida")    

def suma():
    print("Elejiste la Opcion 1. Calcular la suma de tus numero complejos")
    n=entrada()
    m=entrada()
    suma=n+m
    print(f"la suma de tus numeros complejos es: {n} + {m} = {suma}")

def resta():
    print("Elejiste la Opcion 2. Calcular la resta de tus numero complejos")
    n=entrada()
    m=entrada()
    resta=n-m
    print(f"La resta de tus numeros complejos es: {n} - {m} = {resta}")

def multp():
    print("Elejiste la Opcion 3. Calcular la multiplicación de tus numero complejos")
    n=entrada()
    m=entrada()
    multp=n*m    
    print(f"La multiplicación de tus numeros complejos es: {n} * {m} = {multp}")

def div():
    print("Elejiste la Opcion 4. Calcular la división de tus numero complejos")
    n=entrada()
    m=entrada()
    div=n/m
    print(f"La división de tus numeros complejos es: {n} / {m} = {div}")

def p_esc():
    print("Elejiste la Opcion 5. Calcular el producto escalar de tus numero complejos")
    n=entrada()
    m=entrada()
    r=float(input("Dame el numero por el cual se va a multiplicar tus numeros complejos:\n"))
    complejoc1=r*n
    complejoc2=r*m
    print(f"Tus numeros complejos se mmultiplicaron por {r}.\nEl producto escalar de {n} es: {r} * {n} = {complejoc1}\nEl producto escalar de {m} es: {r} * {m} = {complejoc2}")


opt1={
    '1':Real,
    '2':Img,
    '3':partes,
    '4':modulo,
    '5':fase,
    '6':p_escalar
    }

opt2={
    '1':suma,
    '2':resta,
    '3':multp,
    '4':div,
    '5':p_esc,
}



while True:
    while True:
            option=input("Cuantos numeros complejos desea operar, uno [1] o dos [2]:\n")
            if option=='1':
                break
            elif option=='2':
                break
            else:
                print("opcion invalida")
                print("opcion invalida")
    if option=='1':
                sw=input('''Elije como quieres operar el numero complejo.
                [1]-Mostrar parte real 
                [2]-Mostrar parte imaginaria 
                [3]-Mostrar tanto parte real como imaginaria 
                [4]-Calcular el modulo 
                [5]-Calcular la fase 
                [6]-Calcular el producto escalar 
                Teclea el numero de la opcion de tu eleccion:
                ''')
                opt1.get(sw, error)()
    elif option=='2':
                sw=input('''Elije como quieres operar Los numeros complejos.
                [1]-Suma de los numeros
                [2]-Resta de los numeros 
                [3]-Multiplicacion de los numeros 
                [4]-Division de los numeros 
                [5]-Producto escalar a los numeros 
                Teclea el numero de la opcion de tu eleccion:
                ''')
                opt2.get(sw, error)()
    option=input("Para volver al Menu pulsa 'SI' y enter; si no teclea cualquier cosa y da enter\n")
    if option=='SI':
        print("Cargando... (⌐■_■)\n")
    else:
        print("Nos vemos... (⌐■_■)\n")
        break
