# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:03:26 2022

@author: cesar
"""
print("Ejercicio 23, Orden de una Frase")
frase = input("Ingresa una frase a ordenar:")
def ingresar():
    while True:
        swp=input('De que forma quiere que se ordene,\nAlfabéticamente Directa [1] o Inversa [2]:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n Selecciona [1] o [2] ༼ つ ◕_◕ ༽つ")      
    return swp

op=ingresar()
frase=frase.replace(',','')
libreta=frase.split(' ')
if op==1:
    texto=sorted(libreta)
    print("Tu frase ordenada es:\n ", ' '. join(texto))
else:
    intexto=sorted(libreta, reverse=True)
    print("Tu frase ordenada es:\n",' '.join(intexto))