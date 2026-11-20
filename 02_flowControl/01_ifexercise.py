###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


# solucion ejercicio 1 
# numero1 , numero2 = input ( "Ingresa dos numeros : \n" ).split()

# if numero1 > numero2 :
#     print(f"numero {numero1} es mayor")

# elif numero2 > numero1 :
#     print(f"numero {numero2} es mayor")
# else: 
#     print("Los numeros son iguales") 


#solucion ejercicio 2 
# numero1 , numero2 , operador  = input ( "Ingresa dos numeros y el operador a efectuar : " ).split()

# if operador == "+": 
#     print ( int(numero1) + int(numero2) )

# elif operador == "*":
#     print ( int(numero1) * int(numero2) )

# elif operador == "-": 
#     print ( int(numero1) - int(numero2))

# else: 
#     print( int(numero1) / int( numero2) )


# solucion ejercicio 3 
# año = int(input("Ingresa el año para saber si es viciesto : "))


# if año % 4 == 0 : 
#     if año % 100 == 0 : 
#         if año % 400 == 0 : 
#             print( "Año Bisiesto")
#         else : 
#             print("Año No Bisiesto") 
#     else: 
#         print("Año Bisiesto")
# else : 
#     print("Año No Bisiesto")

# if (año % 4 == 0 and año % 100 != 0 ) or año % 400 == 0 : 
#     print("Año bisiesto")
# else : 
#     print( "Año no bisiesto ") 

# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


# solucion ejercicio 4 
# edad = int(input("Ingresa la edad : "))


# if edad >= 0 and edad <= 2 : 
#     print("Compae eres un Bebe")
# elif edad >= 3 and edad <= 12 : 
#     print("Compae eres un niño")
# elif edad >= 13 and edad <= 17 : 
#     print("compae eres un adolescente")
# elif edad >= 18 and edad <= 64 : 
#     print("compae eres un adulto")
# else : 
#     print("compae eres un adulto mayor")