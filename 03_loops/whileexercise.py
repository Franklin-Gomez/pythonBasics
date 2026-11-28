###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# contador = 0 

# while contador < 10 : 
#     contador += 1
#     print(contador)

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# contador = 1 
# sumatoria = 0

# while contador <= 20 : 
#     if  contador % 2 == 0 : 
#         sumatoria += contador    
#         print( sumatoria )
#     contador += 1

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# ------------ Mi solucion ------------------------------
# contador = 1
# sumatoria = 1

# Input_valor = int( input("Ingrese un numero entero positivo : "))
 
# while contador < Input_valor  :
#     sumatoria = sumatoria  * ( contador + 1)
#     contador += 1 

# print(f"El factorial es {Input_valor}")

# ---------------- Solucion IA -----------------------------
# while True:
#     try:
#         numero = int(input("Ingresa un entero positivo: "))
#     except ValueError:
#         print("Debe ser un número entero.")
#         continue # termina esta vuelta aqui. Inicia la otra

#     if numero > 0:
#         break
#     print("Debe ser positivo.")

# contador = 1
# factorial = 1

# while contador <= numero:
#     factorial *= contador
#     contador += 1

# print(f"El factorial de {numero} es {factorial}")
    
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# password = input("Ingrese una contraseña : ")

# while len(password) < 8 :
#     password = list(input("Ingrese una contraseña mayor a 8 caracteres  : "))

# print("Contraseña válida")


    # Ejercicio 5: Tabla de multiplicar
    # Pide al usuario que introduzca un número.
    # Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# numero = int(input("Ingrese numero a multiplicar : "))
# i = 1 
# while i <= 10 :
#     resultado = numero * i 
#     print( f"{numero} x { i } = { resultado }")
#     i+= 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

# numero = int(input("Ingrese un numero : "))

# candidatos_primos = 2
# primos: list[int] = []

# while candidatos_primos <= numero:
#     i = 1
#     cantidad_divisores = 0          # se reinicia para cada candidato

#     while i <= candidatos_primos:
#         if candidatos_primos % i == 0:
#             cantidad_divisores += 1     # aquí solo se cuenta
#         i += 1

#     if cantidad_divisores == 2:         # aquí se decide
#         primos.append(candidatos_primos)

#     candidatos_primos += 1

# print(primos)





















