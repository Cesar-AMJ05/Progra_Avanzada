# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:16:53 2022

@author: cesar
"""
#Ejercicio05
#Se realiza en base 11
"""
11^0= 1
11^1=11
11^2=121
11^3=1331
"""
#De esa forma construimos el T.Pascal
print("Ejercicio 5,Triangulo de Pascal")
def ingresar():
    while True:
        swp=input('Ingresa un numero ENTERO POSITIVO\npara los niveles del T. Pascal,por favor:')
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0):
                print("Procesando... (⌐■_■)\n")
                break
        except:
            print("\n¡NUMERO ENTERO POSITIVO! ༼ つ ◕_◕ ༽つ")      
    return swp
a=ingresar()
for i in range(a):
    print(' '*(a-i),end='')
    print(' '.join(map(str, str(11**i)))) 
    #.join concatena valores ene ste caso con un espacio
    #despues  con la funcion map se "suman" de ese modo acomodandolos
#Fuente, lo vi en pero para un triangulo con asteriscos
