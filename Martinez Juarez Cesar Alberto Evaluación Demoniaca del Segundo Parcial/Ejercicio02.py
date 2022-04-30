# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:52:13 2022
@author: cesar
Ejercicio02-Metodos Numericos-Método de Newton-Raphson 
"""
import matplotlib.pyplot as plt
from tabulate import tabulate
import sympy as sp

def f1(r):
    omega=y.subs(x,r).evalf()
    return omega 
def dvf1(r):
    alfa=dy.subs(x,r).evalf()
    return alfa

def NR_Mth(x0,tol):
    dx=[];di=[];de=[];
    xi=x0
    i=1
    error=abs(2*tol)
    while not(error<=tol):
        x1=xi-(f1(xi)/dvf1(xi))
        error=abs(x1-xi)
        xi=x1
        dx.append(x1);di.append(i);de.append(error)
        i+=1
    print("\n")
    return dx,di,de,x1

def Tabla():
    x1=0.0
    dx=[];di=[];de=[];
    (dx,di,de,x1)=NR_Mth(x0,tol)
    datos=[]
    for i in range(0,len(di),1):        
        datos.append([di[i],dx[i],de[i]])
    print(tabulate(datos,headers=["i","x_i","e"],tablefmt="orgtbl"))
    print(f"\nLa raiz solucion x={x1} con {len(di)} iteraciones con {ing} numeros de presicion")
    nombre=input("Ingresa el nombre del archivo de txt:")
    nombre+=".txt"
    archivo=open(nombre,'a')
    archivo.write("-Método de Newton-Raphson-")
    archivo.write(f"\nx0={x0}")
    archivo.write(f"\nDigitos de presicion:{ing}")
    archivo.write(f"\nEcuación:{equa}")
    archivo.write(f"\nDerivada ecuación:{dy}")
    archivo.write(f"\nRaiz:{x1}\n")
    archivo.write("------------------------------------------------------"+"\n")
    archivo.write(tabulate(datos,headers=["i","x_i","e"],tablefmt="orgtbl")+"\n")
    archivo.write("------------------------------------------------------")
    archivo.close()
    #Grafica
    plt.style.use("dark_background")
    ejey = 'f(' + variable + ')'
    sp.plotting.plot(y,xlabel = variable, ylabel = ejey)
    plt.title(f"-Método de Newton-Raphson- f(x)={y}",fontsize=12)
    plt.show()
    return None


def ingresar(x0,tol,ing):#Ingresamos datos para el metodo
    while True:
        x0=input("Ingresa el valor de x0:")
        try:
            x0=float(x0)
            break
        except:print("Por favor ingresa un Numero valido")
        
    while True:
        ing=input('Ingresa las cifras de tolerancia tolerancia>0:')#Se solicita las cifras de tolerancia
        try:
            ing=int(ing)
            if(ing>= 0 and ing % 1 == 0):
                tol=1/(10**ing)#se da el numero de tolerancia ya en base 10
                break
        except:print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")                
    return x0,tol,ing


while True:
    variable = input('Ingrese la variable: ')
    if (' ' in variable) == False:
        break
x = sp.Symbol(variable)
equa = input('Ingresar la ecuación: ')
y= sp.sympify(equa)
dy=sp.diff(y,x)
plt.close()

x0=tol=0.0
ing=0
(x0,tol,ing)=ingresar(x0,tol,ing)
Tabla()