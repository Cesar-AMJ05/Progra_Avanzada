# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 05:45:01 2022
@author: cesar
Ejercicio03-Metodos Numericos- Método de Lin-Bairstow 
"""
from tabulate import tabulate

def ingresar():
    grado=int(input("Ingresa el grado del polinomio (menor a 5) : "))
    for k in range(grado+1):
        grad.append(grado-k+1)
    
    for k in range(grado+1):
        constantes.append(float(input("Ingrese el coeficiente la variable de grado {:1d} : ".format(grado-k))))
    
    ecuacion=""
    for  k in range(0,len(grad),1):
        if k<len(grad)-1:
            ecuacion+=str(constantes[k])+"x"+"^"+str(grad[k]-1)+"+"
        elif k==len(grad)-1:
           ecuacion+=str(constantes[k])
           
    r=float(input("Ingresa el valor de ro: "))
    s=float(input("Ingresa el valor de So: "))
    archivo=open("Método de Lin-Bairstow_Datos.txt","w")
    archivo.write("-Método de Lin-Bairstow-")
    archivo.write(f"\nEcuacion: {ecuacion}")
    archivo.write(f"\nr0={r}")
    archivo.write(f"\ns0={s}")
    archivo.close()
    return r,s,grado

def Solucion():
    r=s=0.0
    grado=0
    (r,s,grado)=ingresar()
    di=[];dtr=[];dts=[]
    b1=1
    b0=1
    i=0
    delta_r=0
    delta_s=0
    while (b0!=0 and b1!=0):
        r=r+delta_r
        s=s+delta_s
        suma.clear()
        suma2.clear()
        suma.append(constantes[0])
        for k in range(1,grado+1):
            if k==1:
                valor=(suma[k-1]*r+constantes[k])
                suma.append(round(valor,10))
            else:
                valor=(suma[k-1]*r+suma[k-2]*s+constantes[k])
                suma.append(round(valor,10))
            
        suma2.append(suma[0])
        for k in range(1,grado+1):
            if k==1:
                valor=suma2[k-1]*r+suma[k]
                suma2.append(round(valor,10))
            else:
                valor=suma2[k-1]*r+suma2[k-2]*s+suma[k]
                suma2.append(round(valor,10))
        i+=1
        b0=suma[grado]
        b1=suma[grado-1]
        c1=suma2[grado-1]
        c2=suma2[grado-2]
        c3=suma2[grado-3]
        #Deltas
        delta_s=((b1*c1)-(b0*c2))/((c2**2)-(c1*c3))
        delta_r=((b0*c3)-(b1*c2))/((c2**2)-(c1*c3))
        #archivo.write("delta_s=%s\n"%delta_s)
        #archivo.write("delta_r=%s\n"%delta_r)
        di.append(i);dtr.append(delta_r);dts.append(delta_s)
    x1=(r+(r**2+4*s)**(1/2))/2
    x2=(r-(r**2+4*s)**(1/2))/2 
    #Muestra Rices
    archivo=open("Método de Lin-Bairstow_Datos.txt","a")
    text=("Una raiz del polinomio es = "+str(x1))   
    print(text);archivo.write("\n"+text)
    text=("Una raiz del polinomio es = "+str(x2))
    print(text);archivo.write("\n"+text)
    x2=(-suma[1]+((suma[1]**2)-(4*suma[0]*suma[2]))**(1/2))/(2*suma[0])
    text=("Una raiz del polinomio es = "+str(x2))
    print(text);archivo.write("\n"+text)
    x2=(-suma[1]-((suma[1]**2)-(4*suma[0]*suma[2]))**(1/2))/(2*suma[0])
    text=("Una raiz del polinomio es = "+str(x2))
    print(text);archivo.write("\n"+text)
    archivo.close()
    return di,dtr,dts,r,s
grad=[];constantes=[];suma=[];suma2=[]


def Tabla():  
    r=s=0.0
    di=[];dtr=[];dts=[];er=[];es=[];
    (di,dtr,dts,r,s)=Solucion() 
    for i in range(0,len(di),1):
        er.append((dtr[i]/r)*0.1)
        es.append((dts[i]/s)*0.1)
    datos=[]
    for i in range(0,len(di),1):        
        datos.append([di[i],dtr[i],dts[i],er[i],es[i]])
    print(tabulate(datos,headers=["i","r_i","s_i","e_r","e_s"],tablefmt="orgtbl"))
    archivo=open("Método de Lin-Bairstow_Datos.txt","a")
    archivo.write("\n")
    archivo.write("------------------------------------------------------"+"\n")
    archivo.write(tabulate(datos,headers=["i","r_i","s_i","e_r","e_s"],tablefmt="orgtbl")+"\n")
    archivo.write("------------------------------------------------------")
    archivo.close()

Tabla()
    