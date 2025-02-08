# Que el programa primos.py reciba como input desde la terminal un número entero positivo
# y devuelva como resultado un texto que indique si dicho número es o no primo.
#Tenga en cosideración lo siguiente:
#Sí se entrega como input un número decimal el programa debe arrojar un error.
#Sí se entrega como input un número que sea 0 o negativo debe imprimir un mensaje que indique que dicho número no es válido.
#Sí se entrega un número primo debe indicar en un mensaje este hecho.
#Sí se entrega un número compuesto (no primo) debe indicar en un mensaje este hecho,
#así como también mostrar una descomposición de dos divisores (i.e.si se da como input el 4, el mensaje debe señalar que "2*2 = 4").

import argparse # Solo se necesita esta librería.

parser = argparse.ArgumentParser() # Módelo de argumentos 
parser.add_argument("n", type = int) # Se incorporó un nuevo argumento, que es n

args = parser.parse_args() # Transforma a lenguaje Python.
n = args.n # Para que pueda leerlo Python 

if n <= 0: # La condición, sí es menor a 0...
    print("Ingrese un número natural")
elif n <= 2: # Sí es menor o igual a 2...
    print(f"El número {n} es primo") # 1 y 2 son primos por default
else:
    escompuesto = False # Se creo una variable dónde dice es compuesto igual a Falso, cuando no encuentra un compuesto
    divisor = 2 # Un divisor es igual a 2
    while divisor < n: # Mientras el divisor sea menor a n 
        if n % divisor == 0: # Sí el módulo de esta división es 0
            escompuesto = True # Entonces el compuesto es igual a True.
            break # Que se detenga aquí porque quiere decir que ya cumplio, es para terminar while.
        divisor += 1
    if not escompuesto: # Sí no es compuesto
        print(f"El número {n} es primo")
    else: # En caso contrario el número n es compuesto y se cumple el divisor que se llegue a tener * la división señalada y de igual a n.
        print(f"El número {n} es compuesto.\nSe cumple que {divisor}*{int(n/divisor)} = {n}"
              )