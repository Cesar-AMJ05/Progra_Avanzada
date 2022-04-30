# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:22:35 2022
@author: cesar
Ejercicio 10-RSA
"""
import random

def NumPrim(p=0,q=0):
    while True:
        p=random.randint(3, 11)
        if p%2==1:break
    q=(2*p)+1
    return p,q

def Palabra(M,txt=""):
    while True:
        txt=(input("Ingresa una palabra a encriptar:")).upper()
        try:
            if (txt.isalpha()):break
            else:print(""""
Por favor, palabras sin numeros, signos de puntuacion, etc
Solo Letras ᓚᘏᗢ
""")
        except:print("Solo palabras por favor")
    M=[]
    for i in txt:
        for j in range(0,len(letras),1):
            if i==letras[j]:
               M.append(j) 
    return M,txt

def MCD():
    while True:
        sv=random.randint(1, 100)
        a=sv
        b=thetha
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal 
        if a==1:
            return sv
            break
        

def Claves( clv_plb=0, clv_priv=0,n=""):
    a=MCD()
    m=thetha
    res = pow(a,-1,m)
    #Clave Publica#
    clv_plb=a
    #Clave Privada#
    clv_priv=res
    #Numero
    n=p*q
    return  clv_plb, clv_priv,n

def Cifrado():
    txt="" ; M=[]
    (M,txt)=Palabra(M,txt)
    plb=priv=n=0
    (plb,priv,n)=Claves(plb,priv,n)
    C=[]
    e=plb ; mod=n
    #Cifrado C=M^e%n
    for w in M: C.append(((w)**e)%mod)
    """
    Nota: La contraseña se guarda de la siguiente manera:
        Primeros dos numeros: Son la clave privada y el numero n para el desifrado
        Los demas numeros son el mensaje cifrado
        Ejemplo
        147         253      13 64 216 157 106 6 27 0 27 
         ↑           ↑                    ↑
  Clv. Privada  Numero "n"          Mensaje Cifrado
    """
    #Exponente
    C.insert(0,priv)
    #Modulo
    C.insert(1,mod)
    archivo=open("Contraseña_RSA.txt",'w')
    for q in C:
        archivo.write(str(q)+" ")
    archivo.close()

def DesCifrar():
    read=open("Contraseña_RSA.txt",'r')
    w=read.read()
    z=w.split()
    read.close()
    D=[]
    for i in range(0,len(z),1):
        if i==0: 
            d=int(z[i])
        elif i==1:
            mod_D=int(z[i])
        else:
           D.append((int(z[i])**d)%mod_D)
    rest=[]
    for i in D:
        rest.append(letras[i])
    print(f"Su mensaje descifrado es: {D}")
    msj="".join(rest)
    print(f"Su mensaje ya en texto es:{msj}")
    
    
letras=list(map(chr, range(65, 91)))    
p=q=0
(p,q)= NumPrim(p, q)
thetha=(p-1)*(q-1)
Cifrado()
DesCifrar()
        
