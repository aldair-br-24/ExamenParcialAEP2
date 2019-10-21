#hacer que el sistema genere un num. aleatorio entre 1 y 10.
#Luego hacer que el usuario adivine el num. La aplicación debe
#terminar cuando el usuario termine.

import random
a = random.randint(1,10)

while True:
    n =int(input("Adivina el número del sisema (1 ...10): "))

    if n == a:
        print("Adivinaste!")
        break
    else:
        print("Numero incorrecto")