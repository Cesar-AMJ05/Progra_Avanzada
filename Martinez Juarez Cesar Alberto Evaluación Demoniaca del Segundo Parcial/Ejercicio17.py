# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:31:03 2022
@author: cesar
Ejercicio17-Juego de la Vida
"""
import pygame
import numpy as np
import time

WIDTH, HEIGHT = 700, 700
nX, nY = 80, 80
xSize = WIDTH/nX
ySize = HEIGHT/nY

def Juego():
    pygame.init() #Inicia Pygame
    
    screen = pygame.display.set_mode([WIDTH,HEIGHT]) # Tamaño de pantalla
    
    BG_COLOR = (5,5,5) # Color Fondo
    LIVE_COLOR = (0,255,0)#Color para celda viva
    DEAD_COLOR = (125,125,125)#Color para celda muerta
    # Celdas vivas = 1; Celdas muertas = 0
    estado_game = np.zeros((nX,nY)) # Iniciar estado de celdas
    
    pauseRun = False
    
    running = True
    while running:
        n_egame = np.copy(estado_game) 
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            if event.type == pygame.KEYDOWN:
                pauseRun = not pauseRun
    
            mouseClick = pygame.mouse.get_pressed()
            if sum(mouseClick) > 0:
                posX, posY = pygame.mouse.get_pos()
                x, y = int(np.floor(posX/xSize)), int(np.floor(posY/ySize))
                n_egame[x,y] = not mouseClick[2]
    
        screen.fill(BG_COLOR) 
    
        for x in range(0,nX):
            for y in range(0,nY):
    
                if not pauseRun:
                    # Numero de vecinos
                    nNeigh = estado_game[(x-1)%nX,(y-1)%nY] + estado_game[(x)%nX,(y-1)%nY] + \
                            estado_game[(x+1)%nX,(y-1)%nY] + estado_game[(x-1)%nX,(y)%nY] + \
                            estado_game[(x+1)%nX,(y)%nY] + estado_game[(x-1)%nX,(y+1)%nY] + \
                             estado_game[(x)%nX,(y+1)%nY] + estado_game[(x+1)%nX,(y+1)%nY]
    
                    # Regla 1: Una celula muerta con 3 vecinas revive
                    if estado_game[x,y] == 0 and nNeigh==3:
                        n_egame[x,y] = 1
    
                    # Regla 2: Una celula viva con mas de 3 vecinos o menos de 2 muere
                    elif estado_game[x,y] == 1 and (nNeigh < 2 or nNeigh > 3):
                        n_egame[x,y] = 0
                poly = [(x*xSize,y*ySize),
                        ((x+1)*xSize,y*ySize),
                        ((x+1)*xSize,(y+1)*ySize),
                        (x*xSize,(y+1)*ySize)]
                if n_egame[x,y] == 1:
                    pygame.draw.polygon(screen,LIVE_COLOR,poly,0)
                else:
                    pygame.draw.polygon(screen,DEAD_COLOR,poly,1)
        estado_game = np.copy(n_egame)
        time.sleep(0.1)
        pygame.display.flip()
    pygame.quit()

def Reglas():
    while True:
        inicio=str(input("""
El juego de la Vida
¿Como usar?
1.-Para colocar celdas a tu criterio para observae el comportamiento
preciona espacio y coloca las que sean a tu criterio
2.-Vuelve a precionar espacio y deja que el juego empieze
3.-Si deseas poner mas celdas vivas repite el paso 1
Pulsa enter para ejecutar ᓚᘏᗢ:"""))
        if inicio=="":
            break
        else: break
    Juego()
    
Reglas()