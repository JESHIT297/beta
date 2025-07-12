'''
Script description:
Crea un script Python que lance dos dados N veces y vizualice por pamtalla los res+ultados.

La cantidad o número de veces debe ser ingresada por el usuario 
Deben lanzar dos dados 
Udar función
'''

import os
from random import randint

lan = int(input('Cunatas veces deseas lanzar los dados?:'))

i = 1
while i <= lan :
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"Lanzamiento {i}")
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")
    print("\n")

    i+=1