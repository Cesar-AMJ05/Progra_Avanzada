# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:58:23 2022
@author: cesar
Ejercicio08-Python Scripts
Cartas Baraja Inglesa
"""
import random
import time

class Carta:
    def __init__(self,suit,rango):
        self.suit=suit
        self.rango=rango
    def __str__(self):
        if self.rango=="J":
            return self.rango+"-"+self.suit
        else:
            return self.rango+" de "+self.suit

class Conjunto_Naipes:
    def __init__(self):
        self.rango=["As","2","3","4","5","6","7","8","9","10","Sota","Reina","Rey"]
        self.suit=["Espadas","Corazones","Diamantes","Bastos"]
        self.baraja=[]
        for i in self.suit:
            for j in self.rango:
                self.baraja.append(Carta(i,j))
        for n in range(2):
            self.baraja.append(Carta("Joker","J"))

    def deal(self):
        suerte=random.choice(self.baraja)
        self.baraja.remove(suerte)
        return suerte
    
def Mesa():
    baraja=Conjunto_Naipes()
    P1_Mano=[]
    P2_Mano=[]
    for n in range(5):
        P1_Mano.append(baraja.deal())
        P2_Mano.append(baraja.deal())
    
    print("---Cartas Jugador 1---")
    for w in P1_Mano:
        print(w)
    print("---Cartas Jugador 2---")
    for x in P2_Mano:
        print(x)

inicio=Mesa()
while True:
    print('Ingresa "si" para continuar o "no" para salir' )
    task=str(input("¿Quieres volver a Repartir?:").lower())
    key=False
    try:
        if task=="si":
            key=True
            print("Volviendo a Repartir, Espera")
            time.sleep(1)
            Mesa()
        elif task=="no":
            print("Hasta Luego...")
            key=False
            break  
    except:
        print("Selecciona una Opcion valida [si/no]")