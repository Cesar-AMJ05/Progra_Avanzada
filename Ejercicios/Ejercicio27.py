# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:20:17 2022

@author: cesar
"""
#Ejercicio 27
print("Ejercicio 27,Verificar si una palabra/frase es un palindromo")
def ingresar():
    while True:
        swp=input('Ingresa una palabra o frase por favor:')
        try:
            key=True
            if(key==True):
                print("Procesando... (⌐■_■)\n")
                break
            else:print("\n¡Solo palabras y/o frases! ༼ つ ◕_◕ ༽つ")      
        except:
            print("\n¡Solo palabras y/o frases! ༼ つ ◕_◕ ༽つ")      
    return swp

def decision():
    while True:
        respuesta =input("¿Quieres verificar otra palabra y/o frase si es palindromo? [Si/No]=")
        try:
            des=str(respuesta)
            if(des=="si" or des=="SI" or des=="Si"):
                acceso=True
                break
            elif(des=="no" or des=="NO" or des=="No"):
                acceso=False
                break
            else:print("¡Escribe SI o NO! ༼ つ ◕_◕ ༽つ")                
        except:
            print("¡Escribe SI o NO! ༼ つ ◕_◕ ༽つ")
    return acceso

dnw=True
while dnw:
    A=[]
    texto=ingresar()
    init=texto
    Cleaner=["!","¡","#","$","%","&","/","(",")","=","¿","?",".",";",",",".",":","_","-"," "]
    for i in range (len(Cleaner)):
        texto=texto.replace(Cleaner[i],"")
    Cleaner2=(("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"))
    for a, b in Cleaner2:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    A=list(texto.lower())
    B=A.copy()
    B.reverse()
    if(" " in init):
        tipo="frase"
    else:tipo="palabra"
    if(A==B):
        print(f"Tu {tipo} [{init}] SI es un palindromo")
    else:print(f"Tu {tipo} [{init}] NO es un palindromo")
    w=decision()
    if w==True:
        continue
    else:
        break
        dnw=False
        print("Nos vemos...\^o^/")