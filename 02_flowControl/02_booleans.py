
# operadores de comparacion : devuelven un valor booleano (True o False)

import os

os.system("cls") # limpiar pantalla
print ("\nBoleanos")

print(True)
print(False)

print ("\nOperadores de comparacion")

print(5 > 3) # True
print(5 < 3) # False
print(5 >= 3) # True
print(5 <= 3) # False
print(5 == 3) # False
print(5 != 3) # True

print ("\nOperadores de cadena de texto")

# Comparacion de cadenas de texto, se comparan letra por letra, si la primera letra es mayor que la segunda, devuelve True, si es menor devuelve False.

# no compara longitud de la cadena 
# Es sensible a la mayuscula tambien 

print("Hola" == "Hola") # True
print("Hola" == "Adios") # False    
print("Hola" == "hola") # False

