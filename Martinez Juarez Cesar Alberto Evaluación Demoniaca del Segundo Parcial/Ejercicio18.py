# -*-cding: utf-8 -*-
"""
Created on Tue Apr 19 17:11:41 2022
@author: cesar
Ejercicio18-Pendulo Simple Amortiguado

Notas: 
    Antes de iniciar, ejecute el codigo 
    
    %matplotlib auto
    
    Escriba la instruccion anterior en la consola y presione enter
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
def IngresarDatos(m,l,B,g,J,t_m):
    while True:
        m=input("Ingresa la masa del pendulo en kg:")
        try:
            m=float(m)
            if m>=1:break
            else:print("Por favor un valor de masa m>0")
        except:print("Por favor un valor de masa m>0")
        
    while True:
        l=input("Ingresa la longuitud del pendulo en metros:")
        try:
            l=float(l)
            if l>=1:break
            else:print("Por favor un valor de longuitud l>0")
        except:print("Por favor un valor de longuitud l>0")
        
    while True:
        B=input("Ingresa el coef. de Friccion Viscosa:")
        try:
            B=float(B)
            if B>=0:break
            else:print("Por favor un valor de masa b≥0")   
        except:print("Por favor un valor de masa b≥0")   

    while True:
        t_m=input("Ingresa el tiempo de simulacion:")
        try:
            t_m=int(t_m)
            if t_m>=1 and t_m<=200  :break
            else:print("Por favor un tiempo 0<t<200") 
        except:print("Por favor un tiempo 0<t<200")        
        
    g=9.8 #gravedad m/s^2
    J=(m)*(1.)**2#Momento de Inercia en kg.m^2
    return m,l,B,g,J,t_m

#Inicia, se toman los datos obtenidos    
m=l=B=g=J=t_m=0
(m,l,B,g,J,t_m)=IngresarDatos(m, l, B, g, J,t_m)
#Se crea tabla con datos
var=[m,l,B,g,J]
ind=["m","l","B","g","J"]
let=["Masa","Long.Pendulo","C.Friccion","Graveda","M.Inercia"]
u=["kg","m","N.m/(rads/s)","m/s^2"]
print(f"Datos del sistema para simulacion de {t_m} segundos")
for i in range(0,4,1):
    print(f"{let[i]}={ind[i]}={var[i]} {u[i]}")
#Se crea los parametros iniciales para el sistema
t=0
tetha=1.5
xtetha=0
dt=0.5
u=np.array([tetha,xtetha])
#Se crean las funciones, se aplica el cambio de variable y se crea el conjunto
#de Ec. Diferenciales de primer orden
def f(u,t): return (1/J)*(-B*u[1]-(m*g*l)*np.sin(u[0]))
def F(u,T): return np.array([u[1],f(u,t)])
tsol=[t]
sol_tt=[u[0]]
omegasol=[u[1]]
dt=0.05
tfin=t_m
#Se crean los pasos y con el metodo de Euler se realiza la solucion al sitema
while t<tfin:
    u=u+F(u,t)*dt
    t=t+dt
    sol_tt.append(u[0])
    omegasol.append(u[1])
    tsol.append(t)
    
#Se usa pandas para el estilo 
plt.style.use("dark_background")    
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # gris claro
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#1E2247'  # gris azulada oscuro
color='#00ff41'
df=pd.DataFrame({'A':sol_tt})
fig, ax = plt.subplots()
df.plot(color=color, ax=ax)
#Las sombras 
n_shades = 10
diff_linewidth = 1.05
alpha_value = 0.3 / n_shades
# Ahora si colocar los valores de los colores de las líneas
for n in range(1, n_shades+1):
    df.plot(linewidth=2+(diff_linewidth*n),alpha=alpha_value,legend=False,ax=ax,color=color)
ax.grid(color='#2A3459')
if B<(m*l*g):
    plt.title("Subamrotiguado")
elif B==(m*l*g):
    plt.title("Criticamente amrotiguado")
elif B>(m*g*l):
    plt.title("Sobre amrotiguado")
ax.set_ylabel('Amplitud m')
ax.set_xlabel('Tiempo t')
plt.show()


#Se crea la animacion
fig=plt.figure()
ax=fig.gca()
def actualizar(i):#se hace la graficacion del pendulo
    ax.clear()
    plt.plot([0,l*np.sin(sol_tt[i])],[0,-l*np.cos(sol_tt[i])],'b-')
    plt.plot(l*np.sin(sol_tt[i]),-l*np.cos(sol_tt[i]),'ro')
    plt.title(str(round(tsol[i],3)))
    plt.xlim(-l-1,l+1)
    plt.ylim(-l-1,1)

ani=animation.FuncAnimation(fig, actualizar, range(len(tsol)))
plt.show()

