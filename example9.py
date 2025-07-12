'''
Generar una lista de números teneindo en cuenta un númro de inicio (li) y un número de fin (ls).

Los numeros deben ser ingresados por el usuario.

Si el primer número es mayor que el segundo, la lista se debe imprimir en orden desendente. 
'''
import os

os.system('clear')
li = int(input("ingresa limite inferior:"))
ls = int(input("Ingresa limite superior"))

i = li
if li <= ls:
    while i <= ls:
        print(i)
        i+=1
else:
    while i >= ls:
        print(i)
        i-=1