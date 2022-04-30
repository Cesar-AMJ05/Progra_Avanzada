# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 04:27:01 2022

@author: cesar
https://support.microsoft.com/es-es/topic/cómo-descargar-idiomas-de-texto-a-voz-para-windows-10-d5a6b612-b3ae-423f-afa5-4f6caf1ec5d3
"""
import matplotlib.pyplot as plt
from urllib import request
import string
import pandas as pd
# Definimos la URL del archivo a descargar
def Hackeo_XD():
    remote_url = 'https://automatetheboringstuff.com/files/rj.txt'
    local_file = 'Romeo_and_Juliet_by_William_Shakesperare.txt' 
    request.urlretrieve(remote_url, local_file)# Descarga y se guarda localmente
    lineas = open('Romeo_and_Juliet_by_William_Shakesperare.txt').read().split('\n')
    selector=[]
    #[63] y [4483]
    for i in range(0,len(lineas),1):
        if i>=63 and i<=4483:
            selector.append(lineas[i])
    lectura="\n".join(selector)
    return lectura

def Re_Scrib():
    #Reescribimos el texto, quedando solo con la novela
    re_scrib=open('Romeo_and_Juliet_by_William_Shakesperare.txt','w')
    re_scrib.write(lectura)
    re_scrib.close()

def Estadistica():
    lt_d=list(string.ascii_lowercase)
    fre_abs=[];fre_rel=[];fre_ac=[];fre_arm=[];n=[]
    fre_abs=Conteo_Barras()
    b=c=0
    for i in fre_abs:fre_rel.append(i/100)
    for i in range(0,len(fre_rel),1):
        c=c+fre_abs[i]
        fre_ac.append(c)
    for i in range(0,len(fre_rel),1):
        b=c+fre_rel[i]
        fre_arm.append(b)
    for i in range(0,len(fre_abs),1):n.append(lt_d[i])
    da={'X':n,'Frecuencia abs':fre_abs,'Frecuencia rel':fre_rel,'F.Abs.Acumfre_ac':fre_ac,'F.Abs.Re':fre_arm}
    tabla=pd.DataFrame(data=da)
    print(tabla)
    plt.figure(2)
    plt.hist(fre_abs,color='#FE53BB',edgecolor='black')
    plt.title("Histrograma letras de Romeo and Juliet by William Shakesperare ")
    plt.grid()
    plt.show()             
    

    
def Conteo_Barras():
    lt_d=string.ascii_lowercase
    lt_u=string.ascii_uppercase     
    suma_min=[];suma_may=[];suma_tot=[]
    lt=[]
    for i in lt_d:
        suma=0
        for j in lectura:
            if i==j:
                suma=suma+1
        suma_min.append(suma)
    for i in lt_u:
        suma=0
        for j in lectura:
            if i==j:
                suma=suma+1
        suma_may.append(suma)
    
    for i in range(0,26,1):
        suma_tot.append(suma_may[i]+suma_min[i])
        
    for i in range(0,26,1):
        lt.append(lt_d[i]+"t")
    
    #plt.style.use('ggplot')
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=1,ncols=3,figsize=(8,5))
    plt.subplots_adjust(wspace=0.5)
    fig.suptitle('Numero de apariciones de letras minusculas, mayusculas y totales')
    ax1.barh(list(lt_d),(suma_min))
    ax2.barh(list(lt_u),(suma_may))
    ax3.barh((lt),(suma_tot))
    return suma_tot

plt.close(1)
plt.close(2)
lectura=Hackeo_XD()
Re_Scrib()
Estadistica()





