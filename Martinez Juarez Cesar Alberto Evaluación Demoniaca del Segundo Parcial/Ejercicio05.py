# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:51:15 2022
@author: cesar
Ejercicio05-Metodos Numericos-Caminata del borracho-alias "Caminata profe Quintanar"
"""
#Importamos las librerias
import math,pylab,random
import matplotlib.pyplot as plt
from tabulate import tabulate

def long_paso():
    while True:
        l=input('Ingresa la longuitud de paso por favor:')
        try:
            l=float(l)
            if(l >= 0):break
        except:print("\n¡NUMERO POSITIVO l>0! ༼ つ ◕_◕ ༽つ")      
    return l

def num_pasos():
    while True:
        n=input('Ingresa un numero de pasos por favor:')
        try:
            n=int(n)
            if(n >= 0 and n%1==0):break
        except:print("\n¡NUMERO POSITIVO n>0 y n!=0 ! ༼ つ ◕_◕ ༽つ")      
    return n

def Caminata_porfe_Porgramacion(n,l):
    x=y=0
    random.seed()
    movx=[x]
    movy=[y]
    for i in range(0,n,1):        
        alpha=random.random()*(2*math.pi)
        x+=(l*math.cos(alpha))
        y+=(l*math.sin(alpha))
        movx.append(x)
        movy.append(y)
    return movx,movy

def Grafica_Chida():
     plt.style.use("dark_background")
     for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
         plt.rcParams[param] = '0.9'  # gris claro
     for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
         plt.rcParams[param] = '#1E2247'  # gris azulada oscuro
     plt.figure(1)
     plt.plot(movx,movy,'wo-')
     plt.plot(movx,movy,'#00ff41')
     plt.title("Caminata del borracho",fontsize=15)
     plt.xlabel("Cordendada en x",fontsize=10)
     plt.ylabel("Cordendada en y",fontsize=10)
     pylab.savefig("paseo_aleatorio"+str(n)+".png",bbox_inches="tight",dpi=600)
     plt.show()
     
def Tabla_txt():
    numero_pasos=[]
    datos=[]
    for i in range(0,n,1):
        numero_pasos.append(i)
    for i in range(0,n,1):        
        datos.append([numero_pasos[i],movx[i],movy[i]])
    print(tabulate(datos,headers=["Numero Paso","Cordenada en X","Cordenada en Y"],tablefmt="orgtbl"))
    #Escribimos archivo
    archivo=open("Caminata_del_Borracho_Datos.txt",'a')
    archivo.write(f"\nNumero de pasos:{n}\n")
    archivo.write(f"Longuitud de paso:{l}\n")
    archivo.write("------------------------------------------------------"+"\n")
    archivo.write(tabulate(datos,headers=["Numero Paso","Cordenada en X","Cordenada en Y"],tablefmt="orgtbl")+"\n")
    archivo.write("------------------------------------------------------")
    archivo.close()
    
plt.close()    
l=long_paso()
n=num_pasos()
movx=[]
movy=[]
(movx,movy)=Caminata_porfe_Porgramacion(n,l)
Grafica_Chida()
Tabla_txt()