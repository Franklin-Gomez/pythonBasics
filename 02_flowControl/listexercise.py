# import math 

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

# Solucion ejercicio 1 
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

# secreto = mensaje[-7:]
# print(secreto)

# solucion ejercicio 2
# numeros = [10, 20, 30, 40, 50]
# init = numeros[0]

# numeros[0] = numeros[-1]
# numeros[-1] = init
# numeros[0], numeros[-1] = numeros[-1] ,numeros[0] #tuple swap
# print( numeros) 

# Solucion ejercicio 3
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]

# sandwich = pan + ingredientes + pan_abajo

# print(sandwich)

# Solucion ejercicio 4 
# lista = [1, 2, 3]
# lista += lista

# print( lista )

# Solucoion ejercicio 5 
# lista = [10, 20, 30, 40, 50]

# tamaño = len( lista )
# indice_centro = tamaño / 2

# -------- otra solucion 
# valor_centro = lista[ int(indice_centro) : int(indice_centro) + 1 ]

# print(valor_centro[0] )

# ------ una solucion --------

# redondeo_arriba = math.ceil(indice_centro)
# redondeo_abajo = math.floor(indice_centro)

# valor_centro = lista[redondeo_abajo : redondeo_arriba ]

# print(valor_centro[0])

# -------- otra solucion ---------

# valor_centro = lista[ int(indice_centro )]

# print( valor_centro )


# solucion ejercicio 6 
lista = [1, 2, 3, 4, 5, 6]

size = len( lista )

indice_centro = size // 2 # operador que me da entero enseguida

half_lista = lista[ : indice_centro ]

invert_half_list = half_lista[::-1]

solution = invert_half_list + lista[ indice_centro : ]

print( solution )