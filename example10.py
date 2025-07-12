'''
Script description:
Crea un script Python que lance dos dados N veces y vizualice por pamtalla los res+ultados.

La cantidad o número de veces debe ser ingresada por el usuario 
Deben lanzar dos dados 
Udar función
'''

import os
from random import randint

i = 1
status = True
while status :
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"Lanzamiento {i}")
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")
    print("\n")
    i+=1

    status_try_again = True
    while status_try_again:
        try_again = input("Try againg [s/S/n/N]:")
        if try_again == 's' or try_again == 'S' or try_again == 'n' or try_again == 'N':
            status_try_again = False
        else:
            print("Invalid option, please press s/S/n/N")
    
    if try_again == 'n' or 'N':
        break