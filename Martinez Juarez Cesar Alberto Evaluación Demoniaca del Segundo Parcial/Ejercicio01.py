# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:03:20 2022
@author: cesar
Ejercicio01-Metodos Numericos-Método de bisección
"""
# Algoritmo de Bisección
# [a,b] se escogen de la gráfica de la función
#Importamos librerias
import matplotlib.pyplot as plt
from tabulate import tabulate
import sympy as sp

def ingresar(a,b,tol,ing):#Ingresamos datos para el metodo
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
        ing=input('Ingresa las cifras de tolerancia tolerancia>0:')#Se solicita las cifras de tolerancia
        try:
            ing=int(ing)
            if(ing>= 0 and ing % 1 == 0):
                tol=1/(10**ing)#se da el numero de tolerancia ya en base 10
                break
        except:print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")                
    return a,b,tol,ing
    

def Grafica_Chida(f,xi,xf,num=1000):#se grafica si exito pero se intenta por que el metodo asi bien futurista no compila
    plt.style.use("dark_background")
    ejey = 'f(' + variable + ')'
    sp.plotting.plot(y,xlabel = variable, ylabel = ejey)
    plt.title(f"Metodo de Biseccion f(x)={y}",fontsize=12)
    plt.show()

def Bissc(f,a,b,tol):#metodo asi brutal
    di=[];da=[];db=[];dc=[];de=[]#para graficar todos los datos
    if f(a)*f(b)>=0:#Condicion
        print(f"El intervalo no funciona f(a)={f(a)} y f(b)={f(b)}")
    e_abs=abs(b-a)
    m_at=0
    i=1#Contador
    while e_abs>tol:
        c=(a+b)/2
        if i==1:
            error=abs(b-a)/2
            m_at=c
        else:
            error=abs((c-m_at)/c)#Se calcula el error relativo
            m_at=c
        di.append(i);da.append(a);db.append(b);dc.append(c);de.append(error)#se guardan los datos para las tablas
        if f(c)==0:
            return di,da,db,dc,de,c
        if f(a)*f(c)<0:
            b=c
            c_t=a
        else:
            a=c
            c_t=b
        e_abs=abs(c_t-c)
        if e_abs<tol:
            return di,da,db,dc,de,c
        i+=1
    print(f"Solucion NO encontrada, iteraciones agotadas {i-1}")
    return di,da,db,dc,de,c

def Tabla():
    c=0
    di=[];da=[];db=[];dc=[];de=[]
    (di,da,db,dc,de,c)=Bissc(f1,a,b,tol)
    datos=[]
    for i in range(0,len(di),1):        
        datos.append([di[i],da[i],db[i],dc[i],de[i]])
    print(tabulate(datos,headers=["i","'a'","'b'","xi","error"],tablefmt="orgtbl"))
    print(f"La raiz solucion x={c} con {len(di)} iteraciones con {ing} numeros de presicion")
    nombre=input("Ingresa el nombre del archivo de txt:")
    nombre+=".txt"
    archivo=open(nombre,'a')
    archivo.write("\nMetodo de biseccion\n")
    archivo.write(f"\nIntervalos [a,b]=[{a},{b}]")
    archivo.write(f"\nDigitos de presicion:{ing}")
    archivo.write(f"\nEcuación:{equa}")
    archivo.write(f"\nRaiz:{c}\n")
    archivo.write("------------------------------------------------------"+"\n")
    archivo.write(tabulate(datos,headers=["i","'a'","'b'","xi","error"],tablefmt="orgtbl")+"\n")
    archivo.write("------------------------------------------------------")
    archivo.close()
    return None

def f1(r):
    omega=y.subs(x,r).evalf()
    return omega 

plt.close()
while True:
    variable = input('Ingrese la variable: ')
    if (' ' in variable) == False:
        break
x = sp.Symbol(variable)
equa = input('Ingresar la ecuación: ')
y= sp.sympify(equa)
    
tol=a=b=0.0
ing=0
(a,b,tol,ing)=ingresar(a, b,tol,ing)
Bissc(f1,a,b,tol)
Tabla()
Grafica_Chida(f1, a, b)
