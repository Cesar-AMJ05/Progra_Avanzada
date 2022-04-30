# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 01:10:16 2022
@author: cesar
Ejercicio12-CURP completo
"""
import re
def Nombre(Nom_AP,c_NA="",nombre="",c_DF=""):
    while True:
        nom=str(input("Ingresa tu nombre(s):")).upper()
        try:
            if nom!="":
                break
            else:print("Por favor, ingresa tu nombre(s)")
        except:
            print("Por favor, ingresa tu nombre(s)")
    while True:
        ap=str(input("Ingresa tu Apelliado Paterno:")).upper()
        am=str(input("Ingresa tu Apellido Materno:")).upper()
        if ap!="" or am!="":
            break
    #Primeros carcteres
    r1=re.findall("[A,E,I,O,U]", ap)
    n=nom.split()
    if (n[0]=="MARIA" or n[0]=="JUAN"):
        x=n[1]
        c_n=x[0]
    else:c_n=nom[0]
    caracteres_N=ap[0]+r1[0]+am[0]+c_n
    Nom_AP={
        "Nombre":nom,
        "Apellido Paterno":ap,
        "Apellido Materno":am
        }
    nombre=ap+" "+am+" "+nom
    #Ultimos Caracteres
    letras=list(map(chr, range(97, 123)))
    letras.insert(14,"ñ")
    vocales=['a','e','i','o','u']
    for n in vocales:
        letras.remove(n)
    letras=str(letras).upper()
    cst=[]
    c_CS=[] 
    for w in range(0,3,1):
        if w==0:iterador=ap
        elif w==1:iterador=am
        else: iterador=nom        
        for x in range(0,len(iterador),1):
            if x<=0:
                continue
            else:
                for y in letras:
                    if y==iterador[x]:
                        cst.append(y)                
                        break       
        c_CS.append(cst[0])
        cst.clear()
    c_DF="".join(c_CS)
    return Nom_AP, caracteres_N, nombre, c_DF

def Fecha_Nacimiento(Date_User,c_DN):
    while True:
        year=input("Introduce el año de tu nacimiento:")
        try:
            chek=int(year)
            if chek>1582:
                xy=year[len(year)-2]+year[len(year)-1]
                break
            else:print("Ingresa un año de nacimiento valido")
        except:
            print("Por favor, el numero del año de tu nacimiento")
            
    while True:
        month=int(input("Introduce el mes de tu nacimiento(1-12):"))
        try:
            month=int(month)
            if month>=1 and month<=12:
                if month <=9:
                    xm="0"+str(month)
                else: xm=str(month)
                break
            else: print("Por favor, el numero de mes de tu nacimiento (1-12)")
        except:print("Por favor, el numero de mes de tu nacimiento (1-12)")
    
    while True:
        day=input("Introduce el dia de tu nacimiento:")
        try:
            day=int(day)
            lst_31=[1,3,5,7,8,10,12]
            lst_30=[4,6,9,11]
            if (month in lst_30) and day>30:
                print(f"Tu mes de nacimiento es el {month} y solo tiene 30 dias\nPorvafor verifica tu fecha de nacimiento")
            elif (month in lst_31) and day>31:
                print(f"Tu mes de nacimiento es el {month} y solo tiene 31 dias\nPorvafor verifica tu fecha de nacimiento")
            elif month==2 and day>29:
                print(f"Tu mes de nacimiento es el {month} y solo tiene 29 dias\nPorvafor verifica tu fecha de nacimiento")
            else:
                fecha=str(day)+"/"+str(month)+"/"+str(year)
                if day <=9:
                    xd="0"+str(day)
                else: xd=str(day)
                break
        except:print("Por favor, el numero del dia de tu nacimiento")
    c_DN=xy+xm+xd
    Date_User={"Fecha de nacimiento":fecha}
    return Date_User,c_DN

def Sexo_EFederativa(sx="",c_EF=""):
    while True:
        print("Selecciona [H]->Hombre o [M]->Mujer")
        sx=str(input("Seleciona tu Sexo [H/M]:")).upper()
        try:
            if sx=="M" or sx=="H":
                break
            else:print("Por favor, Seleciona tu Sexo [H/M]:")
        except:
            print("Por favor, Seleciona tu Sexo [H/M]:")

    print("""{
1.-Aguascalientes           14.-Jalisco             27.-Tabasco
2.-Baja California          15.-Edo. México         28.-Tamaulipas
3.-Baja California Sur      16.-Michoacán           29.-Tlaxcala
4.-Campeche                 17.-Morelos             30.-Veracruz
5.-Chiapas                  18.-Nayarit             31.-Yucatán
6.-Chihuahua                19.-Nuevo León          32.-Zacatecas
7.-Ciudad de México         20.-Oaxaca              
8.-Coahuila                 21.-Puebla
9.-Colima                   22.-Querétaro
10.-Durango                 23.-Quintana Roo
11.-Guanajuato              24.-San Luis Potosí
12.-Guerrero                25.-Sinaloa
13.-Hidalgo                 26.-Sonora
        }""")
    while True:
        sE=input("Seleciona el numero de la Entidad Federativa de nacimiento:")
        try:
            sE=int(sE)
            if sE>=1 and sE<=32:
                   break
            else: print("Por favor, el numero de la Entidad Federativa de nacimiento")
        except:print("Por favor, el numero de la Entidad Federativa de nacimiento")
    sNE=["AS","BC","BS","CC","CS","CH","DF","CL","CM","DG","GT","GR","HG","JC","MC","MN","MS","NT","NL","OC","PL","QO","QR","SP","SL","SR","TC","TS","TL","VZ","YN","ZS"]
    c_EF=sNE[sE-1]
    return sx,c_EF

Nom_AP={}
Date_User={}
c_NA=c_DN=nombre=c_S=c_EF=c_DF=""
(Nom_AP,c_NA,nombre,c_DF)=Nombre(Nom_AP,c_NA,nombre,c_DF)
(Date_User,c_DN)=Fecha_Nacimiento(Date_User, c_DN)
(c_S,c_EF)=Sexo_EFederativa(c_S,c_EF)
CURP=c_NA+c_DN+c_S+c_EF+c_DF

for q in range(0,3,1):
    print("\n")
print("Su CURP sin los dos ultimos digitor es:")

print(CURP)