# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:59:41 2022

@author: cesar
"""

def Juego(n , origen, destino, auxiliar):
     
      if n==1:
          print (f"Mueve el disco '{n}' del origen '{origen}' al destino '{destino}'")
          return
      Juego(n-1, origen, auxiliar, destino)
      print (f"Mueve el disco '{n}' del origen '{origen}' al destino '{destino}'")
      Juego(n-1, auxiliar, destino, origen)
    
def ingresar():
    while True:
        swp=input("Ingrese hasta que numero de discos que queire mover(De 3 a 15 discos):")
        try:
            swp=int(swp)
            if(swp >= 0 and swp % 1 == 0 and swp>=3 and swp<=15):break
            else:print("Por favor elige un numero de discos del intervalo [3,15]\n")
        except:print("Por favor elige un numero de discos del intervalo [3,15]\n")    
    return swp    
 
print("""
Torre de Hanoi
A continuacion se mostraran los pasos para resolver el juego 
para n discos que usted seleccione de 3 a 15 discos, por ello concidere que cada torre tendra la siguiente nomenclatura:

  *     |     |
 ***    |     |
*****   |     |
  A     B     C
      """)   
n=ingresar()                    
Juego(n,'A','B','C') 
