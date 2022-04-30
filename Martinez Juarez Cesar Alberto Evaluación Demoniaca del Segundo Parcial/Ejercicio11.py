# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:12:17 2022
@author: cesar
Ejercicio11-RFC con homoclave
"""
import re
def Nombre(Nom_AP,c_NA="",nombre=""):
    while True:
        nom=str(input("Ingresa tu nombre(s): ")).upper()
        try:
            if nom!="":
                break
            else:print("Por favor, ingresa tu nombre(s)")
        except:
            print("Por favor, ingresa tu nombre(s):")
    while True:
        ap=str(input("Ingresa tu Apelliado Paterno:")).upper()
        am=str(input("Ingresa tu Apellido Materno:")).upper()
        if ap!="" or am!="":
            break
    #Primeros carcteres
    r1=re.findall("[A,E,I,O,U]", ap)
    caracteres_N=ap[0]+r1[0]+am[0]+nom[0]
    Nom_AP={
        "Nombre":nom,
        "Apellido Paterno":ap,
        "Apellido Materno":am
        }
    nombre=ap+" "+am+" "+nom
    return Nom_AP, caracteres_N, nombre

def Fecha_Nacimiento(Date_User,c_DN):
    while True:
        year=input("Introduce el año de tu nacimiento:")
        try:
            chek=int(year)
            if chek>1582:
                xy=year[len(year)-2]+year[len(year)-1]
                break
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

def Clave_Diferenciasdora():
    cn=["0","1","2","3","4","5","6","7","8","9","&","A","B","C","D","E","F","G","H","I","","J","K","L","M","N","O","P","Q","R","","","S","T","U","V","W","X","Y","Z","Ñ"]
    t_v=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]
    valores=[]
    for i in nombre:
        if i==' ':
            valores.append("0")
        else:
            for j in range(0,len(cn),1):
                if i==cn[j]:
                    valores.append(j)
    presum="".join(map(str,valores))
    suma=0
    for c in range(0,len(presum),1):
        if c<(len(presum)-1):
            b=presum[c]+presum[c+1]
            a=int(b)*int(presum[c+1])
            suma=suma+a
        else:
            suma=suma+int(presum[len(presum)-1])
    dumi=str(suma)
    ulitrhree=dumi[1]+dumi[2]+dumi[3]
    cociente=int(ulitrhree)//34
    residuo=int(ulitrhree)%34
    dig_hmc=t_v[cociente]+t_v[residuo]
    return dig_hmc  
#Datos ingresados    
Nom_AP={}
Date_User={}
#Caracteres
c_NA=c_DN=nombre=""
(Nom_AP,c_NA,nombre)=Nombre(Nom_AP,c_NA,nombre)
(Date_User,c_DN)=Fecha_Nacimiento(Date_User, c_DN)
c_DH=Clave_Diferenciasdora()
RFC_H=c_NA+c_DN+c_DH
print(RFC_H)
