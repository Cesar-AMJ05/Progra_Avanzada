# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 05:17:07 2022

@author: cesar
"""
#Ejercicio26
print("Ejercicio 26,Cifrado Cesar")
def ingresar_texto():
    while True:
        swp=input('Ingresa un Una palabra o frase por favor:')
        stxt=[]
        try:
            stxt=swp.split()
            re="".join(stxt)
            key=re.isalpha()
            if(key):
                print("Procesando... (⌐■_■)\n")
                break
            else:print("\n¡Solo caracteres alfabeticos(sin signos o numeros)! ༼ つ ◕_◕ ༽つ")      
        except:
            print("\n¡Solo caracteres alfabeticos! ༼ つ ◕_◕ ༽つ")      
    return stxt

def ingresar_num():
    while True:
        swp=input('Ingresa un numero ENTERO POSITIVO para realizar los movimentos para el cifrado por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
codigo=""
rec=ingresar_texto()
texto=" ".join(rec)
num= ingresar_num()
alfb=list(map(chr,range(97,123)))
alfb.insert(14,"ñ")
for letra in texto.lower():
    if letra in alfb:
        indice = alfb.index(letra)
        indicec = indice + num
        if indicec > 27:
            indicec -= 27
        codigo += alfb[indicec]
    else:
        codigo += letra
print(f"Texto a cifrar --> {texto}\n")
print(f"Texto cifrado  --> {codigo}\n")
print(f"Num.Desplazamientos= {num}")
