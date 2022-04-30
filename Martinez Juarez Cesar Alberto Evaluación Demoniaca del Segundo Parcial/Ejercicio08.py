# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:46:52 2022
@author: cesar
Ejercicio08-Python Scripts
Contraseña
"""
import re
import random

def Ingresar_Contraseña():
    psw=input("Ingresa tu contraseña:")
    return psw

def Limites():
    key_Master=False
    lim_Min=lim_Num=lim_May=lim_Esp=lim_Lg=True
    print("\n")
    if not re.search("[a-z]", Contraseña):
        lim_Min=False
        print("-Debe contener al menos una letra minúscula [a-z]")
    
    if not re.search("[1-9]", Contraseña):
        lim_Num=False
        print("-Debe contener al menos un número [0-9]")
    
    if not re.search("[A-Z]", Contraseña) or Contraseña[0].isupper():
        lim_May=False
        print("-Debe contener al menos una letra mayúscula [A-Z], no en la primera posición")
        
    if not re.search("[$#@]", Contraseña):#[~!@#$%^&*+-/\{}^.:,:_]
        lim_Esp=False
        print("Debe contener al menos un caracter especial [$, #, @, _]")
    
    if (len(Contraseña)<6 or (len(Contraseña)>12)):
        lim_Lg=False
        print("Longitud mínima - máxima de la contraseña, 6-12 caracteres")
        
    if(lim_Min and lim_Num and lim_May and lim_Esp and lim_Lg):
        key_Master=True
        
    return key_Master

def Cifrado_Cesar(n=0,Contraseña=""):
    print(f"{n} y {Contraseña}")
    codigo=""
    alfb=list(map(chr,range(97,123)))
    alfb.insert(14,"ñ")
    for letra in Contraseña.lower():
        if letra in alfb:
            indice = alfb.index(letra)
            indicec = indice + n
            if indicec > 27:
                indicec -= 27
            codigo += alfb[indicec]            
        else:
            codigo += letra 
    re_wr=list(codigo)
    for i in range(0,len(re_wr),1):
        dumi=Contraseña[i]
        if dumi.isupper():
            x=re_wr[i].upper()
            re_wr[i]=x
    Contraseña_Nw="".join(re_wr)
    return Contraseña_Nw  
    
print("""
Recuerda...
Debe contener al menos una letra minúscula [a-z]
Debe contener al menos un número [0-9]
Debe contener al menos una letra mayúscula [A-Z], no en la primera posición
Debe contener al menos un caracter especial [$, #, @, _]
Longitud mínima - máxima de la contraseña, 6-12 caracteres
          """)
          
while True:
    Contraseña=Ingresar_Contraseña()      
    key_Master=Limites()
    if(key_Master):
        print("Contraseña Valida")
        move=random.randint(0,20)
        Re_Contraseña=Cifrado_Cesar(move,Contraseña)
        file=open("Contraseñas.txt","a")
        file.write(f" \n {move}         |       {Re_Contraseña}  \n")
        file.close()
        break
    else:
        print("Intente de Nuevo")

   