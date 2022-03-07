# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 01:16:16 2022

@author: cesar
"""

#Ejercicio12
print("Ejercicio 12, Abecedario chimuelo")
print("HOLA (⌐■_■), a continuacion se muestra el \nabecedario completo y las letras cuya posiscion es multiplo de 3")
a=list(map(chr,range(97,123)))
a.insert(14,"ñ")
b= "".join(a)
B=[val for i, val in enumerate(b) if i%3==0]
print(f"El abecedario completo:\n\n{a}\n\nY el abecedario con las letras multiplo de 3\n\n{B}")

