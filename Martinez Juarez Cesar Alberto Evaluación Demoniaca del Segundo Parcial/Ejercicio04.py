# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 01:17:34 2022
@author: cesar
Ejercicio04-Metodos Numericos-Método de Trapecios o Trapezoidal
"""
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import sympy as sp

def ingresar(a,b,tramo):#Ingresamos datos para el metodo
    while True:
        a=input("Ingresa el valor a del intervlalo para la funcion [a,b]:")
        try:
            a=float(a)
            break
        except:print("Por favor ingresa un Numero valido")
    while True:
        b=input("Ingresa el valor b del intervlalo para la funcion [a,b]:")
        try:
            b=float(b)
            if b>a:break
            else:print("Por favor ingresa un Numero valido b>a") 
        except:print("Por favor ingresa un Numero valido")    
        
    while True:
        tramo=input('Ingresa n numero de trapecios(intevalos):')#Se solicita las cifras de tolerancia
        try:
            tramo=int(tramo)
            if(tramo>= 0 and tramo % 1 == 0):
                break
        except:print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")                
    return a,b,tramo

def Trapecio_Metodo():
    muestras=tramo+1
    xi=np.linspace(a,b,muestras)  
    fi=[]
    for i in range(0,len(xi),1):
        fi.append(f1(xi[i]))
    mtrlinea=muestras*10
    xk=np.linspace(a,b,mtrlinea)
    fk=[]
    for i in range(0,len(xk),1):
        fk.append(f1(xk[i]))
    #Grafica Funcion con muestras(tramos)
    plt.style.use("dark_background")
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # gris claro
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#080a14'  # gris azulada oscuro
    plt.plot(xi,fi,marker='o',color='#ffffff',label='Muestras')
    plt.plot(xk, fk,color='#00ff41', label='f(x)',linewidth=1.5)
    plt.xlabel('x',fontsize=12)
    plt.ylabel('f(x)',fontsize=12)
    plt.title(f'Integral: Regla de Trapecios f(x)={y}',fontsize=15)
    plt.legend(loc='upper right')
    #Trapecios
    fi = np.array(fi, dtype=float)#Hacemos cambio ya que la matriz tiene
    #un dtype de object, pero esto debería ser un punto flotante dtype.
    plt.fill_between(xi,0,fi, color='#49809f')        
    for i in range(0,muestras,1):
        plt.axvline(xi[i], color='w')
    plt.show()
    
    di=[];dh=[];dvi=[];de=[]
    dis=((b-a)**3)/(12*(tramo**2))
    suma = 0
    for i in range(0,tramo,1):
        dx = xi[i+1]-xi[i]#Espaciado h arbritario (en caso de no ser equidistante)
        Atrapecio = dx*(fi[i]+fi[i+1])/2
        error=dis*Atrapecio*100
        suma = suma + Atrapecio
        di.append(i);dh.append(dx);dvi.append(Atrapecio);de.append(error)
    integral = suma
    print(max(fi))
    print(integral)
    return di,dh,dvi,de,integral


def Tabla():
    integral=0.0
    dh=[];di=[];de=[];dvi=[]
    (di,dh,dvi,de,integral)=Trapecio_Metodo()
    datos=[]
    for i in range(0,len(di),1):        
        datos.append([di[i],dh[i],dvi[i],de[i]])
    print(tabulate(datos,headers=["i","h","Valor_Integral","e"],tablefmt="orgtbl"))
    print(f"\nLa Solucion a la integral es: {integral} con {tramo} trapecios")
    nombre=input("Ingresa el nombre del archivo de txt:")
    nombre+=".txt"
    archivo=open(nombre,'a')
    archivo.write("\n-Método de Trapecios o Trapezoidal-")
    archivo.write(f"\nIntervalo[a,b]=[{a}.{b}]")
    archivo.write(f"\nEcuación:{equa}")
    archivo.write(f"\nNum tramos:{tramo}\n")
    archivo.write(f"\nSolucion Integral Definida={integral}\n")
    archivo.write("------------------------------------------------------"+"\n")
    archivo.write(tabulate(datos,headers=["i","h","Valor_Integral","e"],tablefmt="orgtbl")+"\n")
    archivo.write("------------------------------------------------------")
    archivo.close()
    return None
    
def f1(r):
    omega=y.subs(x,r).evalf()
    return omega 

while True:
    variable = input('Ingrese la variable: ')
    if (' ' in variable) == False:
        break
x = sp.Symbol(variable)
equa = input('Ingresar la ecuación: ')
y= sp.sympify(equa)

tol=a=b=0.0
tramo=0
plt.close()
(a,b,tramo)=ingresar(a, b,tramo)
Tabla()

