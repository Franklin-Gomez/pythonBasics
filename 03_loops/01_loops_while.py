##
## 01 - Bucles ( while )
# permite ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion 

print("\nBucle while: ")

# Bucle con una  simple condicion 
# contador = 0 
# while contador <= 5 : 
#     print( contador )
#     contador += 1 # condicion de salida, evita el bucle infinito 

# utilizando la palabra break, para romper el bucle
# contador2 = 0
# while True : 
#     print( contador2 )
#     contador2 += 1 
#     if contador2 == 5:
#         break # sale del bucle

print("\nBucle con continue:")
# continue, lo que hace es saltar esa iteracion en concreto y continuar en el bucle 

# contador3 = 0
# while contador3 < 10 : 
#     contador3 += 1 

#     if contador3 % 2 == 0 :
#         continue # manda a la siguiente iteracion
    
#     print( contador3 )

print("\nBucle while con else:")
# else, esta condicion cuando se ejecuta? 
# contador4 = 0 
# while contador4 < 5:
#     print(contador4)
#     contador4 += 1 
#     # break , si usas break no se activa el else
# else:
#     print("El bucle ha terminado ")^


# pedirle al usuario un numero que tiene que ser positivo 

# contador5 = -1 

# while contador5 < 0:
#     contador5 = int(input("Ingresa un numero positivo  : "))

#     if contador5 < 0 : 
#         print("El numero debe ser positivo ")

# print(f"Elnumero que has introducido es { contador5}")

print("\nBucle while con try except:")

# try except en bucles while 
contador5 = -1 

while contador5 < 0:
    try: 
        contador5 = int(input("Ingresa un numero positivo  : "))
        if contador5 < 0 : 
            print("El numero debe ser positivo ")

    except ValueError:  # ValueError por el error que espero es de str a int 
        print("lo que introduces debe ser un numero  ")

print(f"Elnumero que has introducido es { contador5}")