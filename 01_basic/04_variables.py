# 04 - variables
# Las varaibles sirven para guardar datos en memoria 
# python es un lenguaje de tipado dinamico y de tipado fuerte 

age = 20 # variable de tipo entero
print(age) # imprime el valor de la variable age
age = 30 # reasignando un nuevo valor a la variable age
print(age) # imprime el nuevo valor de la variable age


# tipado dinamico : el tipo de dato se termine en tiempo de ejecucion 
# no es necesario declarar el tipo de dato de la variable

name = "Juan" # variable de tipo string
#print(type(name)) # imprime el tipo de dato de la variable name

#tipado fuerte : python no realiza conversione de tipo automaticamente
#print( 10 + "10") # esto genera un error de tipo

# f-string ( literal de cvadena de formato)
print( f"Hola mi nombre es {name} y tengo {age} años") # imprime un mensaje con las variables name y age

# no recomendada forma de asignar variables 
name , age , city = "Juan" , 20 , "Madrid" # asignando valores a las variables name, age y city

# Convensiones de nombre de variables
mi_nombre_de_usuario = "Juan" # snake_case, la mas recomendada

miNombreDeUsuario = "Juan" # camelCase
MiNombreDeUsuario = "Juan" # PascalCase, no recomendado para variables

MI_CONSTANTE = "Juan" # UPPER_CASE, recomendado para constantes, aunque python no tiene constantes

is_user : bool = True # esto de bool es una anotacion de tipo, no es el tipo que espera como en js 
print( is_user) # imprime el valor de la variable is_user

# por eso algo como esto es valido en python, aunque no es recomendable

is_user = "Juan" # reasignando un nuevo valor a la variable is_user, ahora es de tipo string
print( is_user) # imprime el nuevo valor de la variable is_user