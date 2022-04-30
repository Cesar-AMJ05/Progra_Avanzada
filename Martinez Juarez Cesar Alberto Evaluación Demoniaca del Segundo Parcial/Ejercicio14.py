# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 01:36:02 2022
@author: cesar
Ejercicio 14- Problema de las 8 reinas
"""
import numpy as np

def ingresar():
    while True:
        num = input("Ingresa un numero positivo del  1 al 8:")
        try:
            if num.isnumeric() and int(num)>0 and int(num)<9:
                return int(num)
            else:
                print("Solo un numero del intervalo [1,8]:")
        except:print("Ingresa un numero positivo del  1 al 8:")

class Num_Reinas:
    resultados = np.empty((92,8,8), dtype="str")
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.Colocar(positions, 0)
        print("Ingresa tu fila de la primera dama")
        fila = ingresar()-1
        print("Ingresa tu columna de la primera dama")
        columna = ingresar()-1

        self.filtrar(fila, columna)

    def Colocar(self, positions, piv):
        
        if piv == self.size:
            self.tablero(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.ver_pos(positions, piv, column):
                    positions[piv] = column
                    self.Colocar(positions, piv + 1)

    def ver_pos(self, positions, r_ocp, column):

        for i in range(r_ocp):
            if positions[i] == column or \
                    positions[i] - i == column - r_ocp or \
                    positions[i] + i == column + r_ocp:
                return False
        return True

    def tablero(self, positions):
        for row in range(self.size):
            for column in range(self.size):
                if positions[row] == column:
                    self.resultados[self.solutions, row, column] = "Q"
                else:
                    self.resultados[self.solutions, row, column] = "■"

    def filtrar(self, fila, columna):
        i = 0
        validas = []
        for tablero in range(92):
            if self.resultados[tablero, fila, columna] == "Q":
                validas.append(tablero)
                i += 1
        opciones = 1
        for tablero in validas:
            print(f"Opcion numero: {opciones}")
            print(self.resultados[tablero])
            opciones += 1

def main():
    Num_Reinas(8)
if __name__ == "__main__":
    main()